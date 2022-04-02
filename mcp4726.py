import smbus

class mcp4726:

    def __init__(self, i2c_bus=1):
        self.bus = smbus.SMBus(i2c_bus)

    def send(self, voltage):
        data1 = (voltage >> 4)
        data2 = ((voltage & 15) << 4)
        data = [data1, data2]
        self.bus.write_i2c_block_data(0x60, 0x40, data)

