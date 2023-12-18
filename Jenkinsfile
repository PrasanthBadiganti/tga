pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_UNIT_TESTS', defaultValue: false, description: 'Run Unit tests?')
        booleanParam(name: 'RUN_SONAR_ANALYSIS', defaultValue: false, description: 'Run Sonar analysis?')
        booleanParam(name: 'PUBLISH_DOCS', defaultValue: false, description: 'Publish documentation to DocHub?')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PrasanthBadiganti/tga.git'
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

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t my_fastapi_app .'
                    // docker.build("tga_assessment", "-f Dockerfile .")
                }
            }
        }

        stage('Deploy') {
            steps {
                // Run Docker container from the image in your environment
                script {
                    sh 'docker run -p 8000:8000 my_fastapi_app'
                }
            }
        }
    }
}

