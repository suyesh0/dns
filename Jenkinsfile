pipeline {
    agent any

    parameters {
        extendedChoice(
            name: 'Domains',
            type: 'PT_MULTI_LINE_TEXT', // Use PT_MULTI_LINE_TEXT for a large text area
            value: '{\n  "domains": [\n    "example.com",\n    "test.org",\n    "sub.domain.net"\n  ],\n  "other_config": "value"\n}',
            description: 'Enter domain data',
        )
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
