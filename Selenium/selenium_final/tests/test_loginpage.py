import pytest
from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.screenshot_util import ScreenshotUtil
# from utils.excel_reader import ExcelReader
from utils.logger import LogGen

logger = LogGen.loggen()

@pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",
    CSVReader.read_csv("login_data.csv")
    # ExcelReader.read_excel("test_data.xlsx", "login_data")
)
def test_login(driver, data):
    login_page = LoginPage(driver)
    logger.info(f"Login page opened")
    logger.info(f"Trying to login with data - {data["username"]}, {data["password"]}")
    login_page.login(data["username"], data["password"])

    logger.info(f"Checking logged in status")
    if data["expected_result"] == "success":
        assert "inventory" in driver.current_url
        logger.info(f"Login Successful - Inventory page opened")
        screenshot_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login-test")
    # else:
    #     assert "inventory" not in driver.current_url
    #     assert login_page.read_error_message().__contains__("Epic sadface: Username and password do not match any user in this service")
    #     logger.error(f"Login Failed - Inventory page NOT opened")
    #     screenshot_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login-test")

    # Fixed by Chetan
    else:
        # Failed login should NOT go to inventory page
        assert "inventory" not in driver.current_url
        logger.error(f"log in failed inventory page not loaded")

        # Read actual error message
        error_message = login_page.read_error_message()

        # Expected failure messages based on type of failure
        expected_errors = [
            "do not match",       # wrong username/password
            "locked out"          # locked out user
        ]

        # Assert that error_message contains at least one expected failure
        assert any(e in error_message for e in expected_errors), f"Unexpected error message: {error_message}"


