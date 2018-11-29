#!/usr/bin/env groovy

@Library('NZMEJenkinsLibs')
import tests.python.Test
import build.package_indexes.python.Build

pipeline {
    agent any
    options {
        // Only keep the last 10
        buildDiscarder (logRotator(numToKeepStr:'10'))
        // And we'd really like to be sure that this build doesn't hang forever, so
        // let's time it out after 15 minutes.
        timeout(time: 15, unit: 'MINUTES')
    }

    stages {

        stage('Checkout') {
            steps {
                // checkout the project into workspace
                checkout scm
            }
        }

        stage('Running tests') {
            steps {
                def test = new Test()
                test.tox()
                sh """
                    python -m coverage xml --include=nzme_skynet*
                """
            }
            post {
                always {
                    cobertura coberturaReportFile: '*/coverage.xml'
                }
            }
        }

        stage('Building and Deploying') {
            steps {
                def build = new Build()
                build.deploy('master', 'jfrog-nzme-testing')
            }
        }
    }

    post {
        always {
            // Success or failure, always send notifications
            notifyBuild(currentBuild.result)
        }
        failure {
            // If there was an exception thrown, the build failed
            currentBuild.result = "FAILED"
            throw e
        }
    }
}

def notifyBuild(String buildStatus = 'STARTED') {
  // build status of null means successful
  buildStatus =  buildStatus ?: 'SUCCESSFUL'

  // Default values
  def colorName = 'RED'
  def colorCode = '#FF0000'
  def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
  def summary = "${subject} (${env.BUILD_URL})"

  // Override default values based on build status
  if (buildStatus == 'STARTED') {
    color = 'YELLOW'
    colorCode = '#FFFF00'
  } else if (buildStatus == 'SUCCESSFUL') {
    color = 'GREEN'
    colorCode = '#00FF00'
  } else {
    color = 'RED'
    colorCode = '#FF0000'
  }

  // Send notifications
  slackSend (color: colorCode, message: summary)
}