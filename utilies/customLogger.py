import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Create Logs directory if not exists
        log_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(log_dir, exist_ok=True)

        # Full path to log file
        log_file = os.path.join(log_dir, "automation.log")

        # Create a unique logger
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.INFO)
        logger.propagate = False  # Prevent duplicate logs in pytest output

        # === Reset handlers to avoid duplication ===
        if logger.hasHandlers():
            logger.handlers.clear()

        # === Create file handler ===
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # === (Optional) Stream handler for console logs ===
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # === Debug print to confirm it's working ===
        print(f"Logger initialized. Log file path: {log_file}")

        return logger