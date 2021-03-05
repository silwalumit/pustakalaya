from logging import Formatter, getLogger, FileHandler, DEBUG

from flask import has_request_context, request


class RequestFormatter(Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


logger = getLogger(__name__)
logger.setLevel(DEBUG)

file_handler = FileHandler('monitorapp.log')
formatter = RequestFormatter('[%(asctime)s]:%(remote_addr)s requested %(url)s: %(levelname)s:%(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
