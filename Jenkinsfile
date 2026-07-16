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

        stage('Save Build Log') {
            steps {
                sh 'gradle clean build > build.log 2>&1'
            }
        }

        stage('AI Log Analysis') {
            steps {
                sh 'python3 scripts/analyze_logs.py'
            }
        }

    }

    post {

        always {
            archiveArtifacts artifacts: '**/build/**, build.log, reports/**', fingerprint: true
        }

        success {
            echo 'Build completed successfully.'
        }

        failure {
            echo 'Build Failed.'
        }

    }
}
