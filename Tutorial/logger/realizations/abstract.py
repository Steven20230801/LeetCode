from abc import abstractmethod


class LoggerAbstract:
    """
       Describes general methods for loggers realizations
    """
    @abstractmethod
    def info(self, message: str = '') -> None:
        """
        Writes log as message with INFO level
        :param message: provides log message
        :return: None
        """
        pass

    @abstractmethod
    def debug(self, message: str = '') -> None:
        """
        Writes log as message with DEBUG level
        :param message: provides log message
        :return: None
        """
        pass

    @abstractmethod
    def error(self, message: str = '') -> None:
        """
        Writes log as message with ERROR level
        :param message: provides log message
        :return: None
        """
        pass

    @abstractmethod
    def warning(self, message: str = '') -> None:
        """
        Writes log as message with WARNING level
        :param message: provides log message
        :return: None
        """
        pass
