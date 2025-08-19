import logging
from datetime import datetime

def setup_logger(name):
    """Set up a logger with timestamp formatting"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def log_user_action(username, action):
    """Log user actions for audit trail"""
    logger = setup_logger("user_actions")
    logger.info(f"User {username} performed action: {action}")