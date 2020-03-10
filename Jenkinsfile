pipeline {
    // Which Build Node?
    agent {
        label 'master'
    }
    // Default python project settings (EDITABLE)
    environment {
        VENV_NAME = '_pyLife'
        BATCH_FOLDER = '/batch_script'
    }    
    // Discard the old builds and artifacts
    options {
      buildDiscarder logRotator(
          artifactDaysToKeepStr: '30', 
          artifactNumToKeepStr: '1', 
          daysToKeepStr: '30', 
          numToKeepStr: '10'
        )
    }
    // Build stages
    stages {
        // Create a new Anaconda python virtual environment and set proxy variables
        stage('Prepare Python env') {
            steps {
                bat 'install_pylife.bat'
            }
        }       
    }
}