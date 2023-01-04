pipeline {
    agent any
    stages {
        stage("init") {
            steps {
              echo 'initilizing the app..'
            }
        }
        stage("build") {
            steps {
              echo 'building the app..'
              sudo docker-compose -f compose.yaml up
              echo 'build done'
            }
        }
        stage("test") {
            steps {
              echo 'testing the app..'
            }
        }
        stage("deploy") {
            steps {
              echo 'deploying the app..'
            }
        }
    }   
}

