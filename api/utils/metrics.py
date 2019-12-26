import socket, sys, json
from datetime import datetime

from api.utils.ex_util import ExUtil
from api import log

"""get the loggers"""
m_log = log.get_metrics_logger()
log = log.get_logger()

class Metrics:
    def __init__(self):
        pass
    @staticmethod
    def log(req, resp):
        metric = {}
        log.debug('function involed: metrics Logging, with parameters: param1[{0}]'.format(str(resp)))
        try:
            metric['uri'] = req.relative_uri

            if req.method != "GET":
                metric['req_body'] = req.context['data']
            else:
                metric['query_params'] = json.dumps(req.params.items())
                metric['req_body'] = json.dumps('')

            response_timestamp = datetime.now()
            span = response_timestamp - req.context['request_timestamp']
            metric['resp_body'] = resp.body
            metric['http_status'] = resp.status[:3]
            metric['type'] = 'req'
            metric['http_verb'] = req.method
            metric['client_ip'] = req.remote_addr
            metric['server_hostname'] = socket.gethostname()
            metric['bytes'] = sys.getsizeof(resp.data)
            metric['tookmsec'] = (span.days * 86400000) + (span.seconds * 1000) + (span.microseconds / 1000)
            metric['timeout'] = 'null'
            metric['response_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            m_log.info(metric)
        except:
            ExUtil.print_stack_trace()