import logging
import time
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        logging.info(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)  # Call the actual function

        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate execution time

        logging.info(f"Function '{func.__name__}' returned: {result}")
        logging.info(f"Function '{func.__name__}' execution time: {execution_time:.6f} seconds")

        return result

    return wrapper

