from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from datetime import datetime

def before_all(context):
    service = Service(executable_path="C:\\Users\\amnaj\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()

def save_screenshot(context, scenario_name):
    folder_name = f"screenshots/{scenario_name.replace(' ', '_')}"
    os.makedirs(folder_name, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(folder_name, f"screenshot_{timestamp}.png")

    context.driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        save_screenshot(context, scenario.name)