pipeline {
        agent none
        stages {
          stage("SonarQube analysis") {
            //agent any
                  def scannerhome = tool 'SonarQubeScanner 2.8
            //steps {
              withSonarQubeEnv('SonarQube') {
              //  echo 'Hello'
                      sh '${scannerHome}/bin/sonar-scanner'
              }
            }
          }
        //  stage("Quality Gate") {
          //  steps {
            //  waitForQualityGate abortPipeline: true
        //    }
        //  }
      //  }
      }
