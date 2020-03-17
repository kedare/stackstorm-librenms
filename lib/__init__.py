import requests

from st2common.runners.base_action import Action


class LibreNMSApiBaseAction(Action):

    api_key = None
    api_root = None
    api_call = None
    method = None
    payload = None

    def __init__(self, config):
        super().__init__(self, config)
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
                headers={"X-Auth-Token": self.api_key},
                data=self.payload
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ValueError("Error during HTTP request: {e}")

        return response.json()

