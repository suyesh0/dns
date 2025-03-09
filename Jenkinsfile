pipeline {
    agent any

    parameters {
        text(name: 'DOMAINS', description: 'Enter domains, one per line.\nExample values:\nexample.com\ntest.org\nsub.domain.net', defaultValue: '')
    }

    stages {
        stage('DNS Check') {
            steps {
                script {
                    def domains = params.DOMAINS.readLines()
                    for (domain in domains) {
                        domain = domain.trim()
                        if (domain) {
                            echo "Checking DNS for ${domain}"
                            sh """
                            #!/bin/bash
                            host ${domain}
                            if [ \$? -eq 0 ]; then
                              echo "DNS lookup successful for ${domain}"
                            else
                              echo "DNS lookup failed for ${domain}"
                              exit 1
                            fi
                            """
                        }
                    }
                }
            }
        }
    }
}
