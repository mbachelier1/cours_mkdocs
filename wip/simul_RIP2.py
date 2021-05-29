class IP:
    @staticmethod
    def str_ip_to_num_ip(value: str) -> int:
        value = value.split('.')
        return int(value[0]) * 2 ** 24 + int(value[1]) * 2 ** 16 + int(value[2]) * 2 ** 8 + int(value[3])

    @staticmethod
    def num_ip_to_str_ip(value: int) -> str:
        result = []
        for _ in range(4):
            result = [str(value % 2 ** 8)] + result
            value //= 2 ** 8
        return '.'.join(result)

    def __init__(self, value: object) -> object:
        """
        :param value: can be a str like '192.168.0.1' or an int
        """
        if isinstance(value, int):
            self.num = value
            self.str = IP.num_ip_to_str_ip(value)
        else:
            self.num = IP.str_ip_to_num_ip(value)
            self.str = value

    def __repr__(self):
        return self.str

    def __int__(self):
        return self.num

    def __eq__(self, other):
        return self.num == other.num


class Network:
    def __init__(self, ip, mask: int):
        self.ip = ip if isinstance(ip, IP) else IP(ip)
        self.mask = mask
        self.bin_mask = int('1' * mask + '0' * (32 - mask), 2)
        if self.ip.num & self.bin_mask != self.ip.num:
            raise ValueError(f'{self.ip} / {self.mask} is not a valid couple.')
        self.broadcast_ip = IP(self.ip.num + 2 ** (32 - mask) - 1)
        self.reserved_ip = {'Network': self.ip, 'Broadcast': self.broadcast_ip}

    def add_terminal(self, ip=None, name="generic terminal"):
        """
        :param ip: Any(str,IP,NoneType)
        :param name: str
        :return: None
        """
        if ip is None:
            min_ip = max((self.reserved_ip[device] for device in self.reserved_ip if device!='Broadcast'), key=lambda x: x.num)
            if min_ip == self.broadcast_ip:
                raise ConnectionError(f'{str(self)} is full.')
            else:
                ip = IP(min_ip.num + 1)
        if not isinstance(ip, IP):
            ip = IP(ip)
        if ip.num & self.bin_mask != self.ip.num:
            raise ValueError(f'{ip} is not a valid IP of the network.')
        for rip in self.reserved_ip:
            if self.reserved_ip[rip] == ip:
                raise ValueError(f'{ip} already attributed to {rip}.')
        else:
            self.reserved_ip[name] = ip



    def __repr__(self):
        return f'{self.ip} / {self.mask}\n'

    def describe(self):
        result = f'{self.ip} / {self.mask}\n'
        for name in self.reserved_ip:
            if name not in ('Network', 'Broadcast'):
                result += f'\t{self.reserved_ip[name]} : {name}\n'
        return result


class Interface:
    def __init__(self, network1: Network, router1_ip: IP, router1_port: int, network2: Network, router2_ip: IP,
                 router2_port: int, speed=None):
        self.network1 = network1
        self.router1_ip = router1_ip
        self.router1_port = router1_port
        self.network2 = network2
        self.router2_ip = router2_ip
        self.router2_port = router2_port
        self.speed = speed


class Router:
    def __init__(self, name: str):
        self.name = name
        self.interface = []
        self.routing_table = []

    def __repr__(self):
        result = f"{self.name}\n"
        for c in self.interface:
            result += "\t" + str(c) + "\n"
        return result


n = Network('100.16.0.0', 13)
n.add_terminal(name='PC1')
n.add_terminal(name='PC2')
print(n)
print(n.describe())