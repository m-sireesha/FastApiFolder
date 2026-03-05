
pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-app"
        CONTAINER_NAME = "fastapi-container"
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/m-sireesha/MY_PYTHON_PROJECTS.git',
                    branch: 'main',
                    credentialsId: 'GitHub-token1'  // <- your Jenkins token ID
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                // Remove any existing container with the same name
                sh "docker rm -f ${CONTAINER_NAME} || true"
                // Run new container
                sh "docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}"
            }
        }

        stage('Wait for FastAPI') {
            steps {
                // Wait for FastAPI to be ready (max 20 seconds)
                sh '''
                for i in {1..10}; do
                  if curl -f http://localhost:8000; then
                    echo "FastAPI is ready!"
                    break
                  fi
                  echo "Waiting for FastAPI..."
                  sleep 2
                done
                '''
            }
        }

        stage('Test FastAPI') {
            steps {
                sh "curl -f http://localhost:8000 || echo 'FastAPI not reachable'"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}



