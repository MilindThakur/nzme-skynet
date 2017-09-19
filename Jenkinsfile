#!groovy

@Library('NZMEJenkinsLibs')
import tests.python.Test
import build.package_indexes.python.Build

node {
    stage('Preparing workspace'){
        // checkout the project into workspace
        checkout scm

    // prepare the virtualenv
    if (!fileExists('.env')){
        sh "virtualenv --no-site-packages .env"
        }
    sh """
    . .env/bin/activate
    pip install -r requirements/ci.txt
    """
    }

    stage('Running tests'){
        def test = new Test()
        test.tox()
    }

    stage('Building and Deploying'){
        def build = new Build()
        build.deploy('master', 'jfrog-nzme-testing')
    }
}
