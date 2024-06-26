import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler


class ACNLogger:

    def debug(self, session, message):
        try:
            self.logger.debug(("[" + session + "]  [" + self._service_name + "]  [DEBUG]  " + message).encode('utf8'))
        except:
            try:
                self.logger.debug("[" + session + "]  [" + self._service_name + "]  [DEBUG]  " + message)
            except:
                self.logger.debug(
                    ("[" + session + "]  [" + self._service_name + "]  [DEBUG]  " + message).decode('utf8'))

    def info(self, session, message):
        try:
            self.logger.info(("[" + session + "]  [" + self._service_name + "]  [INFO]  " + message).encode('utf8'))
        except:
            try:
                self.logger.info("[" + session + "]  [" + self._service_name + "]  [INFO]  " + message)
            except:
                self.logger.info(("[" + session + "]  [" + self._service_name + "]  [INFO]  " + message).decode('utf8'))

    def warning(self, session, message):
        try:
            self.logger.warning(
                ("[" + session + "]  [" + self._service_name + "]  [WARNING]  " + message).encode('utf8'))
        except:
            try:
                self.logger.warning("[" + session + "]  [" + self._service_name + "]  [WARNING]  " + message)
            except:
                self.logger.warning(
                    ("[" + session + "]  [" + self._service_name + "]  [WARNING]  " + message).decode('utf8'))

    def error(self, session, e):
        try:
            self.logger.error(("[" + session + "]  [" + self._service_name + "]  [ERROR]  " + str(
                e.__class__.__name__) + "  " + str(e.message)).encode('utf8'))
        except:
            try:
                self.logger.error("[" + session + "]  [" + self._service_name + "]  [ERROR]  " + str(
                    e.__class__.__name__) + "  " + str(e.message))
            except:
                self.logger.error(("[" + session + "]  [" + self._service_name + "]  [ERROR]  " + str(
                    e.__class__.__name__) + "  " + str(e.message)).decode('utf8'))

    def critical(self, session, e):
        try:
            self.logger.critical(("[" + session + "]  [" + self._service_name + "]  [CRITICAL]  " + str(
                e.__class__.__name__) + "  " + str(e.message)).encode('utf8'))
        except:
            try:
                self.logger.critical("[" + session + "]  [" + self._service_name + "]  [CRITICAL]  " + str(
                    e.__class__.__name__) + "  " + str(e.message))
            except:
                self.logger.critical(("[" + session + "]  [" + self._service_name + "]  [CRITICAL]  " + str(
                    e.__class__.__name__) + "  " + str(e.message)).decode('utf8'))

    def exception(self, message):
        try:
            self.logger.exception("[" + self._service_name + "]  [ERROR]  " + message)
        except:
            self.logger.exception("[" + self._service_name + "]  [ERROR]  Exception")

    def __init__(self, name, file, console_level="debug", logfile_level="debug"):

        offset_s = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone  ###These 3 lines
        offset = offset_s / 60 / 60 * -1  # are to get
        timezone = ["", "+"][offset >= 0] + str(offset).zfill(2) + "00"  # the timezone

        acn_logger = logging.getLogger(name)  # Creating the new logger
        acn_logger.setLevel(logging.DEBUG)  # Setting new logger level to INFO or above
        acn_logger.propagate = False

        console_handler = logging.StreamHandler()

        if console_level == "info":
            console_handler.setLevel(logging.INFO)
        else:
            console_handler.setLevel(logging.DEBUG)

        file_handler = TimedRotatingFileHandler(file, when="W6")
        file_handler.suffix = "%Y%m%d"
        file_handler.extMatch = re.compile(r"^\d{8}$")

        if logfile_level == "info":
            file_handler.setLevel(logging.INFO)
        else:
            file_handler.setLevel(logging.DEBUG)

        acn_logger.addHandler(file_handler)  # Adding file handler to the new logger
        acn_logger.addHandler(console_handler)

        formatter = logging.Formatter('[%(asctime)s' + timezone + ']  %(message)s')  # Creating a formatter

        file_handler.setFormatter(formatter)  # Setting handler format
        console_handler.setFormatter(formatter)

        self.logger = acn_logger
        self._service_name = name
