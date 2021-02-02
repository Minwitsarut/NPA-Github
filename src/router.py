class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interface = {}

    def add_int(self, int_name):
        self.interface[int_name] = ['-', '-']

    def add_ip(self, int_name, ip):
        self.interface[int_name][0] = ip

    def add_connect(self, int_name, connect):
        self.interface[int_name][1] = connect


       
r1 = Router('Cisco', 'IOSv', 'R1')
r2 = Router('Cisco', '3745', 'R2')
r3 = Router('Juniper', 'MXS', 'R3')

r1.add_int('Serial 0/1')
r1.add_int('Serial 0/2')
r2.add_int('Serial 0/1')
r2.add_int('Serial 0/2')
r2.add_int('Serial 0/3')
r3.add_int('Serial 0/1')

r1.add_ip('Serial 0/1', '192.168.1.1')
r1.add_ip('Serial 0/2', '192.168.2.1')
r2.add_ip('Serial 0/1', '192.168.3.1')
r2.add_ip('Serial 0/2', '192.168.4.1')
r2.add_ip('Serial 0/3', '192.168.5.1')
r3.add_ip('Serial 0/1', '192.168.6.1')

r1.add_connect('Serial 0/1', r2.interface['Serial 0/2'][1])
r1.add_connect('Serial 0/2', r3.interface['Serial 0/1'][1])


# count interfaces
# print('Show interfaces of '+ r1.hostname + '\n' + r1.hostname + ' has ' + r1.interface + 'interfaces \n')
print(r1.interface)
print(r2.interface['Serial 0/1'][0])
print(r3.interface['Serial 0/1'][0])



# r1_dict = r1.__dict__
# print(r1_dict['hostname'])

