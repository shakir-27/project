class AIModel:
    def __init__(self, config=None):
        self.config = config or {}
        self.params = self._init_params(self.config)

    def _init_params(self, config):
        # Allocate and initialize whatever is needed for the model
        return {"weights": None, "state": {}}

    def preprocess(self, raw_batch):
        # Turn raw inputs into tensors/features as needed
        return raw_batch

    def forward(self, batch):
        # Compute predictions from inputs
        return {"preds": None, "intermediates": {}}

    def loss(self, preds, targets):
        # Compare predictions to targets
        return 0.0

    def backward(self, loss_value):
        # Compute gradients from loss
        pass

    def step(self, lr=1e-3):
        # Update parameters using gradients
        pass

    def save(self, path):
        # Persist model parameters
        pass

    def load(self, path):
        # Restore model parameters
        pass


def get_data(split="train"):
    # Yield batches of (inputs, targets)
    while True:
        inputs = {}
        targets = None
        yield {"inputs": inputs, "targets": targets}


def train(model, epochs=1, lr=1e-3):
    for _ in range(epochs):
        for batch in get_data(split="train"):
            proc = model.preprocess(batch)
            out = model.forward(proc["inputs"])
            L = model.loss(out["preds"], proc["targets"])
            model.backward(L)
            model.step(lr=lr)


def evaluate(model):
    metrics = {}
    for batch in get_data(split="val"):
        proc = model.preprocess(batch)
        out = model.forward(proc["inputs"])
        # Accumulate metrics
    return metrics


if __name__ == "__main__":
    cfg = {"model_type": "whatever", "dims": [None, None]}
    model = AIModel(cfg)
    train(model, epochs=3, lr=1e-3)
    report = evaluate(model)
    print(report)

