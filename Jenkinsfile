pipeline {
    agent any

    environment {
        IMAGE_NAME = 'localhost:5001/demo-app'
        IMAGE_TAG  = "${IMAGE_NAME}:${BUILD_NUMBER}"
    }

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Сборка #${BUILD_NUMBER}, ветка: ${GIT_BRANCH}"
            }
        }

        stage('Build Image') {
            steps {
                script {
                    docker.build("${IMAGE_TAG}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${IMAGE_TAG}").inside {
                        sh 'pip install pytest --quiet && pytest test_app.py -v'
                    }
                }
            }
        }

        stage('Push Image') {
            steps {
                sh "docker push ${IMAGE_TAG}"
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop demo-app || true
                    docker rm   demo-app || true
                    docker run -d \
                        --name demo-app \
                        --restart unless-stopped \
                        -p 5000:5000 \
                        ${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success { echo 'Конвейер завершён успешно!' }
        failure { echo 'Ошибка конвейера — проверьте логи!' }
        always  { sh "docker rmi ${IMAGE_TAG} || true" }
    }
}
