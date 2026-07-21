pipeline {
    agent any
    triggers {
        githubPush() 
    }

    environment {
        BASE_URL = 'https://api.escuelajs.co'
        PYTHONUNBUFFERED = '1'
    }

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: [
                'All Tests',
                'All API Tests',
                'All UI Tests',
                'test_category.py',
                'test_e2e.py',
                'test_Locations.py',
                'test_login_DDT.py',
                'test_login.py',
                'test_Product.py',
                'test_users.py',
                'Custom Path'
            ],
            description: 'Select a specific test file or full suite to execute'
        )
        string(
            name: 'CUSTOM_PATH',
            defaultValue: 'Test_Case/',
            description: 'Required ONLY if "Custom Path" is selected above'
        )
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment & Dependencies') {
            steps {
                bat '''
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Test Suite') {
            steps {
                script {
                    def pytestCommand = ""

                    if (env.BUILD_CAUSE == 'SCMTRIGGER' || env.BUILD_CAUSE == 'BRANCHINDEXING') {
                        echo "Automatic GitHub Push Triggered! Running Entire Test Suite..."
                        pytestCommand = "pytest Test_Case/ -v --html=reports/automation_report.html --self-contained-html"
                    } else {
                        echo "Manual Build Selected Option: ${params.TEST_SUITE}"
                        
                        switch(params.TEST_SUITE) {
                            case 'All Tests':
                                pytestCommand = "pytest Test_Case/ -v --html=reports/automation_report.html --self-contained-html"
                                break
                            case 'All API Tests':
                                pytestCommand = "pytest Test_Case/test_api/ -v --html=reports/automation_report.html --self-contained-html"
                                break
                            case 'All UI Tests':
                                pytestCommand = "pytest Test_Case/test_ui/ -v --html=reports/automation_report.html --self-contained-html"
                                break
                            case 'Custom Path':
                                pytestCommand = "pytest ${params.CUSTOM_PATH} -v --html=reports/automation_report.html --self-contained-html"
                                break
                            default:
                                pytestCommand = "pytest Test_Case/test_api/${params.TEST_SUITE} -v --html=reports/automation_report.html --self-contained-html"
                                break
                        }
                    }

                    bat """
                        call .venv\\Scripts\\activate.bat
                        ${pytestCommand}
                    """
                }
            }
        }

        // 
        stage('Run JMeter Performance Tests') {
            steps {
                echo "tarting JMeter Performance Tests..."
                bat '''
                    if not exist "reports\\jmeter_html_report" mkdir reports\\jmeter_html_report
                    jmeter -n -t performance_tests/Platzi_Load_Test.jmx -l reports/jmeter_results.jtl -e -o reports/jmeter_html_report -f
                '''
            }
        }
    }

    post {
        always {
            //Playwright/Pytest HTML Report
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'automation_report.html',
                reportName: 'Playwright Automation Report',
                reportTitles: 'Test Results'
            ])

            // JMeter Performance Dashboard HTML Report
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/jmeter_html_report',
                reportFiles: 'index.html',
                reportName: 'JMeter Performance Report',
                reportTitles: 'Performance Metrics'
            ])
        }
    }
}