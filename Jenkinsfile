pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/akula-ujwal/jenkins-pipeline-project.git', branch: 'master'
            }
        }

        stage('Env Setup and Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    . myvenv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Check FastAPI App') {
            steps {
                sh '''
                    . myvenv/bin/activate
                    python -c "from main import app; print('FastAPI app loaded successfully')"
                '''
            }
        }
    }
}

