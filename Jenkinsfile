pipeline {
        agent none
        stages {
          stage("build & SonarQube analysis") {
            agent any
            steps {
              withSonarQubeEnv('SonarQube') {
                sh 'Hello'
              }
            }
          }
          stage("Quality Gate") {
            steps {
              waitForQualityGate abortPipeline: true
            }
          }
        }
      }
