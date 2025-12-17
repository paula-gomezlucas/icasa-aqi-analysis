from conbbdd import conbbdd
import hashlib


class usuario:
    def __init__(self, nombre, passw, email, esGestor):
        self.nombre = nombre
        self.passw = passw
        self.email = email
        self.esGestor = bool(esGestor)

    def acceder(self):
        query = "SELECT EMAIL FROM USUARIO WHERE EMAIL = '{email}' AND ALTA = 1;".format(email=self.email)
        mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
        datos = conbbdd.queryBBDD(mydb, query, True, False)

        if datos:
            comprobarpassw = "SELECT HASHPASS FROM USUARIO WHERE EMAIL = '{email}';".format(email=self.email)
            acceso = conbbdd.queryBBDD(mydb, comprobarpassw, True, False)

            if hashlib.md5(self.passw.encode()).hexdigest() == acceso[0][0]:
                comprobarautorizacion = "SELECT ROL, NOMBRE FROM USUARIO WHERE EMAIL = '{email}';".format(email=self.email)
                lista = conbbdd.queryBBDD(mydb, comprobarautorizacion, True, False)
                self.esGestor = bool(lista[0][0])
                self.nombre = lista[0][1]
                conbbdd.desconectar(mydb)
                return True

            else:
                conbbdd.desconectar(mydb)
                return False

        else:
            conbbdd.desconectar(mydb)
            return False

    def registroBBDD(self):
        query = "SELECT EMAIL FROM USUARIO WHERE EMAIL = '{email}';".format(email=self.email)
        mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
        datos = conbbdd.queryBBDD(mydb, query, True, False)

        if datos:
            conbbdd.desconectar(mydb)
            return False
        else:
            hashpass = hashlib.md5(self.passw.encode()).hexdigest()
            registroUsuario = '''INSERT INTO USUARIO (EMAIL, NOMBRE, HASHPASS, ROL, ALTA)\
                              VALUES ('{email}', '{nombre}', 
                              '{passw}', 0, 1);'''.format(email=self.email, nombre=self.nombre, passw=hashpass)
            conbbdd.queryBBDD(mydb, registroUsuario, False, True)
            return True

    @staticmethod
    def accesoBBDD(email):
        query = "SELECT NOMBRE FROM USUARIO WHERE EMAIL = '{email}';".format(email=email)
        mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
        respuesta = conbbdd.queryBBDD(mydb, query, True, False)
        if respuesta:
            respuesta = respuesta[0][0]
        else:
            respuesta = ""        
        
        conbbdd.desconectar(mydb)
        return respuesta



    def altaBaja(self, email, alta):
        query = "UPDATE USUARIO SET ALTA = {alta} WHERE EMAIL = '{email}';".format(email=email, alta=alta)
        mydb = conbbdd.conectar('195.235.211.197', 'psi_grupo2', 'psi_grupo2', '1234')
        conbbdd.queryBBDD(mydb, query, False, True)
