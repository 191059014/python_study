from toolkit.logger.log import Logger


class TestLogger():

    def __init__(self) -> None:
        self.logger = Logger(level='debug')


if __name__ == '__main__':
    test = TestLogger()
    test.logger.log.debug('this is debug log')
    test.logger.log.info('this is info log')
    test.logger.log.warning('this is info log')
    test.logger.log.error('this is error log')
