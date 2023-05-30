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
                    message: "https://github.com/ytooyama/first テスト成功",
                    )
                }
                failure {
                    slackSend(
                    color: "#FF0000",
                    message: "https://github.com/ytooyama/first テスト失敗",
                    )
                }
            }
        }
    }
}
