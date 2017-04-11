pipeline {
  agent {
    node {
      label 'master'
    }
    
  }
  stages {
    stage('build') {
      steps {
        echo 'Starting build step'
        node(label: 'master') {
          pwd()
          git(url: 'https://github.com/jmpcba/Jenkins_test.git', branch: '*/master')
        }
        
        sh 'python run.py'
        archiveArtifacts(artifacts: 'artefacto.py', onlyIfSuccessful: true)
      }
    }
  }
}