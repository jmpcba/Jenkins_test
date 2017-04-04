#!groovy
pipeline{
	agent any //asigna un node y hace el scm checkout
	stages{
		stage('build'){
			steps{
				println "building $params.P1"
				println "running on $env.BUILD_ID"
				println "executig Python"
				sh 
			}		
		}
		
		stage("test"){
			steps{
				println "testing"		
			}

		}
		
		stage("deploy"){
			steps{
				println "deploying"
			}
		}
	}
}

