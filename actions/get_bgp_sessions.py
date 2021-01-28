from lib.actions import LibreNMSBaseAction


class GetBGPSessions(LibreNMSBaseAction):
    """Get BGP sessions"""

    method = "get"

    def run(self, **kwargs):
        self.api_call = "bgp"

        for key in kwargs:
            self.params[key] = kwargs[key]

        return self._request()
