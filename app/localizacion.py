import requests

from conbbdd import conbbdd


class localizacion:
    def __init__(self, nombre):
        self.lat = None
        self.lng = None
        self.nombre = nombre
        self.ica = None
        self.IDRegion = None

    def __init__(self, address: str, url):

        if 'madrid' in url:
            self.IDRegion = 'Madrid'
        elif 'valencia' or 'alicante' or 'castellon' in url:
            self.IDRegion = 'Valencia'

        url = "https://geocode.maps.co/search?q={address}%20{region}".format(region=self.IDRegion, address=address)
        url2 = "https://geocode.maps.co/search?q={address}%20spain".format(address=address)
        url3 = "https://geocode.maps.co/search?q={address}".format(address=address)
        r = requests.get(url=url)
        data = r.json()

        if data:
            self.lat = float(data[0]['lat'])
            self.lng = float(data[0]['lon'])
        else:
            r2 = requests.get(url=url2)
            data2 = r2.json()
            if data2:
                self.lat = float(data2[0]['lat'])
                self.lng = float(data2[0]['lon'])
            else:
                r3 = requests.get(url=url3)
                data3 = r3.json()
                if data3:
                    self.lat = float(data3[0]['lat'])
                    self.lng = float(data3[0]['lon'])
                else:
                    address = address.split(",")[0]
                    url = "https://geocode.maps.co/search?q={address}%20{region}".format(region=self.IDRegion, address=address)
                    url2 = "https://geocode.maps.co/search?q={address}%20spain".format(address=address)
                    url3 = "https://geocode.maps.co/search?q={address}".format(address=address)
                    r = requests.get(url=url)
                    data = r.json()

                    if data:
                        self.lat = float(data[0]['lat'])
                        self.lng = float(data[0]['lon'])
                    else:
                        self.lat = 200

    
    def __str__(self):
        return f"{self.ica} {self.nombre}"

    def zona_ica(self):

        if self.lat == 200:
            self.ica = -1
        else:
            query = '''SELECT mediaica FROM (SELECT mediaica, SQRT(\
            POW(69.1 * (latitud - {startlat}), 2) +\
            POW(69.1 * ({startlng} - longitud) * COS(latitud / 57.3), 2))\
            AS distance FROM LOCALIZACION ORDER BY distance LIMIT 1)\
            AS SUBQ;'''.format(startlat=self.lat, startlng=self.lng)

            mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
            self.ica = conbbdd.queryBBDD(mydb, query, True, False)[0][0]
            conbbdd.desconectar(mydb)

        return self
