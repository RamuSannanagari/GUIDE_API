import socket
from falcon import MEDIA_TEXT

from api.errors import ERR_UNKNOWN, OK
from .base import BaseResource
from api import log

"""get the logger"""
log = log.get_logger()

class HealthCheckResource(BaseResource):
    """health check ping to the application"""
    def on_get(self, req, resp):
        """
        This function to do application health check
        """
        resp._set_media_type(MEDIA_TEXT)

        try:
            resp.status = OK.get('status')
            host_name = socket.gethostname()
            resp.body = '<html><body>THE SERVER IS UP <p/> Host:' + host_name + '</body></html>'
        except excception:
            log.error('Exception while doing HealthCheck')
            resp.status = ERR_UNKNOWN.get('status')
            resp.body = '<html><body>THE SERVER IS DOWN</body></html>'