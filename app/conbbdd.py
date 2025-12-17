import sys
import mariadb


class conbbdd:

    @staticmethod
    def conectar(servidor, bbdd, usuario, passw):
        try:
            mydb = mariadb.connect(
                host=servidor,
                user=usuario,
                password=passw,
                database=bbdd
            )
            return mydb
        except mariadb.Error as e:
            sys.exit(1)
            return e

    @staticmethod
    def queryBBDD(mydb, sentencia_sql, retorno: bool, insert: bool):
        cursor = mydb.cursor()
        cursor.execute(sentencia_sql)
        if retorno:
            myquery = cursor.fetchall()
            if insert:
                mydb.commit()
            cursor.close()
            return myquery
        
        else:
            mydb.commit()
            cursor.close()
            return None
        

        
    @staticmethod
    def modificarBBDD(mydb, sentencia_sql):
        cursor = mydb.cursor()
        cursor.execute(sentencia_sql)
        cursor.close()

    @staticmethod
    def desconectar(mydb):
        mydb.close()
