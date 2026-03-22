import time
from datetime import datetime

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("starting remote-app")

while True:
    logging.info("Running %s", datetime.now())
    time.sleep(30)
