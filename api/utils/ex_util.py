import sys
import traceback

from api import log

"""get the logger"""
log = log.get_logger()

class ExUtil(object):
    @staticmethod
    def print_stack_trace():
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extrack unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        log.info("Exception type : %s " % ex_type.__name__)
        log.info("Exception message : %s" %ex_value)
        log.info("Stack trace : %s" %stack_trace)

    @staticmethod
    def get_ex_message():
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        log.info("Exception type : %s " % ex_type.__name__)
        log.info("Exception message : %s" %ex_value)
        return ex_type.__name__+ '::' + str(ex_value)
