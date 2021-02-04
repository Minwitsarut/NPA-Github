class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interface = {}

    def add_int(self, int_name):
        self.interface[int_name] = ['-', 'not connect to any neighbor']

    def add_ip(self, int_name, ip):
        self.interface[int_name][0] = ip

    def add_connect(self, from_int, to_int, device):
        self.interface[from_int][1] = "connect to device " + device.hostname + " interface " + to_int 
        device.interface[to_int][1] = "connect to device " + self.hostname + " interface " + from_int 

    def change_hostname(self, new_name):
        self.hostname = new_name

    def show_int(self):
        print('Show interfaces of ' + self.hostname)
        print(self.hostname + " has " + str(len(self.interface)) + " interfaces")
        for att in self.interface:
            print(att)
        
    def show_neighbor(self):
        for att in self.interface:
            print(att + " " + self.interface[att][1])
        print('\n')


       
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

r1.add_connect('Serial 0/1', 'Serial 0/2', r2)
r1.add_connect('Serial 0/2', 'Serial 0/1', r3)

r1.change_hostname("R1-NEW")
r2.change_hostname("R2-NEW")
r3.change_hostname("R3-NEW")



r1.show_int()
r1.show_neighbor()

r2.show_int()
r2.show_neighbor()


r3.show_int()
r3.show_neighbor()

# count interfaces
# print('Show interfaces of '+ r1.hostname + '\n' + r1.hostname + ' has ' + r1.interface + 'interfaces \n')




# r1_dict = r1.__dict__
# print(r1_dict['hostname'])

