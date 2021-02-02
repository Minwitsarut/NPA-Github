class Router:
    def router_details():
        r1 = Router('Cisco', 'IOSv', 'R1')
        r2 = Router('Cisco', '3745', 'R2')
        r3 = Router('Juniper', 'MXS', 'R3')

        r1.add_inf('Gigabit 0/1')
        r1.add_inf('Gigabit 0/2')
        r2.add_inf('Gigabit 0/1')
        r2.add_inf('Gigabit 0/2')
        r2.add_inf('Gigabit 0/3')
        r3.add_inf('Gigabit 0/1')

        print(r1.show_infs())
        print(r2.show_infs())
        print(r3.show_infs())

        r1.connect('Gigabit 0/1', r2, 'Gigabit 0/2')
        r1.connect('Gigabit 0/2', r3, 'Gigabit 0/1')
        print(r1.show_cdp())
        print(r2.show_cdp())
        print(r3.show_cdp())
