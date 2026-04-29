pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io/cheikh9708"
        IMAGE_NAME = "flask"
        K8S_NAMESPACE = "default"
        DEPLOYMENT_NAME = "flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Verify Docker') {
            steps {
                sh 'docker --version'
                sh 'docker ps'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials',
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh """
                docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl set image deployment/${DEPLOYMENT_NAME} \
                ${DEPLOYMENT_NAME}=${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
                -n ${K8S_NAMESPACE}
                """
            }
        }
    }

    post {
        success {
            echo "✔ Pipeline réussi : image déployée"
        }
        failure {
            echo "❌ Pipeline échoué"
        }
    }
}