from datetime import datetime

import requests
from st2reactor.sensor.base import PollingSensor


class LibreNMSBasePollingSensor(PollingSensor):
    api_key = None
    api_root = None
    api_call = None
    method = None
    params = {}
    payload = None
    last_poll = None
    trigger_name = None
    logger = None

    def _build_params(self):
        return

    def setup(self):
        self.logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        try:
            self.api_key = self._config["api_key"]
            self.api_root = self._config["api_root"]
        except KeyError:
            raise ValueError("api_key and api_root need to be configured!")

        self.last_poll = datetime.now()

        self.logger.info(f"LibreNMS polling sensor initialized for {self.trigger_name}")

    def poll(self):
        url = f"{self.api_root}/{self.api_call}"
        self.logger.debug(f"Polling {self.method} {url}")
        try:
            response = requests.request(
                method=self.method,
                url=url,
                headers={
                    "X-Auth-Token": self.api_key,
                    "User-Agent": f"StackStorm LibreNMS Pack: {self.__class__.__name__}"
                },
                data=self.payload,
                params=self._build_params(),
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ValueError("Error during HTTP request: {e}")

        self.last_poll = datetime.now()

        for event in response.json()["logs"]:
            self.sensor_service.dispatch(
                trigger=".".join(["librenms", self.trigger_name]), payload=event
            )

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def cleanup(self):
        pass


class LibreNMSLoggingSensor(LibreNMSBasePollingSensor):
    method = "get"
    log = None

    def setup(self):
        self.api_call = f"logs/{self.log}"

        if self.trigger_name is None:
            self.trigger_name = self.log

        super().setup()

    def _build_params(self):
        return {"from": self.last_poll.strftime("%Y-%m-%d %H:%M:%S")}
