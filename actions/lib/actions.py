import requests

from st2common.runners.base_action import Action
from typing import Mapping, Any


class LibreNMSBaseAction(Action):
    """
    Base action for LibreNMS, to be inherited from.
    """

    api_key: str = None
    api_root: str = None
    api_call: str = None
    method: str = None
    params: Mapping[str, str] = {}
    payload: Mapping[str, Any] = None

    def __init__(self, config):
        super().__init__(config)
        try:
            self.api_key = self.config["api_key"]
            self.api_root = self.config["api_root"]
        except KeyError:
            raise ValueError("api_key and api_root need to be configured!")

    def _request(self):
        try:
            response = requests.request(
                method=self.method,
                url=f"{self.api_root}/{self.api_call}",
                params=self.params,
                headers={
                    "X-Auth-Token": self.api_key,
                    "User-Agent": f"StackStorm LibreNMS Pack: {self.__class__.__name__}"
                },
                data=self.payload,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ValueError("Error during HTTP request: {e}")

        return self._response(response)

    def _response(self, response: requests.Response) -> requests.Response:
        return response.json()
