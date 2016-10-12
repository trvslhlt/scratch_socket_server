

class HTTPRequest(object):
    '''
    request object from byte string
    '''
    method = None
    headers = {}
    body = None
    

    def __init__(self, raw_request):
        '''
        gleans request information from the request's bytes
        '''
        request = get_request_from_raw(raw_request)
        self.method = get_method_from_request(request)

    
def get_request_from_raw(raw_request):
    '''
    takes in a raw request and returns a string
    '''
    return raw_request.decode('utf-8')


def get_method_from_request(request):
    request_line = request.split('\n')[0]
    method = request_line.split(' ')[0]
    return method

