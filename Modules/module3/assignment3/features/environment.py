import configparser
from selenium import webdriver

def before_all(context):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    env = config.get('DEFAULT', 'environment')
    context.base_url = config.get(env, 'base_url')
    context.browser_type = config.get(env, 'browser')

def before_scenario(context, scenario):
    if context.browser_type == 'chrome':
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()