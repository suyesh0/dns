pipeline {
    agent any

    stages {
        stage('Execute Python Script') {
            steps {
                sh 'printing.py' // Replace 'your_script.py' with your script's filename
            }
        }

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
