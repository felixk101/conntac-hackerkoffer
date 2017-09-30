# Usage: call start(), overwrite hackerkoffer.callback_* for your own callbacks
# or keep watch on hackerkoffer.input, .poti and .patchpanel
import serial
import threading


class Hackerkoffer:
    SEG7_NUMBERS = [0x7e, 0x48, 0x3d, 0x6d, 0x4b, 0x67, 0x77, 0x4c, 0x7f, 0x6f, 0x5f, 0x73, 0x31, 0x79, 0x37, 0x17]
    SEG7_DOT = 128
    SEG7_CLEAR = 0

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # open serial port
        print("Serial port opend: " + self.ser.name)

        self.input = []
        self.poti = []
        self.patchpanel = []
        self.led = []
        self.seg7 = []
        self.display = [[0 for x in range(128)] for y in range(64)]

        for i in range(18):
            self.input.append(False)

        for i in range(4):
            self.poti.append(0)

        for i in range(5):
            self.patchpanel.append(255)

        for i in range(11):
            self.led.append(False)

        for i in range(4):
            self.seg7.append(self.SEG7_CLEAR)

    def callback_inputs(self, id, value):
        print("Input %d: %d" % (id, value))

    def callback_potis(self, id, value):
        print("Poti %d: %d" % (id, value))

    def callback_patchpanels(self, id_from, id_to):
        print("Patchpanel %d -> %d" % (id_from, id_to))

    def _led(self, id, state=0):
        self.ser.write(bytes("O %d %d;" % (id, state), "utf-8"))
        self.led[id] = state

    def led_on(self, id):
        self._led(id, 1)

    def led_off(self, id):
        self._led(id, 0)

    # frequency not used yet
    def _piepser(self, id, state=0, frequency=0):
        self.ser.write(bytes("O %d %d;" % (id, state), "utf-8"))
        self.input[id] = state

    def piepser_on(self, id, frequency=0):
        self._piepser(id, 1, frequency)

    # frequency not used yet
    def piepser_off(self, id, frequency=0):
        self._piepser(id, 0, frequency)

    def _fan(self, id, state=0, frequency=0):
        self.ser.write(bytes("O %d %d;" % (id, state), "utf-8"))
        self.input[id] = state

    def fan_on(self, id, frequency=0):
        self._fan(id, 1, frequency)

    def fan_off(self, id, frequency=0):
        self._fan(id, 0, frequency)

    # display
    def seg7_raw(self, id, raw):
        self.ser.write(bytes("c %d %d;" % (id, int(raw))))
        self.seg7[id] = int(raw)

    def seg7_number(self, id, number):
        self.seg7_raw(id, self.SEG7_NUMBERS[number])

    def set_pixel(self, x, y, state):
        self.ser.write(bytes("d %d %d %d" % (x,y,state), "utf-8"))
        self.display[x][y] = state


hackerkoffer = Hackerkoffer()


def handle_patchpanel(data):
    # check, if there are two integers
    id_from, id_to = data.split(' ')
    hackerkoffer.patchpanel[int(id_from)] = int(id_to)
    hackerkoffer.callback_patchpanels(int(id_from), int(id_to))


def handle_inputs(data):
    id, value = data.split(' ')
    hackerkoffer.input[int(id)] = int(value)
    hackerkoffer.callback_inputs(int(id), int(value)==1)


def handle_potis(data):
    id, value = data.split(' ')
    hackerkoffer.poti[int(id)] = int(value)
    hackerkoffer.callback_potis(int(id), int(value))


def handle_data(data):
    if len(data) <= 0:
        return

    typ = data[0]
    data = data[2:]

    if typ == 'E':
        print("Error: %s" % data)
    elif typ == 'P':
        handle_patchpanel(data)
    elif typ == 'I':
        handle_inputs(data)
    elif typ == 'A':
        handle_potis(data)


def read_from_port(ser):
    buf = ''
    while True:
        reading = ser.readline().decode()
        buf = buf + reading
        parts = buf.split(';')
        for part in parts[:-1]:
            handle_data(part)
        buf = parts[-1]


def start():
    # background thread to read from device
    thread = threading.Thread(target=read_from_port, args=(hackerkoffer.ser,))
    thread.start()