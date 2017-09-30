from subprocess import call
from time import sleep



def nyan():
    call(["i3", "workspace", "8"])
    #sleep(1)
    call(["gnome-terminal", "-x", "sh", "-c", "telnet nyancat.dakko.us"])

if __name__ == '__main__':
    nyan()
