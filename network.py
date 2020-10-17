import requests
import socket
import psutil
from tabulate import tabulate


def check_local():
    """Checks for hostname."""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


def check_connectivity():
    """Checks for Connection Status"""
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200


class Network_details(object):
    def __init__(self):
        """Constructor for Network_details Class"""
        self.parser = psutil.net_if_addrs()

    def __repr__(self):
        """Function to return all connections available."""
        self.interfaces = []
        self.address_ip = []
        self.netmask_ip = []
        self.broadcast_ip = []
        for if_name, if_add in self.parser.items():
            self.interfaces.append(if_name)
            for add in if_add:
                if str(add.family) == 'AddressFamily.AF_INET':
                    self.address_ip.append(add.address)
                    self.netmask_ip.append(add.netmask)
                    self.broadcast_ip.append(add.broadcast)
        data = {"Interface": [*self.interfaces],
                "IP-Address": [*self.address_ip],
                "NetMask": [*self.netmask_ip],
                "Broadcast-IP": [*self.netmask_ip]
                }
        return tabulate(data, headers="keys", tablefmt="github")
