pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_UNIT_TESTS', defaultValue: false, description: 'Run Unit tests?')
        booleanParam(name: 'RUN_SONAR_ANALYSIS', defaultValue: false, description: 'Run Sonar analysis?')
        booleanParam(name: 'PUBLISH_DOCS', defaultValue: false, description: 'Publish documentation to DocHub?')
        booleanParam(name: 'TEST_DEPLOY', defaultValue: false, description: 'Deploy in test env?')
        booleanParam(name: 'STAGE_DEPLOY', defaultValue: false, description: 'Deploy in stage env?')
    }

    stages {
        stage('Setting Up Environment') {
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
                    sleep time: 10, unit: 'SECONDS'
                    //sh 'python -m unittest discover -s tests -p "*_test.py"'
                }
            }
        }


        stage('Build Artifact') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t fastapi_application .'
                }
            }
        }

        stage('Build and Publish Docs') {
            when {
                expression { params.PUBLISH_DOCS == true }
            }
            steps {
                script {
                    // Publish documentation to DocHub
                    // sh 'dochub publish'  // Replace with your DocHub publish command
                    sleep time: 12, unit: 'SECONDS'
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
                    sleep time: 22, unit: 'SECONDS'
                    // sh 'sonar-scanner'  // Replace with your Sonar scanner command
                }
            }
        }

        stage('AWS Test Deploy') {
            when {
                expression { params.TEST_DEPLOY == true }
            }
            steps {
                // Run Docker container from the image in your environment
                script {
                //   sh 'docker run -p 8000:8000 my_fastapi_app'
                sh 'docker-compose up -d'
                }
            }
        }

        stage('AWS Stage Deploy') {
            when {
                expression { params.STAGE_DEPLOY == true }
            }
            steps {
                // Run Docker container from the image in your environment
                script {
                    sleep time: 12, unit: 'SECONDS'
                    //sh 'docker-compose up -d'
                }
            }
        }
    }
}

