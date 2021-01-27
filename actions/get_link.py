from lib.actions import LibreNMSBaseAction
from urllib.parse import quote


class GetLink(LibreNMSBaseAction):
    """Get a network link"""

    method = "get"

    def run(self, link_id: str):
        self.api_call = f"resources/links/{link_id}"

        return self._request()

    def _response(self, response):
        return response.json()["links"][0]
