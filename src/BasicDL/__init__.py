import os
import sys

# Add the 'src' directory to sys.path to make BasicDL importable
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

def setup_logging():
    import logging  # Local import to avoid circular import error
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
    log_dir = "logs"
    log_filepath = os.path.join(log_dir, "running_logs.log")
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format=logging_str,
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger("BasicDL")
    return logger