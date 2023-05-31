pipeline {
    agent { label 'gpu' }

    stages {
        stage('Tested with python 3.8') {
            steps {
                sh 'python3.8 test.py'
            }
            post {
                success {
                    slackSend(
                    message: "py38testは成功 ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)",
                )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "py38testは失敗 ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)",
                )
                }
            }            
            
        }
        stage('Tested with python 3.9') {
            steps {
                sh 'python3.9 test.py'
            } 
            post {
                success {
                    slackSend(
                    message: "py39testは成功 ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)",
                )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "py39testは失敗 ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)",
                )
                }
            }
        }
    }
}
