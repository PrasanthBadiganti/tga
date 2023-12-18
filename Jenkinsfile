pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_UNIT_TESTS', defaultValue: true, description: 'Run unit tests?')
        booleanParam(name: 'RUN_SONAR_ANALYSIS', defaultValue: true, description: 'Run Sonar analysis?')
        booleanParam(name: 'PUBLISH_DOCS', defaultValue: true, description: 'Publish documentation to DocHub?')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Unit Tests') {
            when {
                expression { params.RUN_UNIT_TESTS == true }
            }
            steps {
                script {
                    // Run unit tests based on your testing framework
                    sh 'python -m unittest discover -s tests -p "*_test.py"'
                }
            }
        }

        stage('Sonar Analysis') {
            when {
                expression { params.RUN_SONAR_ANALYSIS == true }
            }
            steps {
                script {
                    // Run Sonar analysis commands
                    sh 'sonar-scanner'  // Replace with your Sonar scanner command
                }
            }
        }

        stage('Publish to DocHub') {
            when {
                expression { params.PUBLISH_DOCS == true }
            }
            steps {
                script {
                    // Publish documentation to DocHub
                    sh 'dochub publish'  // Replace with your DocHub publish command
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("your_docker_image_name", "-f Dockerfile .")

                    // Push Docker image to Artifactory
                    docker.withRegistry('https://your_artifactory_registry_url', 'your_artifactory_credentials') {
                        docker.image("your_docker_image_name").push()
                    }
                }
            }
        }



        stage('Deploy') {
            steps {
                // Run Docker container from the image in your environment
                script {
                    sh 'docker run -d -p 8080:8000 your_docker_image_name:latest'
                }
            }
        }
    }

    post {
        success {
            // Actions on success
        }
        failure {
            // Actions on failure
        }
    }
}

