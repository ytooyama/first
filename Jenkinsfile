pipeline {
    agent { label 'gpu' }

    stages {
        stage('Hello') {
            steps {
                sh 'python3.9 test.py'
            }
            post {
                success {
                    slackSend(
                    message: "成功",
                    )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "失敗",
                    )
                }
            }
        }
    }
}
