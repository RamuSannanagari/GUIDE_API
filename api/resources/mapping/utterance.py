from cerberus import Validator, DocumentError
from .base import BaseResource, max_body
from api.errors import RaiseError
from api.utils.ex_util import ExUtil
from api import log
from guide.api.etl.datasourceConnection import DataSource
"""get the logger"""
log = log.get_logger()
from collections import OrderedDict
"""fields restrictions"""
FIELDS = {
            'question': {
            'type': 'string',
            'required': True,
            'minlength': 2,
            'maxlength': 200
        }}

def validate_expression(req, resp, resource, params):
    schema = {
                'question': FIELDS['question']
            }

    """validate the request payload"""
    v = Validator(schema)

    try:
        if not v.validate(req.context['data']):
            RaiseError.error_invalid_parameter(description="invalid payload")
        max_body(6 * 1024)
    except DocumentError:
        description = "invalid expression {}".format(req.context['data'])
        RaiseError.error_invalid_parameter(description=description)

class UtteranceResource(BaseResource):
    #@falcon.before(validate_expression)
    def on_post(self, req, resp):
        """process the utterance using POST method"""
        req_data = req.context['data']
        classifier = req.context['classifier']
        if not req_data:
            raise RaiseError.error_invalid_parameter(description=req.context['data'])
        try:
            if classifier:
                #model,confidence_score = classifier.predict(req_data.get('question'))
                filename=req_data.get('filename')
                filetype=req_data.get('filetype')
                etl_obj=DataSource(filename,filetype)
                sheet_names=etl_obj.getMetaData()['sheet_names']
                l_msg = "output returned by the Model: {}".format(sheet_names)
                log.info(l_msg)

                bdata = OrderedDict()
                bdata['sheet_names']=sheet_names
            else:
                log.error("classifier is not configured...")
        except:
            ExUtil.print_stack_trace()
            RaiseError.error_not_found(description='No Utterance Mapping found')
        self.on_success(resp, bdata)