import math
import random

class NeuralNetwork:
    """
    A simple feed-forward neural network implemented from scratch.

    This class is designed for educational purposes to demonstrate the core
    concepts of forward propagation and backpropagation without relying on
    external libraries like NumPy or TensorFlow.
    """
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate=0.1):
        """
        Initializes the neural network architecture and weights.

        Args:
            input_nodes (int): The number of neurons in the input layer.
            hidden_nodes (int): The number of neurons in the hidden layer.
            output_nodes (int): The number of neurons in the output layer.
            learning_rate (float): The step size for weight updates during training.
        """
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        # Initialize weight matrices with small random values to break symmetry.
        # Weights connecting input layer to hidden layer
        self.weights_input_hidden = [[random.uniform(-0.5, 0.5) for _ in range(input_nodes)] for _ in range(hidden_nodes)]
        # Weights connecting hidden layer to output layer
        self.weights_hidden_output = [[random.uniform(-0.5, 0.5) for _ in range(hidden_nodes)] for _ in range(output_nodes)]

        # Placeholders for layer activations (outputs)
        self.hidden_outputs = [0.0] * self.hidden_nodes
        self.final_outputs = [0.0] * self.output_nodes

    @staticmethod
    def sigmoid(x):
        """
        The sigmoid activation function. Squashes values to a range between 0 and 1.
        
        Note: This can lead to vanishing gradients in deep networks, which is why
        functions like ReLU are often preferred in modern applications.
        """
        # Added a check to prevent overflow with large negative numbers
        if x < -500:
            return 0
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        """
        The derivative of the sigmoid function.
        
        Args:
            x (float): The output of a sigmoid function.
        """
        return x * (1 - x)

    @staticmethod
    def mean_squared_error(targets, outputs):
        """
        Calculates the Mean Squared Error loss between target and predicted values.
        """
        return sum((t - o) ** 2 for t, o in zip(targets, outputs)) / len(targets)

    def feedforward(self, inputs):
        """
        Propagates input data forward through the network.

        Args:
            inputs (list): A list of input values. Its length must match `input_nodes`.

        Returns:
            list: The final output values from the network.
        """
        if len(inputs) != self.input_nodes:
            raise ValueError(f"Input length {len(inputs)} does not match expected {self.input_nodes}")

        # 1. Calculate hidden layer outputs
        for i in range(self.hidden_nodes):
            # Calculate the weighted sum of inputs
            weighted_sum = sum(self.weights_input_hidden[i][j] * inputs[j] for j in range(self.input_nodes))
            # Apply the activation function
            self.hidden_outputs[i] = NeuralNetwork.sigmoid(weighted_sum)

        # 2. Calculate final output layer outputs
        for i in range(self.output_nodes):
            # Calculate the weighted sum of hidden layer outputs
            weighted_sum = sum(self.weights_hidden_output[i][j] * self.hidden_outputs[j] for j in range(self.hidden_nodes))
            # Apply the activation function
            self.final_outputs[i] = NeuralNetwork.sigmoid(weighted_sum)

        return self.final_outputs

    def backpropagate(self, inputs, targets):
        """
        Performs the backpropagation algorithm to update network weights.

        Args:
            inputs (list): The input values for a single training example.
            targets (list): The target values for that training example.
        """
        if len(targets) != self.output_nodes:
            raise ValueError(f"Target length {len(targets)} does not match expected {self.output_nodes}")

        # 1. Run feedforward to get current outputs and intermediate activations
        self.feedforward(inputs)

        # 2. Calculate output layer error and gradients
        output_errors = [targets[i] - self.final_outputs[i] for i in range(self.output_nodes)]
        output_gradients = [output_errors[i] * NeuralNetwork.sigmoid_derivative(self.final_outputs[i]) for i in range(self.output_nodes)]

        # 3. Calculate hidden layer errors by propagating output errors backward
        hidden_errors = [0.0] * self.hidden_nodes
        for i in range(self.hidden_nodes):
            # Sum the contributions of this hidden node to the output errors
            error_sum = sum(output_gradients[j] * self.weights_hidden_output[j][i] for j in range(self.output_nodes))
            hidden_errors[i] = error_sum
        
        # 4. Calculate hidden layer gradients
        hidden_gradients = [hidden_errors[i] * NeuralNetwork.sigmoid_derivative(self.hidden_outputs[i]) for i in range(self.hidden_nodes)]

        # 5. Update the weights from hidden to output layer
        for i in range(self.output_nodes):
            for j in range(self.hidden_nodes):
                # Calculate the weight change and apply it
                delta = self.learning_rate * output_gradients[i] * self.hidden_outputs[j]
                self.weights_hidden_output[i][j] += delta

        # 6. Update the weights from input to hidden layer
        for i in range(self.hidden_nodes):
            for j in range(self.input_nodes):
                # Calculate the weight change and apply it
                delta = self.learning_rate * hidden_gradients[i] * inputs[j]
                self.weights_input_hidden[i][j] += delta
    
    def train(self, training_data, epochs):
        """
        Orchestrates the training process over multiple epochs.

        Args:
            training_data (list): A list of (input, target) tuples.
            epochs (int): The total number of training iterations.
        """
        print("Starting training...")
        for epoch in range(1, epochs + 1):
            total_loss = 0.0
            # Train on each example in the dataset
            for inputs, targets in training_data:
                self.backpropagate(inputs, targets)
                # Recalculate output to measure loss after update
                outputs = self.feedforward(inputs)
                total_loss += NeuralNetwork.mean_squared_error(targets, outputs)
            
            # Periodically print the average loss to monitor training progress
            if epoch % 1000 == 0 or epoch == 1:
                avg_loss = total_loss / len(training_data)
                print(f"Epoch {epoch}/{epochs}, MSE Loss: {avg_loss:.6f}")
        print("Training complete.")

    def predict(self, inputs):
        """
        Makes a prediction for a given set of inputs.

        Args:
            inputs (list): A list of input values.

        Returns:
            list: The network's predicted output.
        """
        return self.feedforward(inputs)

# Main execution block to demonstrate solving the XOR problem
if __name__ == "__main__":
    # Define the XOR problem dataset
    # Inputs: [A, B]
    # Target: A XOR B
    xor_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    xor_targets = [[0], [1], [1], [0]]
    training_data = list(zip(xor_inputs, xor_targets))

    # --- Hyperparameters ---
    INPUT_NODES = 2
    HIDDEN_NODES = 3  # More than 2 nodes are needed for XOR
    OUTPUT_NODES = 1
    LEARNING_RATE = 0.5
    EPOCHS = 20000

    # Instantiate the neural network
    nn = NeuralNetwork(
        input_nodes=INPUT_NODES,
        hidden_nodes=HIDDEN_NODES,
        output_nodes=OUTPUT_NODES,
        learning_rate=LEARNING_RATE
    )

    # Train the network
    nn.train(training_data, epochs=EPOCHS)

    # Display the final predictions for each XOR case
    print("\n--- XOR Problem Predictions After Training ---")
    for inputs, targets in training_data:
        prediction = nn.predict(inputs)
        print(f"Input: {inputs} -> Target: {targets[0]} -> Predicted: {prediction[0]:.3f}")


