from flask import current_app as app

from core.exceptions import ValidationException
from core.logger import logger


@app.errorhandler(ValidationException)
def handle_error(e):
    logger.error(F"Validation error {e.message}")
    return e.get_response()
