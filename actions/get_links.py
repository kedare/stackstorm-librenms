from lib.actions import LibreNMSBaseAction
from urllib.parse import quote


class GetLinks(LibreNMSBaseAction):
    """Get network links"""

    method = "get"

    def run(self, hostname: str):
        self.api_call = f"devices/{hostname}/links"

        return self._request()

    def _response(self, response):
        return response.json()["links"]
