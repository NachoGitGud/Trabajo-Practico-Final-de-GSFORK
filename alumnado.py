from alumno import Alumno

class Alumnado:
    #Inicializa el anotador con una lista de alumnos
    def __init__(self, lista_alumnos = []):
        self.lista_alumnos = lista_alumnos

    #Metodo para agregar un nuevo alumno
    def nuevo_alumno(self, nombre, apellido, nivel, grado):
        alumno = Alumno(nombre, apellido, nivel, grado)
        self.lista_alumnos.append(alumno)
        return alumno
    
    #Busca el alumno con el nombre y apellido dado
    def buscar_por_nombre_apellido(self, nombre_apellido_buscar):
        a = []
        for un_alumno in self.lista_alumnos:
            if un_alumno.coincide(nombre_apellido_buscar):
                a.append(un_alumno)
        return a
    
   #Busca el alumno con el nivel dado
    def buscar_por_nivel(self, buscar_nivel):
        b = []
        for un_alumno in self.lista_alumnos:
           if un_alumno.nivel == buscar_nivel:
            return un_alumno
        return b

    #Busca el alumno con el grado dado
    def buscar_por_grado(self, buscar_grado):
        c = []
        for un_alumno in self.lista_alumnos:
            if un_alumno.grado == buscar_grado:
                return un_alumno
        return c

    #Metodo para modificar el nivel de un alumno buscando por nombre y apellido
    def modificar_alumno(self, nombre_apellido_buscar, nivel):
        alumno = self.buscar_por_nombre_apellido(nombre_apellido_buscar)
        if alumno:
            alumno.nivel = nivel
            return True
        return False

    #Metodo para modificar el grado de un alumno buscando por nombre y apellido
    def modificar_grado(self, nombre_apellido_buscar, grado):
        alumno = self.buscar_por_nombre_apellido(nombre_apellido_buscar)
        if alumno:
            alumno.grado = grado
            return True
        return False

    #Metodo para modificar el grado de un alumno buscando por nombre y apellido
    def modificar_nivel(self, nombre_apellido_buscar, nivel):
        alumno = self.buscar_por_nombre_apellido(nombre_apellido_buscar)
        if alumno:
            alumno.nivel = nivel
            return True
        return False    

    #Metodo que busca los alumnos que coincidan con el filtro dado
    def buscar(self, filtro):
        return [ alumno for alumno in self.lista_alumnos if alumno.coincide_filtro(filtro) ]

    #Metodo para eliminar un alumno buscando por nombre y apellido
    def eliminar_alumno(self, id_alumno):
        alumno = None
        for a in self.lista_alumnos:
            if a.id == id_alumno:
                alumno = a                      
        if alumno:
            self.lista_alumnos.remove(alumno)
            return True
        return False
