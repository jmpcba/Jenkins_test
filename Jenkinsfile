#!groovy
pipeline{
	agent any //asigna un node y hace el scm checkout
	checkout scm
	stages{
		stage('build'){
			steps{
				println "building $params.P1"
				println "running on $env.BUILD_ID"
				println "executig Python"
				sh "python run.py"
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
	post{
		println "anduvo como el choto"
	}
}

