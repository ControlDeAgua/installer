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


class NoZipDistribution(Exception):
    "There is no ZIP file to install the files."


def pause(amount: float = 1.0) -> None:
    "use time.sleep to pause. This can be forced by typing Ctrl+C"
    try:
        time.sleep(amount)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # really strange case, that should be reported as soon as possible
        print("Unexpected error:", f"{type(e).__name__}: {str(e)}")

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
            print(Fore.YELLOW+"WARNING: The destination folder already exists. We will try to remove it.")
            print(Fore.GREEN+"Removing the previous folder...")
            shutil.rmtree("C:/Program Files/Control de Agua")
            actual_cwd = os.getcwd()
            os.chdir("C:/Program Files/")
            os.makedirs("Control de Agua")
            os.chdir(actual_cwd)
        print(Fore.GREEN+"installing source code (python scripts)... please wait...")
        pause(0.7)
        print(Fore.GREEN+"installing other files (images, databases, config files)...")
        pause(1)
        print(Fore.GREEN+"installing binaries (compiled files, DLLs)...")
        pause(1.4)
        print(Fore.GREEN+"installing the main executables...")
        pause(0.5)
        print(Fore.GREEN+"pasting the contents into the final directory... please wait...")
        # this is the dangerous zone
        try:
            z = zipfile.ZipFile("Control de Agua-1.0.0.zip")
        except FileNotFoundError:
            # there are 2 options here:
            # 1. There is no `Control de Agua-1.0.0.zip` on the same directory than
            #    the installer. Just add it.
            # 2. You are calling `install.py` or `Installer.exe` from somewhere else
            #    (maybe with the `python` command). Since we are using the `os.getcwd()`
            #    value to find the zip file, this case should fail.
            # 
            # To clarify this case, I added a separate message, to make the things
            # easier (because `FileNotFoundError` is a subclass of `OSError`).
            raise NoZipDistribution(os.getcwd())
        zlist = z.namelist()
        for member in zlist:
            print(Fore.CYAN+"Extracting "+member+"...")
        print(Fore.GREEN+"Please wait... (don't press 'Ctrl' keys!)...")
        z.extractall('C:/Program Files/Control de Agua')
        z.close()
        print(Fore.GREEN+Style.BRIGHT+"Done. Press Enter if you are done.", end=" ")
        getpass.getpass("")
    except NoZipDistribution as zip_exc:
        # we set the exception `__str__` to the current cwd, so
        # we can make things easier.
        print(Fore.YELLOW+f"""Hmm... it seems like the file 'Control de Agua-1.0.0.zip' is not present.
I'm looking at '{str(zip_exc)}'.
Verify if you have the Zip archive on this directory, and then try it again.""")
    except OSError as e:
        print(Fore.YELLOW+f"The OS system raised an error:\n {str(e)}\n")
        print("""Check the permissions, check if no other program is using 'C:/Program Files/Control De Agua',
and try again.""", end="")
        getpass.getpass(" ")
    except KeyboardInterrupt:
        print(Fore.YELLOW+"Operation cancelled by user. The final installation may be damaged or incomplete.")
    except Exception as e:
        print(Style.BRIGHT+Fore.RED+"An unexpected error ocurred."+"\n"+"  Error:", str(e)+"\n")
        print(Style.BRIGHT+Fore.RED+"Please report this at <https://github.com/ControlDeAgua/bug_tracker/issues>.")
        print("Press Enter to close.", end="")
        getpass.getpass(" ")
    print("Installer made with love by Diego Ramirez... see you!")
    pause(0.7)
