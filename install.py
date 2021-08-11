import sys

if not sys.platform == "win32":
    sys.exit("this installer was generated for win32 systems")

import getpass
import zipfile
import os
from os import startfile
import time
import shutil
from colorama import init, Fore, Style

def pause(amount: float = 1.0) -> None:
    "use time.sleep to pause. This can be forced by typing Ctrl+C"
    try:
        time.sleep(amount)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Unexpected error:", str(e))

if __name__ == '__main__':
    try:
        init(autoreset=True)
        print(Fore.GREEN+"Welcome to the Diego Ramirez' installer!")
        print("""Before installing, please get sure the folder 'C:/Program Files/Control de Agua'
is not being used by any other program. """+Style.BRIGHT+"Press Enter if you are ready.", end="")
        s = getpass.getpass(" ")
        print(Style.BRIGHT+Fore.GREEN+"Installing 'Control de Agua' on 'C:/Program Files/Control de Agua'...")
        if not os.path.exists("C:/Program Files/Control de Agua"):
            print(Fore.GREEN+"Generating the destination folder...")
            shutil.copytree("supply_folder", "C:/Program Files/Control de Agua")
        else:
            print(Fore.YELLOW+"warning: the destination folder already exists.")
            print(Fore.GREEN+"Removing the previous folder...")
            shutil.rmtree("C:/Program Files/Control de Agua")
            shutil.copytree("supply_folder", "C:/Program Files/Control de Agua")
        print(Fore.GREEN+"installing source code (python)... please wait...")
        pause(0.7)
        print(Fore.GREEN+"installing other files (images, databases)...")
        pause(1)
        print(Fore.GREEN+"installing binaries...")
        pause(1.4)
        print(Fore.GREEN+"installing the executables...")
        pause(0.5)
        print(Fore.GREEN+"pasting the contents... please wait...")
        z = zipfile.ZipFile("Control de Agua-1.0.0.zip")
        z.extractall('C:/Program Files/Control de Agua')
        print(Fore.GREEN+Style.BRIGHT+"completely done. Press Enter if you are done.", end=" ")
        s = getpass.getpass("")
        startfile("C:/Program Files/Control de Agua/Control de Agua.lnk")
    except Exception as e:
        print(Style.BRIGHT+Fore.RED+"An error ocurred."+"\n"+"  Error:", str(e))
        print("Press Enter to close.", end="")
        s = getpass.getpass(" ")
    print("Made with love by Diego Ramirez... see you!")
    pause(0.7)
