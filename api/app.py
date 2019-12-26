import sys,os
import  falcon
from decouple import config
from numpy.core import multiarray
from falcon_swagger_ui import register_swaggerui_app

from api import log
from api.middleware import ContextManager,Serializer
from api.resources.mapping import base,utterance,healthcheck
from api.resources.classifier import FidBobClassifier
from api.utils.ex_util import ExUtil

""" get the logger """
log=log.get_logger()

class Application(falcon.API):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        log.info("API Server Coming Up...")

        """ resource mapping """
        self.add_route("/",base.BaseResource())
        self.add_route("/v1/utterance",utterance.UtteranceResource())
        self.add_route("/x-tree/F5Monitor.html",healthcheck.HealthCheckResource())
def create_app(Serializer,ContextManger):
        """ configure the application and middleware """
        middleware=[Serializer,ContextManger]
        application=Application(middleware=middleware)
        SWAGGERUI_URL = '/swagger'

        import pathlib
        SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'
        #SCHEMA_URL="/static/v1/datasource.json"
        #STATIC_PATH=pathlib.path(__file__).parent/'static'
        #application.add_static_route('/static',str(STATIC_PATH))
        pt="Falcon Swagger Doc"
        f_url="https://falconframework.org/favicon-32X32.png"
        conf={'supportedSubmitMethods':['get'],}
        register_swaggerui_app(app=application,swagger_uri=SWAGGERUI_URL,api_url=SCHEMA_URL,config=conf)
        log.info("API Server Ready To Serve Requests")
        return application

def get_app():
        try:
            classifier=FidBobClassifier()
        except:
            ExUtil.print_stack_trace()

        """ init the classifier """
        serializer=Serializer()
        context_manager=ContextManager(classifier)

        if not context_manager:
            print("context config params are not initialized")
            sys.exit(1)

        return create_app(serializer,context_manager)
application=get_app()
""" main method"""
if __name__ == '__main__':
        from wsgiref import simple_server
        httpd=simple_server.make_server("localhost",8080,get_app())
        httpd.serve_forvever()
