from hackerkoffer_lib import start, hackerkoffer
import time

def test_all_leds():
    print("BEGINNING LED TEST")

    for i in range(11):
        print("LED %i" %i)
        hackerkoffer.led_on(i)
        time.sleep(0.5)
        hackerkoffer.led_off(i)

    print("END OF LED TEST")


def test_all_piepser():
    print("BEGINNING PIEPSER TEST (HIGH/LOW)")

    for i in (15,16):
        hackerkoffer.piepser_on(i)
        time.sleep(1)
        hackerkoffer.piepser_off(i)

    print("END OF PIEPSER TEST")


def test_fan():
    print("BEGINNING FAN TEST")
    hackerkoffer.fan_on(17)
    time.sleep(3)
    hackerkoffer.fan_off(17)
    print("END OF FAN TEST")


def test_seg7():
    print("BEGINNING OF SEG7 TEST (RIGHT TO LEFT)")
    for segment in range(4):
        for i in range(10):
            hackerkoffer.seg7_number(segment, i)
            time.sleep(0.5)
            hackerkoffer.seg7_raw(segment, hackerkoffer.SEG7_CLEAR)

        time.sleep(2)

    print("END OF SEG7 TEST")


def wait_on_input(id, state):
    while True:
        if hackerkoffer.input[id] == state:
            return
        time.sleep(1)


def wait_on_poti_min(id):
    while True:
        if hackerkoffer.poti[id] <= 10:
            return
        time.sleep(1)


def wait_on_poti_max(id):
    while True:
        if hackerkoffer.poti[id] >= 4086:
            return
        time.sleep(1)


def test_inputs():
    for i in range(15):
        print("Flip switch %d on" % i)
        wait_on_input(i, True)
        print("Flip switch %d off" % i)
        wait_on_input(i, False)


def test_potis():
    for i in range(4):
        print("Turn poti %d to min" % i)
        wait_on_poti_min(i)
        print("Turn poti %d to max" % i)
        wait_on_poti_max(i)


def wait_on_panel_plug(id_from, id_to):
    while True:
        if hackerkoffer.patchpanel[id_from] == id_to:
            return
        time.sleep(1)


def wait_on_panel_unplug():
    while True:
        if hackerkoffer.patchpanel[0] == 255 \
                and hackerkoffer.patchpanel[1] == 255 \
                and hackerkoffer.patchpanel[2] == 255 \
                and hackerkoffer.patchpanel[3] == 255 \
                and hackerkoffer.patchpanel[4] == 255:
            return
        time.sleep(1)


def test_panels():
    for i in range(5):
        print("Plug cabel from %d to %d" % (i,i))
        wait_on_panel_plug(i,i)
        print("Unplug cabel")
        wait_on_panel_unplug()


def test_all_outputs():
    print("BEGINNING OUTPUT TESTS")
    test_all_leds()
    time.sleep(2)
    test_all_piepser()
    time.sleep(2)
    test_seg7()
    time.sleep(2)
    test_fan()


def test_all_inputs():
    print("BEGINNING INPUT TESTS")
    test_inputs()
    test_potis()
    test_panels()


def test_all():
    test_all_outputs()
    test_all_inputs()

    print("TEST SUCCESSFUL, BOOYAH!")


def main():
    start()

    test_all()


if __name__ == "__main__":
    main()
