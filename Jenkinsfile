pipeline {
    agent any

    parameters {
        extendedChoice(
            name: 'Domains',
            type: 'PT_MULTI_LINE_TEXT',
            value: '{\n  "domains": [\n    "example.com",\n    "test.org",\n    "sub.domain.net"\n  ],\n  "other_config": "value"\n}',
            description: 'Enter domain data',
            multiSelectDelimiter: ','
        )
    }

    stages {
        stage('DNS Check') {
            steps {
                script {
                    def jsonData = readJSON text: params.Domains
                    for (domain in jsonData.domains) {
                        echo "Checking DNS for ${domain}"
                        sh """
                        #!/bin/bash
                        python dns_checker.py ${domain}
                        """
                    }
                    echo "Other Config: ${jsonData.other_config}"
                }
            }
        }
    }
}
