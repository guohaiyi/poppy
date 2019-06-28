import logging
import os
import time
from datetime import datetime

logger = logging.getLogger(__name__)


def create_file(file_name):
    path = file_name[:-7]
    if not os.path.isdir(path):
        os.makedirs(path)

    if not os.path.isfile(file_name):
        fb = open(file_name, mode='w', encoding='utf-8')
        fb.close()
    else:
        # print("不需要创建")
        pass


def set_handler(level):
    if level == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)
    logger.addHandler(MyLog.console)


def remove_handler(level):
    if level == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)
    logger.removeHandler(MyLog.console)


def set_now_time():
    now_time = time.strftime(MyLog.time_format, time.localtime(time.time()))
    return now_time


class MyLog:
    # 基本设置
    base_path = "../Log/"
    path = os.path.join(base_path, str(datetime.now().strftime("%Y%m%d")))
    log_file = path + "/log.log"
    err_file = path + "/err.log"
    create_file(log_file)
    create_file(err_file)
    time_format = "%Y-%m-%d %H:%M:%S"

    # 设置需要输出到控制台的等级
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)

    # 设置需要打印的日志等级
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(message):
        set_handler('debug')
        logger.debug("[DEBUG] " + "[" + set_now_time() + "] " + message)
        remove_handler('debug')

    @staticmethod
    def info(message):
        set_handler('info')
        logger.info("[INFO] " + "[" + set_now_time() + "] " + message)
        remove_handler('info')

    @staticmethod
    def warning(message):
        set_handler('warning')
        logger.warning("[WARNING] " + "[" + set_now_time() + "] " + message)
        remove_handler('warning')

    @staticmethod
    def error(message):
        set_handler('error')
        logger.error("[ERROR] " + "[" + set_now_time() + "] " + message)
        remove_handler('error')


if __name__ == "__main__":
    MyLog.debug("debug")
    MyLog.info("info")
    MyLog.warning("warning")
    MyLog.error("error")
