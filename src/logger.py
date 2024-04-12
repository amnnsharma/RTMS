import logging
import os
from datetime import datetime


log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for the logger
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
log_filepath = os.path.join(log_dir, log_filename)
file_handler = logging.FileHandler(log_filepath)
file_handler.setLevel(logging.DEBUG)

# Create a formatter for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Example usage
#logger.debug('This is a debug message')
#logger.info('This is an info message')
#logger.warning('This is a warning message')
#logger.error('This is an error message')
#logger.critical('This is a critical message')
