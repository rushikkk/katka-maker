pipeline {
  agent any
  stages {
    stage('Init') {
      agent any
      steps {
        echo 'Hello!'
        unstable ':('
        validateDeclarativePipeline 'Jenkinsfile'
      }
    }
  }
}