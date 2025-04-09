pipeline {
    agent any
    environment {
        dockerimage = ''
        registry = 'anujdocker0403/flowerapp'
        registryCredential = 'Docker_id'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/Anuj-shivam/flower-prediction']]
                )
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerimage = docker.build(registry)
                }
            }
        }
        stage('Running Container') {
            steps {
                script {
                    // Stop and remove existing container (if any)
                    sh 'docker stop flowerapp || true'
                    sh 'docker rm flowerapp || true'
                    // Run the container
                    sh 'docker run -d -p 5000:5000 --name flowerapp anujdocker0403/flowerapp'
                }
            }
        }
    }
}
