#public class Usuario{}
class Pokemon:
    
    #public Pokemon(parametros):{}
    def __init__(self,id,nombre,especie,tipo,foto,passw):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.tipo = tipo
        self.foto = foto
        self.passw = passw
        #print("Este es el constructor")

    def imprimir_tipo(self):
        print(self.nombre + ' es de tipo ' + self.tipo)

    def autenticar(self,nombre,passw):

        if self.nombre == nombre and self.passw == passw:

            print('La autentificación es correcta')
            return True
        print('La autentificación es incorrecta')
        return False