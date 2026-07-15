# 📂 utilities/Custom_logger.py
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists("logs"):
            os.makedirs("logs") 
        
        logging.basicConfig(
            filename="logs/automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )
        
        return logging.getLogger()