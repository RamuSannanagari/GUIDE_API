from falcon.errors import HTTPInternalServerError
from falcon.errors import HTTPUnauthorized
from falcon.errors import HTTPUnsupportedMediaType
from falcon.errors import HTTPPayloadTooLarge
from falcon.errors import HTTPMethodNotAllowed
from falcon.errors import HTTPNotAcceptable
from falcon.errors import HTTPNotFound
from falcon.errors import HTTPBadRequest
from falcon.errors import HTTPError
from falcon import status_codes

OK = {
     'status' : status_codes.HTTP_OK,
     'code' : 200,
}

ERR_UNKNOWN = {
    'status' : status_codes.HTTP_INTERNAL_SERVER_ERROR,
    'code' : 5000,
    'title' : 'Unknown Error'
}

ERR_AUTH_REQUIRED = {
    'status' : status_codes.HTTP_UNAUTHORIZED,
    'code' : 4010,
    'title' : 'Authentication Required'
}


ERR_INVALID_PARAMETER = {
    'status' : status_codes.HTTP_BAD_REQUEST,
    'code' : 4010,
    'title' : 'Invalid body or Parameter(s)'
}

ERR_NOT_SUPPORTED = {
    'status' : status_codes.HTTP_METHOD_NOT_ALLOWED,
    'code' : 1000,
    'title' : 'Not Supported'
} 

ERR_NOT_ACCEPTABLE = {
    'status' : status_codes.HTTP_NOT_ACCEPTABLE,
    'code' : 4060,
    'title' : 'Not Accepatble'
} 

ERR_REQUEST_BODY_TOO_LARGE = {
    'status' : status_codes.HTTP_REQUEST_ENTITY_TOO_LARGE,
    'code' : 4130,
    'title' : 'request body too large'
} 
ERR_UNSUPPORTED_MEDIA_TYPE = {
    'status' : status_codes.HTTP_UNSUPPORTED_MEDIA_TYPE,
    'code' : 4150,
    'title' : 'Un Supported Media Type'
}
ERR_RESOURCE_TIMEOUT = {
    'status' : status_codes.HTTP_REQUEST_TIMEOUT,
    'code' : 4080,
    'title' : 'One or More Resource Timed Out'
}
ERR_INVALID_HEADER = {
    'status' : status_codes.HTTP_BAD_REQUEST,
    'code' : 4000,
    'title' : 'Invalid Header Param or Value'
}
ERR_MISSING_HEADER = {
    'status' : status_codes.HTTP_BAD_REQUEST,
    'code' : 4000,
    'title' : 'Missing Header Param (s)'
}

class ApplicationError (HTTPError):
    __slots__ = ()
    """generic application error returned as HTTP 500"""

    def __init__ (self, error = ERR_UNKNOWN, description = None):
        super(ApplicationError, self).__init__(error.get('status'),error.get('title'), description,code = error.get('code'))

class ResourceTimeOutError(ApplicationError):
    """when any resource request timeout"""
    def __init__(self, error = ERR_RESOURCE_TIMEOUT, description = None):
        super(ApplicationError, self).__init__(error, description)

class RaiseError:
    """utility class to generate errors from within the applicaation"""	

    def __init__(self):
       pass
    @staticmethod
    def error_unknown(error = ERR_UNKNOWN , description=None):
        raise HTTPInternalServerError(error.get('title'),description , code = error.get('code'))
    @staticmethod
    def error_auth_reuired(error = ERR_AUTH_REQUIRED , description=None):
        raise HTTPUnauthorized(error.get('title'),description , code = error.get('code'))
    @staticmethod
    def error_invalid_parameter(error = ERR_INVALID_PARAMETER , description=None):
        raise HTTPBadRequest(error.get('title'),description , code = error.get('code'))
    @staticmethod
    def error_resource_timeout( description=None):
        raise ResourceTimeOutError(description = description)
    @staticmethod
    def error_method_not_supported(allowed_methods, error = ERR_NOT_SUPPORTED , description=None):
        raise HTTPNotFound(allowed_methods,title=error.get('title'),description = description , code = error.get('code'))
    @staticmethod
    def error_invalid_header( error = ERR_INVALID_HEADER , description=None):
        raise HTTPBadRequest(title=error.get('title'),description = description , code = error.get('code'))
    @staticmethod
    def error_missing_header( error = ERR_MISSING_HEADER , description=None):
        raise HTTPUnsupportedMediaType(description = description , code = error.get('code'))
    @staticmethod
    def error_not_acceptable(error = ERR_NOT_ACCEPTABLE , description=None):
        raise HTTPNotAcceptable(description , code = error.get('code'))
    @staticmethod
    def error_request_body_too_large( error = ERR_REQUEST_BODY_TOO_LARGE , description=None):
        raise HTTPPayloadTooLarge(error.get('title'),description , code = error.get('code'))
    @staticmethod
    def error_application( description=None):
        raise ApplicationError(description = description)

"""main function"""
if __name__=='__main__':
    try:
        RaiseError.error_auth_reuired(description='Test error...')
    except (ApplicationError, ResourceTimeOutError,HTTPInternalServerError,HTTPNotFound,HTTPBadRequest,HTTPUnauthorized) as ex:
        print(ex.to_json())