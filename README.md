#  Playwright Python API & Performance Automation Framework

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-API-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Apache JMeter](https://img.shields.io/badge/Apache%20JMeter-Performance-D22128?style=for-the-badge&logo=apachejmeter&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

A production-ready, modular **REST API Automation & Load Testing Framework** built using **Python, Playwright API Request context, Pytest, Apache JMeter, and Jenkins CI/CD Pipeline**.

---

##  Features & Highlights

- **Modular API Architecture**: Organized endpoint wrappers for clean separation of concerns (`api_endpoints/`).
- **Comprehensive Test Coverage**: **25+ REST API endpoints** validated across Auth, Products, Categories, and Users modules.
- **End-to-End (E2E) Workflows**: Multi-step business scenarios (e.g., Login ➔ Create Category ➔ Create Product ➔ Fetch Product) implemented in `test_e2e.py`.
- **Data-Driven Testing (DDT)**: Parametrized test execution using external JSON data files (`login_data.json`) and Pytest fixtures.
- **Performance & Load Testing**: Integrated **Apache JMeter** (`.jmx`) test suite to evaluate API response latency, throughput, and error rates under load.
- **Continuous Integration (CI/CD)**: Fully automated pipeline via **Jenkinsfile** with automated execution on GitHub push triggers.
- **Rich Dashboard Reporting**: Automated generation of interactive **Playwright HTML Reports** and **JMeter Performance Dashboard Reports**.

---

## Repository Structure

```text
playwright-python-api-framework/
├── api_endpoints/          # Reusable API Client Modules
│   ├── Auth_Client.py
│   ├── Auth_Login.py
│   ├── Locations_api.py
│   └── Product_api.py
├── performance_tests/      # JMeter Performance / Load Test Scripts
│   └── Platzi_Load_Test.jmx
├── Test_Case/              # Automated Test Suites
│   └── test_api/
│       ├── test_category.py
│       ├── test_e2e.py
│       ├── test_Locations.py
│       ├── test_login_DDT.py
│       ├── test_login.py
│       ├── test_Product.py
│       └── test_users.py
├── Test_data/              # External JSON Data for DDT
│   └── login_data.json
├── utilities/              # Helpers & Custom Configurations
├── reports/                # Generated HTML Automation & JMeter Reports
├── Jenkinsfile             # CI/CD Pipeline Configuration
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/bimalesh07/playwright-python-api-framework.git
cd playwright-python-api-framework
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

---

## Test Execution

### 1. Running API Automation Suite (Pytest + Playwright)

Run all API test cases with self-contained HTML report:
```bash
pytest Test_Case/ -v --html=reports/automation_report.html --self-contained-html
```

Run specific test modules:
```bash
pytest Test_Case/test_api/test_e2e.py -v
pytest Test_Case/test_api/test_login_DDT.py -v
```

### 2. Running JMeter Performance Tests (Terminal / Non-GUI Mode)

Execute JMeter performance suite and generate dashboard report:
```bash
jmeter -n -t performance_tests/Platzi_Load_Test.jmx -l reports/jmeter_results.jtl -e -o reports/jmeter_html_report -f
```

---

##  CI/CD Jenkins Pipeline

The project includes a parameterised `Jenkinsfile` supporting both manual parameter selection and automatic GitHub push triggers:

1. **SCM Trigger**: Runs complete Pytest regression and JMeter load suite automatically on every `git push`.
2. **Build Parameters**: Allows selecting specific test modules (`test_category.py`, `test_Product.py`, etc.).
3. **Artifact Publishing**: Automatically publishes **Playwright HTML Report** and **JMeter Interactive Performance Dashboard** after build completion.

---

## Sample Reports

- **Pytest HTML Report**: Available at `reports/automation_report.html`
- **JMeter Performance Dashboard**: Open `reports/jmeter_html_report/index.html` in any browser to view:
  - Request Latency & Response Times (Min, Max, Avg, 90th/95th Percentile)
  - Throughput (Transactions Per Second)
  - Error % and APDEX Score

---

## Author

- **Bimalesh Kumar** - [GitHub Profile](https://github.com/bimalesh07)
