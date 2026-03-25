from datetime import datetime
from importlib.metadata import version
from multiprocessing.synchronize import Event as EventClass
import time

from remote_app.utils.logging_utils import root_logger as logger


class AppController:
    _step_event: EventClass

    def __init__(self, stop_event: EventClass):
        self._stop_event = stop_event

    def run(self) -> None:
        app_version = version("remote-app")
        logger.info("starting remote-app (version %s)", app_version)
        while not self._stop_event.is_set():
            logger.info("Running %s", datetime.now())
            time.sleep(30)

        logger.info("stopping remote-app (version %s)", app_version)
