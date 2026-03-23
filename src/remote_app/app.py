from datetime import datetime
from importlib.metadata import version
import logging
from multiprocessing.synchronize import Event as EventClass
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class AppController:
    _step_event: EventClass

    def __init__(self, stop_event: EventClass):
        self._stop_event = stop_event

    def run(self) -> None:
        app_version = version("remote-app")
        logging.info("starting remote-app (version %s)", app_version)
        while not self._stop_event.is_set():
            logging.info("Running %s", datetime.now())
            time.sleep(30)

        logging.info("stopping remote-app (version %s)", app_version)
