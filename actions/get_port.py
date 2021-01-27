from lib.actions import LibreNMSBaseAction
from urllib.parse import quote


class GetPort(LibreNMSBaseAction):
    """Get a port"""

    method = "get"

    def run(self, port_id: str):
        self.api_call = f"ports/{port_id}"

        return self._request()

    def _response(self, response):
        return response.json()["port"][0]
