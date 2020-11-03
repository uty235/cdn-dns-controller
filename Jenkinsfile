pipeline {
    agent {
        label"build"
    }
    environment {
        repository = "https://github.com/uty235/cdn-dns-controller"
        repositoryCredentials = "mihhail"
        ImageName = "cdn-dns-controller"
    }
    agent any
    options {
        timeout(time: 1, unit:'HOURS')
    }
    stages {
        stage ('git clone') {
            steps {
                sh 'git clone https://github.com/uty235/cdn-dns-controller'
            }
        }
        stage('install dependency') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('test') {
            steps {
                sh 'python3 -m pytest test/'
            }
        }
        stage ('create docker image') {
            steps {
                sh 'docker build -t cdn-dns-controller -f docker/Dockerfile .'
            }
        }
        stage ('run docker') {
            steps {
                sh 'docker run -it -d -p 5000:5000 --rm --name cdn-dns-controller cdn-dns-controller'
            }
        }
        stage ('sanity test') {
            steps {
                sh 'curl localhost:5000/'
            }
        }
        stage ('cleanup') {
            steps {
                sh 'docker rm -f cdn-dns-controller'
            }
        }
    }
}
