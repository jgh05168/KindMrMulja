pipeline {
    agent any

    environment{
        BACK_DOCKER_IMAGE_NAME='backend/nodejs'
        BACK_CONTAINER_NAME = 'nodejs-server'

        FRONT_DOCKER_IMAGE_NAME='frontend/vuejs'
        FRONT_CONTAINER_NAME='vuejs-client'

        DATABASE_NAME='mariadb'

    }


    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Copy env file'){
            steps{
                script{
                    sh'''
                        cp /var/jenkins_home/settingsFiles/.env ./backend/.env
                    '''
                }
            }
        }

        stage('Parallel Build Docker Image'){
            parallel{
                stage('frontend Build Docker Image'){
                    steps{
                        script{
                            sh'''
                                cd ./frontend/kind-mulja
                                docker build -t ${FRONT_DOCKER_IMAGE_NAME} .
                            '''
                        }
                    }
                }

                stage('backend Build Docker Image'){
                    steps{
                        script{
                            sh'''
                                cd ./backend
                                docker build -t ${BACK_DOCKER_IMAGE_NAME} .
                            '''
                        }
                    }
                }
            }
        }

        stage('Parallel Delete Previous Docker Container'){
            parallel{
                stage('Delete Previous Front Docker Container'){
                    steps {
                        script {
                            def frontContainerExists = sh(script: 'docker ps -a | grep ${FRONT_CONTAINER_NAME}', returnStdout: true).trim().split('\n').size()
                            echo "${frontContainerExists}"
                            if (frontContainerExists==1) {
                                echo "${frontContainerExists}"
                                sh "docker stop ${FRONT_CONTAINER_NAME}"
                                sh "docker rm ${FRONT_CONTAINER_NAME}"
                            } else {
                                echo "Frontend container does not exist. Skipping deletion."
                            }
                        }
                    }
                }
                stage('Delete Previous Back Docker Container'){
                    steps {
                        script {
                            def frontContainerExists = sh(script: 'docker ps -a | grep ${BACK_CONTAINER_NAME} || true', returnStatus: true).trim().split('\n').size()
                            echo "${frontContainerExists}"
                            if (frontContainerExists==1) {
                                echo "${frontContainerExists}"
                                sh "docker stop ${BACK_CONTAINER_NAME}"
                                sh "docker rm ${BACK_CONTAINER_NAME}"
                            } else {
                                echo "Frontend container does not exist. Skipping deletion."
                            }
                        }
                    }
                }
            }
        }


        stage('Parallel Run Docker Container'){
            parallel{
                stage('Run Front Docker Container'){
                    steps{
                        script{
                            sh "docker run -d --name ${FRONT_CONTAINER_NAME} -p 5173:5173 ${FRONT_DOCKER_IMAGE_NAME}"
                        }
                    }
                }
                stage('Run Back Docker Container'){
                    steps{
                        script{
                            sh "docker run -d --link ${DATABASE_NAME} --name ${BACK_CONTAINER_NAME} -p 3000:3000 ${BACK_DOCKER_IMAGE_NAME}"
                        }
                    }
                }
            }
        }

    }
}