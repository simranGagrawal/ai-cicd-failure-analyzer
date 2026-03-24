pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-cicd-analyzer .'
            }
        }

        stage('Install Trivy') {
            steps {
                sh '''
                curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh './bin/trivy image --exit-code 1 --severity HIGH, CRITICAL ai-cicd-analyzer'
            }
        }
    }
}
