from falcon import MEDIA_TEXT
import json

from api.errors import  RaiseError, HTTPBadRequest
from api.utils.ex_util import ExUtil



class Serializer(object):
    def process_request (self, req, resp):
        """ enfornce the request method and media type"""
        if req.method in ('POST','PUT'):
            print(req.content_type)
            print('------------')
            if 'application/json' in req.content_type:
                try:
                    print("inside ")
                    raw_json = req.stream.read()
                    if not raw_json:
                        RaiseError.error_invalid_parameter(description = 'empty request body - need a valid JSON.')
                    """ set the data in the context after decoding"""
                    req.context['data'] = json.loads(raw_json)
                except HTTPBadRequest:
                    raise
                except(UnicodeDecodeError, TypeError):
                    ExUtil.print_stack_trace()
                    RaiseError.error_invalid_parameter(description='unable to process your request - malformed payload...')
            else:
                RaiseError.error_missing_header(description = 'supports requests encoded in JSON in JSON only')


        """enforce the media support types"""
        if req.path not in('/','/x-tree/F5Monitor.html','/favicon.ico','/favicon.png')	and not req.path.startswith(('v1/swagger','/static')):
            if not req.client_accepts_json:
                RaiseError.error_not_acceptable(description='support response encoded in JSON only' + MEDIA_TEXT)



