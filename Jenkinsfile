pipeline {
    agent any

    stages {
        stage('Execute Python Script') {
            steps {
                sh 'chmod +x printing.py' // Add execute permissions
                sh 'python3 printing.py' // Execute with python3
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
