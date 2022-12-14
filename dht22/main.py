def read_sensor():
  global temp, hum
  temp = hum = 0
  try:
    dht_pin.measure()
    temp = dht_pin.temperature()
    hum = dht_pin.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))

      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0

      hum = round(hum, 2)
      return(f'Temp {temp}, hum {hum}')
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('IP', 1337))
server.listen()

while True:
    client, addr = server.accept()
    message = client.recv(1024).decode()
    if message == "KEY2":
        
        try:
            client.sendall(read_sensor())
            client.close()
        except Exception as ex:
            print (ex)
        
