from conbbdd import conbbdd


class logica:
    def __init__(self):
        self.esVivienda = True  # En esta versión, sólo accesible a viviendas en idealista
        self.IDregion = None
        self.lector = None
        #  self.rangoTiempo = None

    def que_region(self, url):
        if self.esVivienda:
            if 'madrid' in url:
                self.IDregion = 'Madrid'
            elif 'valencia' or 'alicante' or 'castellon' in url:
                self.IDregion = 'Valencia'

        else:  # ESCALABLE A VISITAS VACACIONALES
            pass

    #  def que_pagina_web(self, url):
    #    if 'https://www.idealista.com/' in url:
    #        self.esVivienda = True
    #    elif 'https://www.trivago.es/' in url:
    #        self.esVivienda = False
    #    else:
    #        pass

    @staticmethod
    def zona_ica(localizaciones):

        for loc in localizaciones:
            query = '''SELECT mediaica FROM (SELECT mediaica, SQRT(\
            POW(69.1 * (latitud - {startlat}), 2) +\
            POW(69.1 * ({startlng} - longitud) * COS(latitud / 57.3), 2))\
            AS distance FROM LOCALIZACION ORDER BY distance LIMIT 1)\
            AS SUBQ;'''.format(startlat=loc.lat, startlng=loc.lng)

            mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
            loc.ica = conbbdd.queryBBDD(mydb, query)[0][0]
            conbbdd.desconectar(mydb)

        return localizaciones

    #  FUTURAS LÍNEAS DE TRABAJO
    #  def rango_tiempo(self, inicio, fin):
    #    if self.esVivienda:
    #       pass
    #   else -> guardarlo en rangoTiempo
