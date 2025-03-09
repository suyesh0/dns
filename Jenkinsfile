pipeline {
    agent any

    parameters {
        text(name: 'DOMAINS', description: 'Enter domains, one per line', defaultValue: 'example.com\ntest.org\nsub.domain.net')
        booleanParam(name: 'CHECK_MX', description: 'Check MX records?', defaultValue: true)
        string(name: 'TIMEOUT', description: 'DNS query timeout (seconds)', defaultValue: '5')
    }

    stages {
        stage('DNS Check') {
            steps {
                script {
                    def domains = params.DOMAINS.readLines()
                    for (domain in domains) {
                        domain = domain.trim()
                        if (domain) {
                            sh """
                            #!/bin/bash
                            python dns_checker.py '${domain}' '${params.CHECK_MX}' '${params.TIMEOUT}'
                            """
                        }
                    }
                }
            }
        }
    }
}

