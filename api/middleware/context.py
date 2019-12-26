from datetime import datetime
from api import log
from api.errors import ApplicationError, RaiseError, HTTPBadRequest, HTTPUnauthorized
from api.utils.metrics import Metrics



"""get the logger"""
log = log.get_logger()

class ContextManager(object):
    def __init__(self, classifier):
        """
        db_session: db session object to be shared across requests
        classifier: classifier model to drive the intent mapping
        """
        self._classifier = classifier
    def process_request(self, req, resp):
         """
            Handle pre-processing of the request (before routing)
         """
         if req.path not in('/','/x-tree/F5Monitor.html','/favicon.ico','/favicon.png') and not req.path.startswith(('v1/swagger','/static')):
            try:
                req.context['request_timestamp'] = datetime.now()
                """ set the request context """
                req.context['classifier'] = self._classifier
            except (IndexError, HTTPBadRequest , HTTPUnauthorized) as ex:
                raise ex
    def process_response(self, req, resp, resource=None, req_succeeded=False):
        """
        Handle post-processing of the response (after routing).
        """
        if req.path not in ('/','/x-tree/F5Monitor.html','/favicon.ico','/favicon.png')	and not req.path.startswith(('v1/swagger','/static')):
            try:
                Metrics.log(req, resp)
            except:
                raise ApplicationError(description="Unkown exception in Process response")