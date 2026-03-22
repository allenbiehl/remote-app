import time
from datetime import datetime
from multiprocessing.synchronize import Event as EventClass
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class AppController:
    _step_event: EventClass

    def __init__(self, stop_event: EventClass):
        self._stop_event = stop_event

    def run(self) -> None:
        logging.info("starting remote-app (version 1.0.4)")
        while not self._stop_event.is_set():
            logging.info("Running %s", datetime.now())
            time.sleep(30)

        logging.info("stopping remote-app (version 1.0.4)")
