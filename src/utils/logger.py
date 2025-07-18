import logging

def get_logger(name="scraper"):
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger(name)
