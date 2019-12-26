import json

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

from api import log
from api.errors import RaiseError, OK
from api.utils.ex_util import ExUtil

"""get the logger"""
log = log.get_logger()

class BaseResource(object):
    CUST_VA = {
    'message': 'Welcome To Guide APIs...'
    }

    def to_json(self, body_dict):
        try:
            return json.dumps(body_dict)
        except (ValueError, TypeError):
            ExUtil.print_stack_trace()
            RaiseError.error_application(description='unable to process your request - try again...')
    def on_success(self, res, data=None, error=OK):
        res.status = error.get('status')
        meta = OrderedDict()
        meta['code'] = error.get('code')
        meta['message'] = 'OK'
    
        obj = OrderedDict()
        obj['meta'] = meta
        obj['data'] = data
        res.body = self.to_json(obj)
    def on_get(self, req, resp):
        if req.path == '/':
            self.on_success(resp, self.CUST_VA)
        else:
            RaiseError.error_method_not_supported(allowed_methods='GET',description='for the request path: ' + req.path)
    def on_post(self, req, res):
        RaiseError.error_method_not_supported(allowed_methods='POST', description='for the request path: ' + req.path)
    def on_put(self, req, res):
        RaiseError.error_method_not_supported(allowed_methods='PUT', description='for the request path: ' + req.path)
    def on_delete(self, req, res):
        RaiseError.error_method_not_supported(allowed_methods='DELETE',description='for the request path: ' + req.path)

def max_body(limit):
    """Request max length restriction hook"""
    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            description = ('The size of the request is too large. The body must not exceed ' + str(limit) +' bytes in length.')
            RaiseError.error_request_body_too_large(description=description)
        return hook