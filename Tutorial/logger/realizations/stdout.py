from datetime import date, datetime
from logging import Handler, LoggerAdapter
import logging
import os
from Tutorial.logger.realizations.abstract import LoggerAbstract


class StdoutLogger(LoggerAbstract):
    """
    Default logger initialization, which pass log message to stdout with levels name in message
    """

    def __init__(self, report_name: str = ""):
        self.project_name = report_name if report_name != "" else "Logger"
        self.log_folder = "logs"
        self.logger = self.set_logger(report_name)

    def info(self, message: str = "") -> None:
        """
        Writes log as message with INFO level
        :param message: provides log message
        :return: None
        """
        self.logger.info(
            "{}| {} info: {}".format(datetime.now(), self.project_name, message)
        )

    def debug(self, message: str = "") -> None:
        """
        Writes log as message with DEBUG level
        :param message: provides log message
        :return: None
        """
        self.logger.debug(
            "{}| {} debug: {}".format(datetime.now(), self.project_name, message)
        )

    def error(self, message: str = "") -> None:
        """
        Writes log as message with ERROR level
        :param message: provides log message
        :return: None
        """
        self.logger.error(
            "{}| {} error: {}".format(datetime.now(), self.project_name, message)
        )

    def warning(self, message: str = "") -> None:
        """
        Writes log as message with WARNING level
        :param message: provides log message
        :return: None
        """
        self.logger.warning(
            "{}| {} warning: {}".format(datetime.now(), self.project_name, message)
        )

    def set_logger(self, project_name) -> LoggerAdapter:
        """
        Initialization graylog with necessary loggers structure
        :return: LoggerAdapter - logger object, which provides access to graylog
        """

        project_name = project_name if project_name else self.project_name

        my_logger = logging.getLogger(project_name)
        my_logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(funcName)s :%(message)s")
        # 創立logs資料夾
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)
        # 創立logs/project_name資料夾
        if not os.path.exists(os.path.join(self.log_folder, project_name)):
            os.makedirs(os.path.join(self.log_folder, project_name))
        # 創立logs/project_name/日期.log
        file_name = os.path.join(self.log_folder, project_name, f"{date.today()}.log")

        # Handler.setFormatter(formatter)

        # Create console handler and set level to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        my_logger.addHandler(ch)

        # Create file handler and set level to INFO
        fh = logging.FileHandler(file_name)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        my_logger.addHandler(fh)

        self.logger = LoggerAdapter(my_logger, {"project_name": project_name})
