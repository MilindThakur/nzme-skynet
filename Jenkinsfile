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
            PKG_NAME = sh (
                script = 'python setup.py --fullname',
                returnStdout: true
            )
            PKG_PATH = "dist/${PKG_NAME}.tar.gz"
            sh """
                fury push ${PKG_PATH}
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