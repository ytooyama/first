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
                    message: "https://github.com/ytooyama/first py38テスト成功",
                )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "https://github.com/ytooyama/first py38テスト失敗",
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
                    message: "https://github.com/ytooyama/first py39テスト成功",
                )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "https://github.com/ytooyama/first py39テスト失敗",
                )
                }
            }
        }
    }
}
