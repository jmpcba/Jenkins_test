#!groovy
pipeline{
	agent any //asigna un node y hace el scm checkout
	stages{
		stage('build'){
			steps{
				println "building on $env.BUILD_ID"
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

