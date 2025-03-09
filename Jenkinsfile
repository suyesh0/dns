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
                            echo "Checking domain: ${domain}"
                            try {
                                sh """
                                #!/bin/bash
                                python dns_checker.py '${domain}' '${params.CHECK_MX}' '${params.TIMEOUT}'
                                exit_code=\$?
                                if [ \$exit_code -ne 0 ]; then
                                    echo "Error: dns_checker.py failed for ${domain} with exit code \$exit_code"
                                    exit 1
                                fi
                                """
                            } catch (Exception e) {
                                error "An error occurred while checking ${domain}: ${e.getMessage()}"
                            }
                        }
                    }
                }
            }
        }
    }
}
