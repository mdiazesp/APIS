pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        sh 'docker --version'
        sh 'ls -ltr'
        sh 'docker ps'
      }
    }

    stage('Build') {
      steps {
        sh 'cat version_image | xargs ./Scripts/build.sh'
      }
    }

    stage('Run') {
      steps {
        sh 'cat version_image | xargs bash Scripts/run.sh'
        sh 'docker logs test_api01'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python3 ./Tests/00_test_api.py'
          }
        }

        stage('Logs') {
          steps {
            sleep 10
            sh 'docker logs test_api01'
          }
        }

        stage('TestConversor') {
          steps {
            sh 'python3 ./Tests/01_test_api.py'
          }
        }

      }
    }

    stage('stop') {
      steps {
        sh 'bash Scripts/stop.sh'
      }
    }

    stage('upload_image') {
      steps {
        sh 'cat version_image | xargs bash Scripts/upload.sh'
      }
    }

  }
}