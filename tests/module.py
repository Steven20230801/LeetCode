from Tutorial.logger.logger_interface import log, log_exception


@log_exception
def sum11(a, b):
    return a + b
