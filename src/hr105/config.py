

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        "time_simple": {
            'format': '%(asctime)s, %(message)s'
        },
        "api_response": {
            'format': '%(message)s'
        },
        'standard': {
            # 'format': '[%(levelname)s] %(name)s: %(message)s'
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
            "stream": "ext://sys.stdout"
        },
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "hr105.log",
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 5,
            "level": "DEBUG"
        },
    },
    "root": {
        "handlers": ["console"],
    },
    "loggers": {
        "hr105.cli": {
            "handlers": ["console", "default"],
            "level": "DEBUG",
            "propagate": False
        },
        "hr105": {
            "handlers": ["console", "default"],
            "level": "DEBUG",
            "propagate": False
        },
        "tests": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}