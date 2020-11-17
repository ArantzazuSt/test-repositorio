
from opendaq import *
import argparse
import json


parser = argparse.ArgumentParser(description = 'Leer las salidas analogicas fijando un valor de entrada')

parser.add_argument('-p','--port', metavar='',required=True, default='/dev/ttyUSB0', help= 'Serial port (default: /dev/ttyUSB0)')
parser.add_argument('-e','--input', metavar='', required=True,help= 'entradas seleccionadas')
parser.add_argument('-r', '--rep', metavar='', required=True, help='numero de repeticiones')
parser.add_argument('-j', '--JSON', metavar='',help= 'generar un archivo JSON')
args = parser.parse_args()


#   def create_test_json(self, results_input, results_outputs):
#   filename = '%s_%s_test.json' % (self.serial_str, time.strftime ('%y%m%d'))
#   
#   f = open(filename, 'w')
#   data = {
#       "model": self.hw_ver,
#       "serial": self.serial,
#       "time": int(time.time()),
#       "items": []
#   }


#Generar el archivo JSON
#   json.dump(data, f, indent= 2)
#   f.close()

if __name__ == '__main__':
    print ("El puerto escogido es %s, entrada %s y numero de repeticoines: %s") % (args.port, args.input, args.rep)