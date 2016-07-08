import MySQLdb as mdb
import sys
from time import gmtime, strftime

def query(sql):
    try:
        con = mdb.connect('localhost', 'root', 'allemant', 'neointelperu_apps');

        cur = con.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        return rows
    except mdb.Error, e:
        
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    
    finally:
    
        if con:    
            con.close()

def rangoFechas():
    """
    devuelve un listado anio-mes, desde hace N Meses
    hasta la fecha actual, soporta hasta 11 meses
    """
    anio = int(strftime("%Y", gmtime()))
    mes = int(strftime("%m", gmtime()))
    l = []
    for x in [0]:
        
        diff = mes - x
        if diff <= 0:
            l.append([anio - 1, 12+ diff])
        else:
            l.append([anio, diff])
    return l
    
def getReporte01():
    ou = {}
    l = rangoFechas()
    
    sql = ''
    for f in l:
        fecha = '%s-%02d' % (f[0], f[1])
        if sql != '':
            sql +=' UNION '
        sql += '(SELECT d.estado, e.nombre estado_nombre, count(d.id) total, "' + fecha + '" anio_mes '
        sql += 'FROM venta_campania_001 d '
        sql += 'JOIN venta v ON v.id=d.id '
        sql += 'JOIN venta_estado e ON e.id = d.estado '
        sql += 'WHERE v.info_create_fecha >="' + fecha + '-01 00:00:00" AND '
        sql += 'v.info_create_fecha <="' + fecha + '-31 23:59:59" AND '
        sql += 'v.info_status=1 AND ' 
        sql += 'd.aprobado_supervisor = 1 AND '
        sql += 'd.tramitacion_venta_validar = 1 AND '
        sql += 'd.tramitacion_venta_cargar = 1 '
        sql += 'GROUP by 1)'
    # print sql
    ou['estados'] = query(sql)

    sql = ''
    for f in l:
        fecha = '%s-%02d' % (f[0], f[1])
        if sql != '':
            sql +=' UNION '

        sql += '(SELECT d.estado_real, er.nombre estado_real_nombre, er.estado_id, count(d.id) total, "' + fecha + '" anio_mes '
        sql += 'FROM venta_campania_001 d '
        sql += 'JOIN venta v ON v.id=d.id '
        sql += 'JOIN venta_estado_real er ON er.id = d.estado_real '
        sql += 'JOIN venta_estado e ON e.id = er.estado_id '
        sql += 'WHERE v.info_create_fecha >="' + fecha + '-01 00:00:00" AND '
        sql += '      v.info_create_fecha <="' + fecha + '-31 23:59:59" AND '                      
        sql += '      v.info_status=1 AND '
        sql += '      d.aprobado_supervisor = 1 AND '
        sql += '      d.tramitacion_venta_validar = 1 AND '
        sql += '      d.tramitacion_venta_cargar = 1 '
        sql += 'GROUP by 1)'
    # print sql
    ou['estados_reales'] = query(sql)
    return ou

