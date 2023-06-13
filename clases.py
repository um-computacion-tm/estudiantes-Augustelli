class Universidad:
    def __init__(self, facultad, rector) -> None:
        self.facultad = facultad
        self.rector = rector
        self.carreras = list()  # Se Inicializar con valores de las carreras
        self.cantidad_carreras = len(self.carreras)


class Profesores():
    def __init__(self, nombre, apellido, email, edad,):
        self.nombre = nombre
        self.apellido = apellido
        self. email = email
        self. asistencia = 0
        self. edad = edad

    def cambiar_nombre_profesor(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_apellido_profesor(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def profesor_asiste_clase(self):
        self.asistencia += 1


class Alumnos():
    def __init__(self, nombre, apellido, dni, carrera, estado, sexo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.carrera = carrera
        self.estado = estado
        self.sexo = sexo

    def cambiar_nombre_alumno(self, nuevo_nombre):
        self.nombre = nuevo_nombre


class Materias():

    def __init__(self, nombre, codigo, dictada_por, facultad, carreras) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.dictada_por = dictada_por
        self.facultad = facultad
        self.carreras = carreras

    def cambiar_profesor(self, nuevo_profesor):
        self.dictada_por = nuevo_profesor

    def cambiar_nombre_materia(self, nuevo_nombre):
        self.nombre = nuevo_nombre


