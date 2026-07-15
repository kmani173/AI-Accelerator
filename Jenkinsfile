pipeline {
    agent any

    stages {
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

        stage('Done') {
            steps {
                echo 'AI Accelerator Jenkins Pipeline executed successfully!'
            }
        }
    }
}
