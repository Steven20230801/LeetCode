from Tutorial.logger.realizations.abstract import LoggerAbstract
from Tutorial.logger.realizations.stdout import Logger

Logger: LoggerAbstract = Logger()


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


def init_logger(conf: Config, report_name: str) -> None:
    """
    Log initialization for report by config.yml. If graylog conf is not exist - will be print all logs to stdout
    :param conf: consist Config object (parsed config.yml), that provide graylog credentials
    :param report_name: all log messages will be marks this value
    :return: None
    """
    global Logger
    try:
        graylog = conf.get_graylog("main")
        if graylog is None or graylog.host_string == "":
            raise Exception("graylog is not exist in config")

        Logger = GraylogLogger(
            graylog_address="{}:{}".format(graylog.host_string, graylog.port),
            report_name=report_name,
        )
        print("graylog inited: will send logs there")
    except Exception as e:
        log.warning("using Logger, GraylogLogger: {}".format(e))
