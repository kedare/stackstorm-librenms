from lib.actions import LibreNMSBaseAction


class GetDevice(LibreNMSBaseAction):
    """Get a single device by ID or hostname"""

    method = "get"

    def run(self, id: str):
        self.api_call = f"devices/{id}"
        return self._request()
