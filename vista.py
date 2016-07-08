def validarCadena(cadena):
    # cadena = cadena.decode('latin-1').encode("utf-8")
    cadena = cadena.replace('"', '')
    return cadena
    
def imprimirReporte01(data):
    ou, ou1, ou2 = '', '', ''
    for row in data['estados']:
        if ou1 != '':
            ou1 += ','
        ou1 += '{'
        ou1 += '"id":' + '"' + str(row[0]) + '",'
        ou1 += '"no":' + '"' + validarCadena(row[1]) + '",'
        ou1 += '"ca":' + '"' + str(row[2]) + '",'
        ou1 += '"fe":' + '"' + str(row[3]) + '"'
        ou1 += '}'
    ou1 = '"padre":[' + ou1 + '], '
    for row in data['estados_reales']:
        if ou2 != '':
            ou2 += ','
        ou2 += '{'
        ou2 += '"id":' + '"' + str(row[0]) + '",'
        ou2 += '"no":' + '"' + validarCadena(row[1]) + '",'
        ou2 += '"pa":' + '"' + str(row[3]) + '",'
        ou2 += '"ca":' + '"' + str(row[3]) + '",'
        ou2 += '"fe":' + '"' + str(row[4]) + '"'
        ou2 += '}'
    ou2= '"hijo":[' + ou2 + ']'
    ou = '"reporte01": {' + ou1 + ou2 + '}'
    return ou
    
