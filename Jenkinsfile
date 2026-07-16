pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Java') {
            steps {
                sh 'java -version'
            }
        }

        stage('Verify Git') {
            steps {
                sh 'git --version'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Verify Gradle') {
            steps {
                sh 'gradle -v'
            }
        }

        stage('Gradle Build') {
            steps {
                sh 'gradle clean build'
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: '**/build/**', fingerprint: true

        }

        success {

            echo "Build completed successfully."

        }

        failure {

            echo "Build Failed."

        }

    }

}
