#!groovy

@Library('NZMEJenkinsLibs')
import tests.python.Test
import build.package_indexes.python.Build

node {
    stage('Preparing workspace'){
        // checkout the project into workspace
        checkout scm
    }

    stage('Running tests'){
        def test = new Test()
        test.tox()
    }

    stage('Building and Deploying'){
        def build = new Build()
        build.deploy()
    }
}
