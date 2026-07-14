import pytest
import os
from pathlib import Path
from utilities.read_env import ReadEnv
from utilities.Custom_logger import LogGen

logger = LogGen.loggen()


def pytest_configure(config):
    logger.info("******** Bootstrapping Framework Engine Configuration ********")
    
    # Metadata setup for global HTML reports
    config._metadata['Project Name'] = 'Platzi E-Commerce Automation Suite'
    config._metadata['Framework Type'] = 'Hybrid Hybrid Automation Engine (API + UI Ready)'
    config._metadata['Execution Engine'] = 'Playwright Engine'

@pytest.fixture(scope="session")
def base_url():
    url = ReadEnv.get_base_url()
    if not url:
        logger.error("BASE_URL is not defined in the environment variables.")
        raise ValueError("BASE_URL environment variable is missing!")
    logger.info(f"Target Automation Endpoint verified dynamically: {url}")
    return url

#HTML REPORT FORMATTING HOOKS
def pytest_html_report_title(report):
    """Dynamically updates the browser tab/page title for the automation execution report."""
    report.title = "Platzi Enterprise Test Suite Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """Injects custom environment details into the top banner of the execution summary report."""
    from py.xml import html
    prefix.extend([html.h3(f"Execution Context: {ReadEnv.get_base_url()}")])

# 🛠️ FUTURE-PROOF UI HOOK: Screen capture integration scaffold
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Global test observer hook. It tracks execution status.
    In the future, when UI is integrated, this automatically catches failures and attaches screenshots to HTML report.
    """
    outcome = yield
    report = outcome.get_result()
    
    # UI Automation hook handler placeholder:
    if report.when == "call" and report.failed:
        logger.warning(f"Execution Failure detected on: {item.nodeid}")
        
        # Checking if 'page' fixture exists (indicates a UI test context failure)
        if "page" in item.fixturenames:
            page = item.funcargs.get("page")
            if page:
                # Dynamically path creation for screenshots directory
                screenshot_dir = Path("reports/screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                screenshot_path = screenshot_dir / f"{item.name}.png"
                
                # Take screenshot sync
                page.screenshot(path=str(screenshot_path))
                logger.info(f"Captured failure screenshot saved at: {screenshot_path}")
                
                # Hook script code to attach screenshot inside html report directly
                html_element = f'<div><img src="screenshots/{item.name}.png" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                extra = getattr(report, "extra", [])
                extra.append(item.config.pluginmanager.getplugin("html").extras.html(html_element))
                report.extra = extra