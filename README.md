# `installer`
Instalador del producto principal de @ControlDeAgua.

## Método recomendado de uso

Primero, descargue (y/o modifique) el código en formato ZIP (puede buscarlo en https://github.com/ControlDeAgua/ControlDeAgua/releases). Asegúrese de que el archivo
ZIP se llame `Control de Agua-1.0.0.zip` a la hora de correr el instalador. Procure que esté en el mismo directorio que el programa (aplica
lo mismo en caso de ejecutables).

Si desea usar el instalador en ejecutable (y no en Python), puede usar este comando en el mismo directorio que el programa:

```
setup.py build
```

Una vez que haga esto, puede transportar e instalar
el código de `Control de Agua` de varias maneras.

### Instalando en la misma computadora

Puede usar `installer` en la misma computadora en la que lo descargó, con Python o con ejecutable (`.exe`). Para usar Python,
busque el archivo `installer.py`; y para usar el ejecutable, busque `Installer.exe` en el directorio `build`.

### Transportar el código

Puede pasar el código de una computadora a otra con `installer`. Pase la carpeta que lo contiene (y que contiene el ZIP) a una unidad de USB. Luego
introduzca la unidad en otro ordenador. Luego, instale con normalidad desde la USB. Finalmente, extraiga la unidad.

De esta forma, usted puede tener un solo `installer` para subir diversas copias de `Control de Agua`.

## Notas

- Al igual que `Control de Agua`, `installer` solo está disponible para computadoras Windows.
- Si desea correr los archivos en Python, deberá instalar Python 3.6 o superior.
