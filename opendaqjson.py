'''Programa que imprime el valor de las entrads al fijar un valor en la salida '''

import json
import argparse
import time

from opendaq import *


if __name__ == 'main':

    parser = argparse.ArgumentParser(description='Valor de las salidas Opendaq')

    parser.add_argument('-p', '--puerto', metavar='', help='Puerto seleccionado')
    parser.add_argument('-l', '--listInput', nargs='+', metavar='',
                        type=int, help='Entradas seleccionadas')
    parser.add_argument('-r', '--rep', metavar='', type=int,
                        help='Numero de repeticiones')

    args = parser.parse_args()
    daq = DAQ(args.puerto)

    mylist = args.listInput  # Array de entradas a leer

    f = open("prueba.json", 'w')
    data = {
        "model": daq.hw_ver,
        "serial": daq.serial_str,
        "port": args.puerto,
        # "time": int(time.time()),
        "items": []

    }

    for i in mylist:
        data["items"].append({"Input number": i, "readings": daq.read_analog()})
        print(data)

    json.dump(data, f, indent=2)
    f.close()
