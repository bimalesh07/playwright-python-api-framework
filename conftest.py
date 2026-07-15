import pytest
from utilities.Custom_logger import LogGen

logger = LogGen.loggen()


def pytest_html_report_title(report)
    report.title = "Platzi Enterprise Test Suite Report"

def pytest_configure(config):
  
    logger.info("********AUTOMATON ********")
    config._metadata['Project Name'] = 'Platzi E-Commerce Automation'
    config._metadata['Framework Type'] = 'Hybrid Automation Platform'
    config._metadata['Execution Engine'] = 'Playwright Engine'