import pytest
from utilities.Custom_logger import LogGen

logger = LogGen.loggen()

def pytest_html_report_title(report):
    report.title = "Platzi Enterprise Test Suite Report"

def pytest_configure(config):
    logger.info("******** AUTOMATION PIPELINE INITIALIZED ********")

def pytest_metadata(metadata):
    metadata['Project Name'] = 'Platzi E-Commerce Automation'
    metadata['Framework Type'] = 'Hybrid Automation Platform'
    metadata['Execution Engine'] = 'Playwright Engine'