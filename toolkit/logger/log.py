import logging
from logging import handlers


class Logger():
    """
    日志工具类
    """
    __level_maps = {'debug': logging.DEBUG, 'info': logging.INFO, 'warn': logging.WARN, 'error': logging.ERROR}

    def __init__(self,
                 fpath: str = '/log/',
                 fname: str = 'app.log',
                 level: str = 'info',
                 mBytes: int = 10 * 1024 * 1024,
                 bCount: int = 3,
                 fmt: str = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s') -> None:
        # 获取日志对象
        self.log = logging.getLogger(fname)
        # 设置日志格式
        log_format = logging.Formatter(fmt)
        # 获取日志级别
        log_level = self.__level_maps.get(level)
        # 设置日志级别
        self.log.setLevel(log_level)
        """
        往屏幕上输出
        """
        sh_out = logging.StreamHandler()
        sh_out.setFormatter(log_format)
        self.log.addHandler(sh_out)
        """
        往文件里写入普通日志, maxBytes: 每个日志文件最大字节数, backupCount: 保存日志的数量
        """
        cPath = fpath + fname
        common_handler = handlers.RotatingFileHandler(cPath, maxBytes=mBytes, backupCount=bCount, encoding='utf-8')
        common_handler.setFormatter(log_format)
        self.log.addHandler(common_handler)
        """
        往文件里写入错误日志, maxBytes: 每个日志文件最大字节数, backupCount: 保存日志的数量
        """
        sIndex = fname.index(".")
        ePath = fpath + fname[:sIndex] + '-error' + fname[sIndex:]
        error_handler = handlers.RotatingFileHandler(ePath, maxBytes=mBytes, backupCount=bCount, encoding='utf-8')
        error_handler.setFormatter(log_format)
        error_handler.setLevel(logging.ERROR)
        self.log.addHandler(error_handler)
