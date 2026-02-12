pipeline {
    agent { label 'built-in' }

    stages {
        stage('Build') { // Defines the "Build" stage
            steps {
                echo 'Building the application...' // Prints a message to the console
                // Add your build commands here, e.g., mvn clean install, npm install, etc.
            }
        }

        stage('Test') { // Defines the "Test" stage
            steps {
                echo 'Running tests...' // Prints a message to the console
                // Add your test commands here, e.g., mvn test, npm test, etc.
            }
        }

        stage('Deploy') { // Defines the "Deploy" stage
            steps {
                echo 'Deploying the application...' // Prints a message to the console
                // Add your deployment commands here, e.g., scp, kubectl apply, etc.
            }
        }
    }

    post { // Defines actions to take after the pipeline completes
        always { // Actions to run regardless of pipeline outcome
            echo 'Pipeline finished.'
        }
        success { // Actions to run only if the pipeline succeeds
            echo 'Pipeline completed successfully!'
        }
        failure { // Actions to run only if the pipeline fails
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
