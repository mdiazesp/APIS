pipeline {
  agent any
  stages {
    stage('env') {
      steps {
        sh 'docker --version'
      }
    }

    stage('build') {
      steps {
        sh 'cat version_image | xargs ./Scripts/build.sh'
      }
    }

    stage('run') {
      steps {
        sh 'cat version_image | xargs bash Scripts/run.sh'
        sh 'docker logs test_api01'
      }
    }

    stage('test') {
      parallel {
        stage('test') {
          steps {
            sh 'python3 ./Tests/00_test_api.py'
          }
        }

        stage('test1') {
          steps {
            sh 'python3 ./Tests/01_test_api.py'
          }
        }

        stage('test3') {
          steps {
            sh 'python3 ./Tests/03_test_api.py'
          }
        }

      }
    }

  }
}