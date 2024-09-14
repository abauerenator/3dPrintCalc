# 3dPrintCalc
Very simple Python script to calculate 3D printing cost and final price.

Calculadora de costos de impresion y precio de venta, que incluye todos los factores necesarios para un calculo preciso.
Rellenar cada campo segun sea necesario. 

- Se tiene en cuenta posibles fallos en las impresiones.
- Costo electrico.
- Costo de material.
- Costo de mano de obra si corresponde.
- Amotizacion de la maquina.
- impuestos.
- costos de embalaje.
- costos de envio.
- En el resultado obtenemos costo total de manofactura
- Ganacia neta
- Precio de venta, con y sin impuestos.

![Screenshot 2024-09-13 214338](https://github.com/user-attachments/assets/a8bb2f8f-5896-4ab6-bd74-acecf55bc57d)

# Como usar: 
- Descargar el codigo en zip.
- Descomprimir en una carpeta.
- Abrir una linea de comandos CMD desde esta carpeta
- intalar todas las dependencias con: pip install -r requirements.txt o sudo pip3 install -r requirements.txt
- Ejecutar el archivo 3dPrintCalc.bat en windows 
- En linux hacer chmod +x 3dPrintCalc.sh y luego ejecutar con 3dPrintCalc.sh

# requerimentos 
- python 3.9 +
- ver requirements.txt

# NOTA:
- La cotizacion del dolar se obtiene desde dolarhoy - dato solo en caracter informativo para argentina.
  no tiene efecto en los calculos.
