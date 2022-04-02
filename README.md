# API server for mcp4726

## setup
```
make setup
```
## running server
```
make start
```
## using
```
curl -X POST http://localhost:8000/ -d '{"data": [1,2,3]}' -v
```
## docker
make sure your i2c device is on /dev/i2c-1
```
make docker-run
```
otherwise, use the following after building
```
docker run --device /dev/i2c-<whatever> sampling-api
```