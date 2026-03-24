pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-cicd-analyzer .'
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                docker pull aquasecurity/trivy:latest

                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                aquasecurity/trivy:latest image ai-cicd-analyzer
                '''
            }
        }
    }
}
