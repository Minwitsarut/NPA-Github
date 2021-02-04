from src.router import pytest 
@pytest.fixture(scope='module')
def default_router():
    name = 'default'
    return Router(name)

@pytest.fixture(scope='module')
def default_interface():
    port = 'fa0/1'
    cidr = '192.168.0.0/24'
    ip_address = '192.168.1.1'
    fa01 = Interface(port=port, cidr=cidr, ip_address=ip_address)
    return fa01

class TestInit(object):
    def test_valid_args(self,default_router):
        router = default_router
        name = router.hostname

        hostname_message = f'Expected "default" as hostname, Actual: <{name}>'
        assert router.hostname == 'default',hostname_message

        expected_commands = ["en", "conf t", "no ip domain-lookup"]
        actual_commands   = router.commands
        commands_message  = f'Expected: {expected_commands}\n Actual: <{actual_commands}>'
        assert actual_commands == expected_commands,commands_message

        router_message = "Expected to get the default router"
        assert Router._all_routers[0] == router,router_message

    def test_invalid_args(self,default_router):
        """Test that if you try and make a second Router with the same name, it will fail."""
        router = default_router
        with pytest.raises(ValueError):
            router1 = Router("default")

class TestAddInterface(object):
    def test_valid_args(self,default_router,default_interface):
        router = default_router
        router.add_interface(default_interface)

        expected_interface = 'fa 0/1,192.168.0.0/24,192.168.1.1'
        actual_interface   = str(router.interfaces[0])
        interface_add_message = f'Expected: {expected_interface}\n Actual:'
        assert actual_interface == expected_interface,interface_add_message

    def test_add_two_same_interfaces(self,default_interface,default_router):
        """This test adds the same interface to a Router twice to test that it raises
        a ValueError."""
        print("current directory", os.getcwd())
        router = default_router
        interface = default_interface
        router.add_interface(interface)
        repeat_interface = 'fa0/1,192.168.0.0/24,192.168.1.1'.split(",")
        print(repeat_interface)
        with pytest.raises(ValueError):
            new_copy = Interface(repeat_interface[0], repeat_interface[1], repeat_interface[2])
            print([id(x) for x in router.interfaces])
            print(id(new_copy))
            router.add_interface(new_copy)