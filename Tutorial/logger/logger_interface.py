from time import perf_counter
import traceback
from Tutorial.logger.realizations.abstract import LoggerAbstract
from Tutorial.logger.realizations.stdout import StdoutLogger

Logger: LoggerAbstract = StdoutLogger()


class log:
    """
    Logger interface, which makes access to Logger object.
    """

    @staticmethod
    def info(message: str = "") -> None:
        """
        Passes a message to the INFO method of the logger object
        :param message: provides log message
        :return: None
        """
        Logger.info(message)

    @staticmethod
    def debug(message: str = "") -> None:
        """
        Passes a message to the DEBUG method of the logger object
        :param message: provides log message
        :return: None
        """
        Logger.debug(message)

    @staticmethod
    def error(message: str = "") -> None:
        """
        Passes a message to the ERROR method of the logger object
        :param message: provides log message
        :return: None
        """
        Logger.error(message)

    @staticmethod
    def warning(message: str = "") -> None:
        """
        Passes a message to the WARNING method of the logger object
        :param message: provides log message
        :return: None
        """
        Logger.warning(message)


def init_logger(report_name: str) -> None:
    global Logger
    """
    Log initialization for report by config.yml. If graylog conf is not exist - will be print all logs to stdout
    :param conf: consist Config object (parsed config.yml), that provide graylog credentials
    :param report_name: all log messages will be marks this value
    :return: None
    """
    Logger.set_logger(report_name)
    print("Logger inited: will send logs there")


def log_exception(func):
    """
    Decorator provides simple exception handler: logs exception and throws it up
    :param func:
    :return: None or exception
    """

    def inner(*args, **kwargs):
        try:
            start_time = perf_counter()
            res = func(*args, **kwargs)
            end_time = perf_counter()
            run_time = end_time - start_time
            log.info(f"Function {func.__name__} Took {run_time:.4f} seconds")
        except Exception as e:
            log.error(
                "{} {}. \ntraceback: {}".format(
                    func.__name__, e, traceback.format_exc()
                )
            )
            raise e
        return res

    return inner
