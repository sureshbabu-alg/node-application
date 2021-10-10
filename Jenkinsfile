pipeline {
  agent any
  environment {
    region = "us-west-2"
  }
  stages {
    stage("Stage-1") {
      steps {
      sh "echo 'test-1' "
      sh '''
      ls
      pwd
      echo "region name is ${region}"
      '''
    }
    }
    stage("Stage-2") {
      parallel {
        stage("build") {
          steps {
            sh "echo 'this is build stage'"
            sh "echo 'region name is ${region}'"
          }
        }
        stage("deploy") {
          steps {
            sh "echo 'this is deploy stage'"
            sh "echo 'region name is ${region}'"
          }
        }
      }

    }
    stage("Stage-3") {
      steps {
      sh "echo 'test-3' "
      sh "echo 'region name is ${region}'"
    }
    }
  }
}
