class localizacion:
    def __init__(self, lat, lng, nombre):
        self.lat = lat
        self.lng = lng
        self.nombre = nombre
        self.ica = None

    def __str__(self):
        return f"{self.ica} {self.nombre}"
