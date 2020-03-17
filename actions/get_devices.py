from lib.actions import LibreNMSBaseAction


class GetDevices(LibreNMSBaseAction):
    """Get a device"""

    method = "get"

    def run(self, **kwargs):
        self.api_call = "devices"

        for key in kwargs:
            self.params[key] = kwargs[key]

        return self._request()

    def _response(self, response):
        data = response.json()["devices"]
        return data
