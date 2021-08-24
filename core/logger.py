import os, logging


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class Logger:

    @staticmethod
    def get_config():
        return {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': {
                'default': {
                    'format': '%(name)s: [%(asctime)s] %(levelname)s: %(message)s'
                }
            },
            'filters': {
                'infofilter': {
                    '()': InfoFilter,
                }
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'stream': 'ext://flask.logging.wsgi_errors_stream'
                },
                'error_file': {
                    'formatter': 'default',
                    'level': 'WARNING',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': os.path.join(os.environ.get('LOG_DIR', os.path.abspath('./')), 'error.log'),
                    'maxBytes': int(os.environ.get('LOG_HIST_SIZE', 1024 * 5)),
                    'backupCount': int(os.environ.get('LOG_BACKUP_COUNT', 10)),
                    'delay': True,
                },
                'access_file': {
                    'formatter': 'default',
                    'level': 'INFO',
                    'filters': ['infofilter', ],
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'filename': os.path.join(os.environ.get('LOG_DIR', os.path.abspath('./')), 'access.log'),
                    'backupCount': int(os.environ.get('LOG_BACKUP_COUNT', 10)),
                    'delay': True,
                    'utc': True,
                    'when': 'midnight'
                }
            },
            'loggers': {
                'app.error': {
                    'handlers': ['console'] if os.environ.get('DEBUG') else ['error_file'],
                    'level': 'DEBUG',
                    'propagate': False,
                },
                'app.access': {
                    'handlers': ['access_file', 'error_file', 'console'] if os.environ.get('DEBUG') else [
                        'access_file',
                        'error_file'],
                    'level': 'DEBUG',
                    'propagate': False
                }
            },
            'root': {
                'handlers': ['console'] if os.environ.get('DEBUG') else ['access_file', 'error_file'],
                'level': 'ERROR'
            }

        }
