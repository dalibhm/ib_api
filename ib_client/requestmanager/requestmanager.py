

class RequestManager:
    def __init__(self):
        self.requests = {}

    def register_request(self, request_id, request):
        self.requests[request_id] = request

    def get_request_by_id(self, request_id):
        return self.requests.get_request(request_id)
