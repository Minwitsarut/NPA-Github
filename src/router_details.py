class Router:
    def __init__(self, brand, model,hostname): 
        self.brand = brand
        self.model = model
        self.hostname = hostname
class Interface:
    def __init__(self, ip, connect):
        self.ip = {}
        self.connect = {}

    def add_ip():

    def add_connect():

r1 = Router('Cisco', 'IOSv', 'R1')
r2 = Router('Cisco', '3745', 'R2')
r3 = Router('Juniper', 'MXS', 'R3')

r1 = Interface('')      
print('Router Name : ' + r1.hostname + '\n' + 'Brand : ' + r1.brand + '\n' + 'Model : ' + r1.model + '\n')
print('Router Name : ' + r2.hostname + '\n' + 'Brand : ' + r2.brand + '\n' + 'Model : ' + r2.model + '\n')
print('Router Name : ' + r3.hostname + '\n' + 'Brand : ' + r3.brand + '\n' + 'Model : ' + r3.model + '\n')


#         print(r1.show_infs())
#         print(r2.show_infs())
#         print(r3.show_infs())

#         r1.connect('Gigabit 0/1', r2, 'Gigabit 0/2')
#         r1.connect('Gigabit 0/2', r3, 'Gigabit 0/1')
#         print(r1.show_cdp())
#         print(r2.show_cdp())
#         print(r3.show_cdp())

# if __name__ == '__main__':
#     main()
    

