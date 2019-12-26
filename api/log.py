import sys
import logging
from logging.handlers import  RotatingFileHandler
from decouple import  config

import os
os.environ['LOG_LEVEL']="DEBUG"
os.environ['ENABLE_METRICS_LOG']="true"
os.environ['APP_LOG_PATH']=r"C:\Users\abhi\api\logs\server.txt"
os.environ['METRICS_LOG_PATH']=r"C:\Users\abhi\api\logs\metrics.txt"
""" log level """
level=config("LOG_LEVEL",default="INFO")
logging.basicConfig(level=level)

""" root logger """
logger=logging.getLogger("API")
logger.propagate=False

""" metrics logger """
metrics_logger=logging.getLogger("METRICS")
metrics_logger.propagate=False

""" log formats INFO,DEGUG,ERROR and metrics  """
INFO_FORMAT='[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s'
DEBUG_FORMAT='[%(asctime)s] [%(threadName)s] [%(levelname)s] [in %(pathname)s :%(lineno)d] %(message)s'
ERROR_FORMAT=INFO_FORMAT
METRICS_FORMAT='%(message)s'

""" formatter and handlers for logger"""
stream_handler=logging.StreamHandler(sys.stdout)
app_file_handler=RotatingFileHandler(config('APP_LOG_PATH',default='apps.log'),maxBytes=10485760, backupCount=20)
app_log_formatter=logging.Formatter(eval(level+'_FORMAT'))

stream_handler.setFormatter(app_log_formatter)
app_file_handler.setFormatter(app_log_formatter)

metrics_file_handler=RotatingFileHandler(config('METRICS_LOG_PATH',default='metrics.log'),maxBytes=10485760, backupCount=20)
metrics_log_formatter=logging.Formatter(METRICS_FORMAT)
metrics_file_handler.setFormatter(metrics_log_formatter)

""" available loggers """
logger.addHandler(stream_handler)
logger.addHandler(app_file_handler)
metrics_logger.addHandler(metrics_file_handler)

def get_logger():
   return logger

def get_metrics_logger():
   return metrics_logger

if __name__ == '__main__':
    logger = get_logger()
    logger.info("hello {} !!".format("world"))
