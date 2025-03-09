pipeline {
    agent any

    stages {
        stage('Disk Status') {
            steps {
                script {
                    def diskStatus = sh(script: 'df -h', returnStdout: true).trim()
                    println "Disk Status:\n${diskStatus}"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
