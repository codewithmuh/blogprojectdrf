pipeline {
    agent any
    stages {
        stage('Checkout') {
            
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],
                          userRemoteConfigs: [[url: 'git@github.com:rashiddaha/blogprojectdrf.git']]])
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
    post {
        always {
            slackSend (color: '#36a64f',
                       message: "Build ${currentBuild.number} of ${env.JOB_NAME} succeeded!",
                      )
        }
        unsuccessful {
            slackSend (color: '#ff0000',
                       message: "Build ${currentBuild.number} of ${env.JOB_NAME} failed. Check the Jenkins console output for details.",
                    )
        }
    }
}


// #!groovy

// node {

//     try {
//         stage 'Checkout'
//             checkout scm

//             sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
//             def lastChanges = readFile('GIT_CHANGES')
//             slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"

//         // stage 'Test'

//         //     // sh 'virtualenv env -p python3.10'
//         //     // sh '. env/bin/activate'
//         //     sh '.source env/bin/activate'
//         //     // sh 'env/bin/pip install -r requirements.txt'
//         //     sh 'env/bin/python3.10 manage.py test --testrunner=blog.tests.test_runners.NoDbTestRunner'

//         stage 'Deploy'
//             sh 'sudo ./deployment/deploy_prod.sh'

//         stage 'Publish results'
//             slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
//     }

//     catch (err) {
//         slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

//         throw err
//     }

// }