import sys

if not sys.platform == "win32" or sys.version_info < (3, 6):
    sys.exit("this installer was generated for win32 systems with Python 3.6 or greater")

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
        print("Unexpected error:", str(e), f"{type(e).__name__}")

if __name__ == '__main__':
    try:
        init(autoreset=True)
        print(Fore.GREEN+"Welcome to the Diego Ramirez' installer!")
        print("""Before installing, please get sure the folder 'C:/Program Files/Control de Agua'
is not being used by any other program. """+Style.BRIGHT+"Press Enter if you are ready.", end="")
        getpass.getpass(" ")
        print(Style.BRIGHT+Fore.GREEN+"Installing 'Control de Agua' on 'C:/Program Files/Control de Agua'...")
        if not os.path.exists("C:/Program Files/Control de Agua"):
            print(Fore.GREEN+"Generating the destination folder...")
            actual_cwd = os.getcwd()
            os.chdir("C:/Program Files")
            os.makedirs("Control de Agua")
            os.chdir(actual_cwd)
        else:
            print(Fore.YELLOW+"warning: the destination folder already exists.")
            print(Fore.GREEN+"Removing the previous folder...")
            shutil.rmtree("C:/Program Files/Control de Agua")
            actual_cwd = os.getcwd()
            os.chdir("C:/Program Files/")
            os.makedirs("Control de Agua")
            os.chdir(actual_cwd)
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
        getpass.getpass("")
    except OSError as e:
        print(Fore.YELLOW+f"The OS system raised an error:\n {str(e)}\n")
        print("""Check the permissions, check if no other program is using 'C:/Program FIles/Control De Agua'
and try again.""", end="")
        getpass.getpass(" ")
    except KeyboardInterrupt:
        print(Fore.CYAN+"Operation cancelled by user. The original installation may be damaged.")
    except Exception as e:
        print(Style.BRIGHT+Fore.RED+"An unexpected error ocurred."+"\n"+"  Error:", str(e)+"\n")
        print(Style.BRIGHT+Fore.RED+"Please report this at <https://github.com/ControlDeAgua/bug_tracker/issues>.")
        print("Press Enter to close.", end="")
        getpass.getpass(" ")
    print("Installer made with love by Diego Ramirez... see you!")
    pause(0.7)
