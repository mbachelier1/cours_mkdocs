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

    def __init__(self, value):
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

    def add_machine(self, ip, name: str):
        """

        :param ip: Any(str,IP)
        :param name: str
        :return: None
        """
        if not isinstance(ip, IP):
            ip = IP(ip)
        if ip.num & self.bin_mask != self.ip.num:
            raise ValueError(f'{ip} is not a valid IP of the network.')
        for rip in self.reserved_ip:
            if self.reserved_ip[rip] == ip:
                raise ValueError(f'{ip} already attributed to {rip}.')
        else:
            self.reserved_ip[name] = ip
        print(self.reserved_ip)

    def __repr__(self):
        result = f'{self.ip} / {self.mask}\n'
        for name in self.reserved_ip:
            if name not in ('Network','Broadcast'):
                result += f'\t{self.reserved_ip[name]} : {name}\n'
        return result


n = Network('100.16.0.0', 13)
n.add_machine(IP('100.16.0.1'), 'PC1')
n.add_machine(IP('100.16.0.2'), 'PC2')
print(n)
