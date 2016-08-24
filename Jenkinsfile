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
            sh "./venv/bin/pip install -r requirements/ci.txt -c requirements/constraints.txt"

        stage 'Test'
            sh """
                . venv/bin/activate
                #TODO remove me - hacking to only one test
                #py.test test
                py.test -q -s test/test_validation.py::ValidationTestCase::test_validate_broken_images_file
            """

        stage 'Create and upload artifact to gemfury on master'
            if (env.BRANCH_NAME.trim() == 'master') {

                println 'Create dist package'
                sh """
                    python setup.py sdist
                """

                println 'Push package to gemfury'
                sh "python setup.py --fullname > commandResult"
                result = readFile('commandResult').trim()
                PKG_PATH = "dist/${result}.tar.gz"
                sh """
                    curl --noproxy push.fury.io -v -F package=@${PKG_PATH} https://push.fury.io/aqy2yywXqKVEs6pjKpea/grabone/
                """
            }
            else {
                println 'Not pushing to gemfury because branch is: '+env.BRANCH_NAME.trim()+' and not master'
            }

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