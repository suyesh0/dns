pipeline {
    agent any

    parameters {
        string(name: 'DOMAINS', defaultValue: 'example.com,test.org,sub.domain.net', description: 'Comma-separated list of domains to check')
    }

    stages {
        stage('DNS Check') {
            steps {
                script {
                    def domains = params.DOMAINS.split(',')
                    for (domain in domains) {
                        domain = domain.trim()
                        echo "Checking DNS for ${domain}"
                        sh """
                        #!/bin/bash
                        dig ${domain} A +short
                        if [ \$? -eq 0 ]; then
                          echo "A record found for ${domain}"
                        else
                          echo "A record not found for ${domain}"
                          exit 1
                        fi
                        """
                    }
                }
            }
        }
    }
}
