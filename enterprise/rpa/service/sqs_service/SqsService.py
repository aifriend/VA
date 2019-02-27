from service.sqs_service.ISqsService import ISqsService
from service.util.HttpUtils import https_request
from tools.ACNLogger import ACNLogger


class SqsService(ISqsService):

    def __init__(self):
        ISqsService.__init__(self)
        self.logger = ACNLogger(name="SqsService", file="logs/rpa-sqs-service.log")
        self.req_config = self.req_config.get('RPA')

    def send_sqs_message(self, account_id, queue_name, message, **kwargs):
        # Request
        server = str(self.req_config.get('sqs_server'))
        url = str(self.req_config.get('sqs_url'))
        response = https_request(server, url % (account_id, queue_name, message), "GET", None, {})

        return response
