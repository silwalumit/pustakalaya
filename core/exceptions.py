class ErrorConstants:
    VALIDATION_ERROR = "VALIDATION_ERROR"


class ErrorCodes:
    VALIDATION_ERROR = 100


class CustomException(Exception):
    def __init__(self, code, err_type, message, status=400):
        super(CustomException, self).__init__()
        self.status = status
        self.code = code
        self.type = err_type
        self.message = message

    def __repr__(self):
        return F"<{self.__class__.__name__}({self.type})>"

    def get_response(self):
        response = self.__dict__
        status = response.pop("status")
        return response, status


class ValidationException(CustomException):
    def __init__(self, message="Validation error"):
        code = ErrorCodes.VALIDATION_ERROR
        err_type = ErrorConstants.VALIDATION_ERROR
        super(ValidationException, self).__init__(code, err_type, message)
