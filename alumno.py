
class Alumno:
    def __init__(self, nombre, nota):
     self.nombre = nombre
     self.nota = nota

    def notas(self):
        print("El alumno: ", self.nombre,".", "Tiene la sigueinte calificacion", self.nota)
        return

n = Alumno("Diego", 9)
n.notas()
n2 = Alumno("Zory", 10)
n2.notas()


