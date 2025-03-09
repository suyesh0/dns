pipeline {
    agent any

    parameters {
        extendedChoice(
            name: 'DNS_CONFIG',
            type: 'PT_MULTI_LINE_TEXT',
            value: 'domains=example.com,test.org,sub.domain.net\ncheckMX=true\ntimeout=5',
            description: 'Enter DNS configuration (domains, checkMX, timeout)',
            multiSelectDelimiter: ',' // Required, but not used
        )
    }

    stages {
        stage('DNS Check') {
            steps {
                script {
                    def config = [:]
                    params.DNS_CONFIG.readLines().each { line ->
                        def parts = line.split('=')
                        if (parts.size() == 2) {
                            config[parts[0].trim()] = parts[1].trim()
                        }
                    }

                    def domains = config.domains.split(',')
                    def checkMX = config.checkMX.toBoolean()
                    def timeout = config.timeout.toInteger()

                    for (domain in domains) {
                        domain = domain.trim()
                        if (domain) {
                            sh """
                            #!/bin/bash
                            python dns_checker.py '${domain}' '${checkMX}' '${timeout}'
                            """
                        }
                    }
                }
            }
        }
    }
}
