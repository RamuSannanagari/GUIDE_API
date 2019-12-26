from functools import wraps
from time import time
from api import log

import sys
sys.path.append('C:\\ai-capability\\ap127563-customer-virtual-assistant')

"""get the logger"""
log = log.get_logger()

def stop_watch(target):
    """to capture execution time of a function"""
    @wraps(target)
    def wrap(*args,**kwargs):
        t_start = time()
        result = target(*args, **kwargs)
        t_end = time()
        log.debug('function :{:s} args:[{:s}] took: {:2.3f} sec'.format(target.__name__, str(args), str(kwargs), t_end-t_start))
        return result
    return wrap
def log_entry_exit(target):
    """to entry and exit of a function"""
    @wraps(target)
    def wrap(*args, **kwargs):
        log.debug('function begin :{s} args:[{:s}, {:s}]'.format(target.__name__,str(args), str(kwargs)))
        result = target(*args, **kwargs)
        log.debug('function end :{:s} result:[{:s}]'.format(target.__name__, result))
        return result
    return wrap