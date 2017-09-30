import asyncio
import serial_asyncio
import websockets
clients = set()
connection = None

async def hello(websocket, path):
    clients.add(websocket)
    try:
        while True:
            name = await websocket.recv()
            print("from socket: "+name)
            connection.write(name.encode("utf-8"))
    except:
        pass


start_server = websockets.serve(hello, 'localhost', 5678)


class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        global connection
        connection = transport
        print('port opened', transport)
        #transport.serial.rts = False  # You can manipulate Serial object via transport
        transport.write(b'Hello, World!\n')  # Write serial data via transport

    async def doDataReceive(self, data):
        for client in clients:
            await client.send(data) #-await

    def data_received(self, data):
        print ("from serial: "+data.decode('utf-8').replace('\n', ''))
        #print('data received', repr(data))
        future = asyncio.ensure_future(self.doDataReceive(data.decode('utf-8')))
        asyncio.wait(future)

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()

    def pause_writing(self):
        print('pause writing')
        print(self.transport.get_write_buffer_size())

    def resume_writing(self):
        print(self.transport.get_write_buffer_size())
        print('resume writing')

loop = asyncio.get_event_loop()
coro = serial_asyncio.create_serial_connection(loop, Output, '/dev/pts/4', baudrate=115200)
loop.run_until_complete(coro)
loop.run_until_complete(start_server)
loop.run_forever()
loop.close()