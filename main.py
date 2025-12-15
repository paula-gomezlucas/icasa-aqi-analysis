from logica import logica
from usuario import usuario
from localizacion import localizacion


def main():
    login = False
    user: usuario
    opcion = -1
    loc1 = localizacion(40.387423435579784, -3.675099906410683, 'Casita adosada en Puente de Vallecas')
    loc2 = localizacion(40.43310826724064, -3.7597656491229396, 'Piso en Casa de Campo con vistas hermosas')
    loc3 = localizacion(40.47834830891741, -3.8665659966154946, 'Apartamento con terraza y dos baños - Majadahonda')
    loc4 = localizacion(40.533223146046744, -3.6660390993337515, 'Chalet con piscina, Alcobendas')
    loc5 = localizacion(40.31591200991959, -3.7186984691387597, 'Dúplex amueblado en Getafe')
    loc6 = localizacion(40.32917857284654, -3.490400787506039, 'Piso Rivas-Vaciamadrid')
    loc7 = localizacion(40.41739245776822, -3.689849859286296, 'Estudio sin amueblar en el Retiro')
    loc8 = localizacion(40.44673432028439, -3.485585368358161, 'Chalet con sótano al lado del cementerio - Torrejón de Ardoz')
    loc9 = localizacion(40.36944865202632, -4.409118694562305, 'Casa Rural - San Martín de Valdeiglesias')
    loc10 = localizacion(40.905401924608555, -3.8799728077644047, 'Chalet unifamiliar en Rascafría')
    localizaciones = [loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9, loc10]
    localizaciones = logica.zona_ica(localizaciones)

    while not login:
        email = input('Introduzca email: ')
        passw = input('Introduzca contraseña: ')
        user = usuario(None, passw, email, None)
        login = bool(usuario.acceder(user))

    while opcion != 0 and login:
        if user.esGestor:
            respuesta = input("¿Quieres consultar los datos de los usuarios(y/n)?")
            if respuesta == 'y':
                fila = input("Introduce el email del usuario cuyos datos quieres consultar\n")
                for e in usuario.accesoBBDD(user, fila):
                    print(e)
        log = logica()
        opcion = int(input("Elige región: \n1.Madrid\n2.Valencia\n3.Volver\n0.Logout\n"))
        if opcion == 1:
            logica.que_region(log, 'https://www.idealista.com/venta-viviendas/madrid')
            print('Hemos encontrado estas viviendas, con los siguientes ICA correspondientes: \n')
            for loc in localizaciones:
                print(loc)
        elif opcion == 2:
            logica.que_region(log, 'https://www.idealista.com/venta-viviendas/valencia')
            print('Hemos encontrado estas viviendas, con los siguientes ICA correspondientes: \n')
            for loc in localizaciones:
                print(loc)
        else:
            pass


if __name__ == '__main__':
    main()
