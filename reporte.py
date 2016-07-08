#!/usr/bin/python

import os, logging
import modelo
import vista

# url = '192.168.1.4/ruta.php?'
url = ' neointel-001-site1.ctempurl.com/Reporte/GetReportData'
# url = 'neointel-001-site1.ctempurl.com/Reporte/GetReportData?'

# fichero_log = './test.log'
# logging.basicConfig (
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename = fichero_log,
#     filemode = 'w',)

cadena = '';
reporte01 = modelo.getReporte01()
cadena = '{' + vista.imprimirReporte01(reporte01) + '}'

# print cadena

cadena = cadena.replace('"','_c_')      
cadena = cadena.replace(' ','_e_')
cadena = cadena.replace('{','_li_')
cadena = cadena.replace('}','_lf_')
cadena = cadena.replace('[','_ri_')
cadena = cadena.replace(']','_rf_')

# print cadena
# print '-----------------------'
mm = 'wget -P /home/neointel/script/reporte_a_nube/download/ '+url+'?datos=' + cadena 
# mm = 'wget '+url+'datos=' + cadena
os.system(mm)
# os.system('rm ruta.php?datos*')
logging.info('Enviando Datos')
print mm
