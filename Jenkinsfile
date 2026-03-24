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
                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                aquasec/trivy image ai-cicd-analyzer
                '''
            }
        }
    }
}
