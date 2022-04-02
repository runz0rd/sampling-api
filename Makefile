# https://www.bitwizard.nl/wiki/I2C_DAC
# 1     number of the I2C bus (0 on older raspberry pi's)
# 0x60  address of the DAC, use 0x61 (or 0x62 and 0x63) for the other DAC.
# 0x40  configuration: normal.
# 0xff  high 8 bits of the value
# 0xf0  lower four bits of the value (in the high nibble)
setup:
	sudo apt install i2c-tools -y
	sudo i2cdetect 1
	sudo i2cset -y 1 0x60 0x40 0xff 0xf0 i
	sudo pip3 install -r requirements.txt

start:
	python server.py

docker-run:
	docker build . -t sampling-api
	docker run --device /dev/i2c-1 sampling-api