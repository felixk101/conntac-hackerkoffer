from hackerkoffer_lib import start, hackerkoffer
import time
import nyan as nyan

def handle_inputs(id, value):
    # turn LEDs depending on switches
    if id >= 6 and id <=9:
        hackerkoffer._led(id-6, value)

    if id == 10:
        nyan.nyan()
        pass

    if id == 12 or id == 13:
        hackerkoffer._led(id-7, value)

    if id >= 1 and id <= 5:
        piepser = 16 if hackerkoffer.poti[0] > 4000 and hackerkoffer.poti[1] > 4000 else 15
        hackerkoffer._piepser(piepser, value)

    if id == 11 or id == 14:
        if hackerkoffer.input[11] and hackerkoffer.input[14]:
            knightrider(True)
        else:
            knightrider(False)

    if id == 0:
        if hackerkoffer.input[11] and hackerkoffer.input[14]:
           #hackerkoffer.input[12] and \ #not working at the moment
           #hackerkoffer.input[13] and \ # not working at the moment
            piepkonzert()
        else:
            hackerkoffer.piepser_on(15)
            time.sleep(0.2)
            hackerkoffer.piepser_off(15)
            hackerkoffer.piepser_on(16)
            time.sleep(0.4)
            hackerkoffer.piepser_off(16)

def handle_potis(id, value):
    if id == 0:
        hackerkoffer.seg7_number(0, value % 10)
        hackerkoffer.seg7_number(1, int(value % 100 / 10))
        hackerkoffer.seg7_number(2, int(value % 1000 / 100))
        hackerkoffer.seg7_number(3, int(value % 10000 / 1000))


def piepkonzert():
    for i in range(100):
        hackerkoffer.piepser_on(15)
        time.sleep(0.2)
        hackerkoffer.piepser_off(15)
        hackerkoffer.piepser_on(16)
        time.sleep(0.2)
        hackerkoffer.piepser_off(15)

def knightrider(active):
    if active:
        for i in range(5):
            hackerkoffer.led_off(0)

        for loop in range(3):
            for i in range(0,5):
                hackerkoffer.led_on(i)
                time.sleep(0.05)
                hackerkoffer.led_off(i)

            for i in range(5,0):
                hackerkoffer.led_on(i)
                time.sleep(0.05)
                hackerkoffer.led_off(i)

        time.sleep(1)

    for i in range(5):
        hackerkoffer._led(i, hackerkoffer.input[i+6])

def main():
    hackerkoffer.callback_inputs = handle_inputs
    hackerkoffer.callback_potis = handle_potis
    start()


if __name__ == "__main__":
    main()
