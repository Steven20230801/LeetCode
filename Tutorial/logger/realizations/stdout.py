from datetime import datetime
from logging import Handler, LoggerAdapter
import logging
from Tutorial.logger.realizations.abstract import LoggerAbstract


class Logger(LoggerAbstract):
    """
    Default logger initialization, which pass log message to stdout with levels name in message
    """

    def __init__(self, report_name: str = ""):
        self.project_name = report_name if report_name != "" else "Logger"
        self.log_folder = "logs"

    def info(self, message: str = "") -> None:
        """
        Writes log as message with INFO level
        :param message: provides log message
        :return: None
        """
        print("{}| {} info: {}".format(datetime.now(), self.project_name, message))

    def debug(self, message: str = "") -> None:
        """
        Writes log as message with DEBUG level
        :param message: provides log message
        :return: None
        """
        print("{}| {} debug: {}".format(datetime.now(), self.project_name, message))

    def error(self, message: str = "") -> None:
        """
        Writes log as message with ERROR level
        :param message: provides log message
        :return: None
        """
        print("{}| {} error: {}".format(datetime.now(), self.project_name, message))

    def warning(self, message: str = "") -> None:
        """
        Writes log as message with WARNING level
        :param message: provides log message
        :return: None
        """
        print("{}| {} warning: {}".format(datetime.now(), self.project_name, message))

    def set_logger(self) -> LoggerAdapter:
        """
        Initialization graylog with necessary loggers structure
        :return: LoggerAdapter - logger object, which provides access to graylog
        """

        my_logger = logging.getLogger(self.report_name)
        my_logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(filename)s - %(name)s - %(funcName)s - %(asctime)s - %(levelname)s :%(message)s"
        )  # setting log format
        file_name = os.path.join(
            log_folder, f"{date.today()}.log"
        )  # write data to x.log
        Handler.setFormatter(formatter)
        my_logger.addHandler(handler)

        service_adapter = logging.LoggerAdapter(
            my_logger, {"report_name": self.report_name}
        )

        return service_adapter
