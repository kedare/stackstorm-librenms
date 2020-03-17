from lib.actions import LibreNMSBaseAction

class GetBGPSessions(LibreNMSBaseAction):

    def run(self, remote_asn):
        self.api_call = f"bgp?remote_asn={remote_asn}"

        return self._request()

