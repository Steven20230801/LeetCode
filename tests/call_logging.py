from Tutorial.logger.logger_interface import log, init_logger

# from Tutorial.logger.realizations.stdout import Logger

from tests.module import sum11

if __name__ == "__main__":
    init_logger("test")

    log.info("info")
    sum11(1, 2)
