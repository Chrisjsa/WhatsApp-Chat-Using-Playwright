from .clean_text import clean_text_for_logging
import logging
import inspect
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_caller_info(context: str = None, ex: Exception = None,
                    error: bool = False, warning: bool = False,
                    depth: int = 3, show_logger: bool = True) -> str:
    """
    Locate the function where this function is called from and provide additional information.

    :param context: str, optional. Additional context information to be included in the output.
    :param ex: Exception, optional. The exception that occurred, if any.
    :param error: bool, optional. If True, indicates that an error occurred.
    :param warning: bool, optional. If True, indicates that a warning occurred.
    :param depth: int, optional. The depth of the call stack to include in the output.
    :param show_logger: bool, optional. If True, logs the output using the logger.
    :return: str. The information about the located function.
    """

    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_code.co_name
    locate = inspect.getfile(caller_frame).split('/')
    locate = ".".join(map(str, locate[-depth:]))
    locate_info = f'{locate[:-2]}{caller_name}'

    if context:
        context = clean_text_for_logging(context, max_length=500)
        locate_info = f'{locate_info} {context}'

    if ex:
        ex_type = 'Unexpected exception in '
        if error:
            ex_type = 'Error in '
        if warning:
            ex_type = 'Warning in '

        locate_info = f'{ex_type}{locate_info} | Exception: {ex} | Line -{sys.exc_info()[-1].tb_lineno}-'
    else:
        locate_info = f'{"Error" if error else "Warning"} in {locate_info}'

    if show_logger:
        if error:
            logger.error(locate_info)
        elif warning:
            logger.warning(locate_info)
        else:
            logger.info(locate_info)

    return locate_info