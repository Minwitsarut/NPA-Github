def cubic(side):
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MX5', 'R3')

    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r2.add_inf('Gigabit 0/1')
    r2.add_inf('Gigabit 0/2')
    r2.add_inf('Gigabit 0/3')
    r3.add_inf('Gigabit 0/1')

print(r1.show_infs())
