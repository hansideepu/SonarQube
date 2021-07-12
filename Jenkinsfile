pipeline {
        agent none
        stages {
          stage("SonarQube analysis") {
            //agent any
                steps{
                  def scannerhome = tool 'SonarQubeScanner 2.8';
                   withSonarQubeEnv('SonarQube') {
                   sh '${scannerHome}/bin/sonar-scanner'
              }
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
