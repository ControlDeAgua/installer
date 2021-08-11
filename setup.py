import sys

try:
    from cx_Freeze import setup, Executable
except ImportError:
    sys.exit("error: you need the cx_freeze package to run the setup() file")

gui_base = None

exe = [Executable("install.py",
                 target_name="Installer.exe")]

setup(name="Control de Agua - Instalador",
      version="1.0.0",
      description="""Esta es una aplicacion para manejar
la venta de garrafones en una base de datos
privada mediante una interfaz simple pero
suficiente para la necesidad del usuario.

Desarrollado por Diego Ramirez <dr01191115@gmail.com> (@DiddiLeija en GitHub)""",
      executables=exe)
