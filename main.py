def read_ds_sensor():
  roms = ds_sensor.scan()
  #print('Found DS devices: ', roms)
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
      try:
          temp = ds_sensor.read_temp(rom)
          if isinstance(temp, float):
              temp = round(temp, 2)
      #print('Valid temperature')
              return (f'Street {temp}')
      except Exception as ex:
          return ex
  #return '0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('IP', 1337))
server.listen()

#client, addr = server.accept()
#print(read_ds_sensor())
while True:
    client, addr = server.accept()
    message = client.recv(1024).decode()
    if message == "KEY1":
        
        #read_sensor()  
        #print(read_ds_sensor())
        x = read_ds_sensor()
        #print (x)
        client.sendall(x)
        client.close()


