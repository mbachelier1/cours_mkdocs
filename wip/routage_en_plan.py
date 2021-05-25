class IP:
    pass


class Network:
    pass


class Connection:
    def __init__(self, network1: Network, router1_ip: IP, router1_port: int, network2: Network, router2_ip: IP,
                 router2_port: int, speed=None):
        self.network1 = network1
        self.router1_ip = router1_ip
        self.router1_port = router1_port
        self.network2 = network2
        self.router2_ip = router2_ip
        self.router2_port = router2_port
        self.speed = speed


def __repr__(self):
    return f"Network : {self.network}, IP on network : {self.router_ip}"


class Router:
    def __init__(self, name: str):
        self.name = 0
        self.connection = []
        self.routing_table = []

    def __repr__(self):
        result = f"{self.name}\n"
        for c in self.connection:
            print("\t" + str(c))
