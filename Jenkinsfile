node {
    stage('Clone repo') {
        git branch: 'main', credentialsId: 'realsnack-git', url: 'https://github.com/Realsnack/python-rest-api.git'
    }

    stage('Build docker image') {
        sh 'docker build -t 192.168.1.27:49153/python-restapi:latest .'
    }

    stage('Build docker image') {
        sh 'docker push 192.168.1.27:49153/python-restapi:latest'
    }

    stage('Remove old container') {
        sh 'docker stop python-rest_api && docker rm python-rest_api || true'
    }

    stage('Run docker image') {
        sh 'docker run -d --name python-rest_api -p 5050:5050 192.168.1.27:49153/python-restapi:latest'
    }
}