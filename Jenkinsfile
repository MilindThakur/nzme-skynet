#!groovy

node {

    def err = null
    currentBuild.result = "SUCCESS"


    try {

        stage 'Checkout'
            checkout scm

        stage 'Python Requirements'
            sh """
            if [ ! -d "venv" ]
                then
                    virtualenv --no-site-packages venv
                fi
            """
            sh """
            if [ -f "requirements/preinstall.txt" ]; then
              ./venv/bin/pip install -r requirements/preinstall.txt
            fi
            """
            sh "./venv/bin/pip install -r requirements/test.txt"

        stage 'Test'
            sh """
                . venv/bin/activate
                cd test
                py.test
            """

        stage 'Create dist package'
            sh """
                python setup.py sdist
            """

        stage 'Upload artifact to gemfury'
            sh "python setup.py --fullname > commandResult"
            result = readFile('commandResult').trim()
            PKG_PATH = "dist/${result}.tar.gz"
            sh """
                curl -F package=@${PKG_PATH} https://${gemfury_secret}@push.fury.io/grabone/
            """

        stage 'Finish'

    }
    catch (caughtError) {

        err = caughtError
        currentBuild.result = "FAILURE"

    }
    finally {

        if (err) {
            throw err
        }
    }
}