import logging
import functools

FILENAME = "logs.txt"
FILEMODE = 'a'
FORMAT = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
LEVEL = logging.DEBUG
DATEFORMAT = '%H:%M:%S'

logging.basicConfig(
    filename=FILENAME,
    filemode=FILEMODE,
    level=LEVEL,
    format=FORMAT,
    datefmt=DATEFORMAT
)

def log(func): 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_values = [repr(x) for x in args]
        kwargs_values = [repr(x) for x in kwargs.values()]
        all_values = ", ".join(args_values + kwargs_values)
        logging.info(f"function {func.__name__} called with args {all_values}")

        try:
            result = func(*args, **kwargs)
            return result

        except Exception as e:
            # Log results
            logging.info(f"Exception raised in {func.__name__}. Exception ------> {str(e)}")
            raise e
    
    return wrapper