def buildStatus = 0

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
                script {
                    buildStatus = sh(
                        script: 'gradle clean build > build.log 2>&1',
                        returnStatus: true
                    )

                    if (buildStatus == 0) {
                        echo "Gradle Build Successful."
                    } else {
                        echo "Gradle Build Failed."
                    }
                }
            }
        }

        stage('AI Log Analysis') {
            steps {
                sh 'python3 scripts/analyze_logs.py'
            }
        }

        stage('Mark Build Result') {
            steps {
                script {
                    if (buildStatus != 0) {
                        error("Gradle Build Failed")
                    }
                }
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
