class Router:
    def __init__(self, hostname, brand, model):
        self.hostname = hostname
        self.brand = brand
        self.model = model
        self.interface = {}
    def add_int(self, int_name):
        self.interface[int_name] = ["-", "-"]
    def add_ip(self, int_name, ip):
        self.interface[int_name][0] = ip



        
r1 = Router('R1', "BrandXX", "ModelYY")
r2 = Router('R2', "BrandXX", "ModelYY")
r3 = Router('R3', "BrandXX", "ModelYY")

r1.add_int("S0/0")
r1.add_int("S0/1")
r2.add_int
r1.add_ip("S0/0", "192.168.1.1")

print(r1.interface["S0/0"][0])
# r1_dict = r1.__dict__
# print(r1_dict['hostname'])

