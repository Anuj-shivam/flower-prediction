pipeline {
    agent any
    environment {
        REMOTE_VM = 'anuj@192.168.0.134'
        GIT_REPO = 'https://github.com/Anuj-shivam/flower-prediction.git'  // Added Git URL
        DOCKER_IMAGE_NAME = 'flowerapp'
        CONTAINER_NAME = 'flowerapp'
        REMOTE_DIR = '/home/anuj/flowerapp'
    }
    stages {
        stage('Clean Remote Directory & Clone Repo') {
            steps {
                script {
                    sshagent(credentials: ['anuj-remote-vm-ssh']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${REMOTE_VM} "
                                // Delete directory if it exists
                                if [ -d '${REMOTE_DIR}' ]; then
                                    echo 'Removing existing directory...'
                                    rm -rf ${REMOTE_DIR}
                                fi
                                // Clone repo directly on the VM
                                git clone ${GIT_REPO} ${REMOTE_DIR}
                            "
                        """
                    }
                }
            }
        }
        stage('Build & Run Docker on Remote VM') {
            steps {
                script {
                    sshagent(['anuj-remote-vm-ssh']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${REMOTE_VM} "
                                cd ${REMOTE_DIR}
                                docker build -t ${DOCKER_IMAGE_NAME} .
                                docker stop ${CONTAINER_NAME} || true
                                docker rm ${CONTAINER_NAME} || true
                                docker run -d --name ${CONTAINER_NAME} -p 8080:80 ${DOCKER_IMAGE_NAME}
                            "
                        """
                    }
                }
            }
        }
    }
}
