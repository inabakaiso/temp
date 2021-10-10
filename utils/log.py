#自作ログ
from logger import StreamHandler, DEBUG, Formatter, FileHandler, getLogger

DIR = 'the Path to this dir'

logger = getLogger(__name__)

#関数
def logger():
    log_fmt = Formatter('%(asctime)s %(name)s %(linear)d [%(levelname)s][%(funcName)s][%(message)s ')
    handler = StreamHandler()
    handler.setlevel('INFO')
    hendler.setFormatter(log_fmt)
    logger.addHandler(handler)
    
    handler = FileHandler(DIR + 'train.py.log', 'a')
    handler.setlevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setlevel(DEBUG)
    logger.addHandler(handler)
    
    return logger

if __name__ == '__main__':
    log_fmt = Formatter('%(asctime)s %(name)s %(linear)d [%(levelname)s][%(funcName)s][%(message)s ')
    handler = StreamHandler()
    handler.setlevel('INFO')
    hendler.setFormatter(log_fmt)
    logger.addHandler(handler)
    
    handler = FileHandler(DIR + 'train.py.log', 'a')
    handler.setlevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setlevel(DEBUG)
    logger.addHandler(handler)
    #以下から通常の文を書き進めつつ
    #logger.info('注意事項')
    #logger.debug('')

