import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists("Logs"):
            