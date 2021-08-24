from flask import current_app as app

from app import err_logger
from core.exceptions import ValidationException


@app.errorhandler(ValidationException)
def handle_error(e):
    err_logger.error(F"Validation error {e.message}")
    return e.get_response()
