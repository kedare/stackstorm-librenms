from lib.actions import LibreNMSBaseAction


class GetIPARP(LibreNMSBaseAction):
    """Get IP/ARP information"""

    method = "get"

    def run(self, ip: str):
        self.api_call = f"resources/ip/arp/{ip}"
        return self._request()
