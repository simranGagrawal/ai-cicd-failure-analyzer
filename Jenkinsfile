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
                sh 'trivy image ai-cicd-analyzer .'
            }
        }
    }
}
