pipeline {
  agent any
  stages {
    stage('SonarQube analysis') {
      tools {
        sonarQube 'SonarQube Scanner 4.6.2.2472'
      }
      steps {
        withSonarQubeEnv('SonarQube') {
          sh 'sonar-scanner'
        }
      }
    }
  }
}
