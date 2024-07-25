from utils.logger import setup_logger
import os

logger = setup_logger()

def before_all(context):
    logger.info("Starting test run")

    if not os.path.exists('reports'):
        os.makedirs('reports')

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
    logger.info("Test run complete")

