#!groovy
pipeline{
	agent any //asigna un node y hace el scm checkout
	stages{
		stage('build'){
			steps{
				println "building"
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

