#Modulo para crear las diferentes classes a utilizar en la aplicacion

class Materia:
    #Clase asociada a la entidad Materias   
  
    def __init__(self, listadatos: list) -> None:
        '''
        Args:
            listadatos: debe tener la informacion en el siguiente orden:
            IDMateria (int): Id de la Materia de estudio
            Materia (str): Nombres de la Materia de estudio
            Ciclo (int): Ciclo al que pertenece la materia entre 1 y 4
            Creditos (int): Cantidad de creditos
            
        '''
        self.IDMateria = listadatos[0]
        self.Materia = listadatos[1]
        self.Ciclo = listadatos[2]
        self.Creditos = listadatos[3]



    '''
    Getters
    '''
    def listadatos(self):
        return [self.IDMateria,
        self.Materia, 
        self.Ciclo,
        self.Creditos]
    '''
    Setters
    '''
#------------------------------------------------------------------------------------------------------------------------------------------------

class Profesor:
    '''Clase asociada a la entidad Materias
    '''
  
    def __init__(self, listadatos: list) -> None:
        '''
        Args:
            listadatos: debe tener la informacion en el siguiente orden:
                IDProf (str): Id del profesor inicia con la letra P y luego un numero consecutivo
                Nombr (str): Nombres y Apellidos del profesor
                Materi (list): Lista con codigos de materias que dicta el profesor
        '''

        self.IDProfesor = listadatos[0]
        self.Nombre = listadatos[1]
        self.Materias = listadatos[2]
        

    '''
    Getters
    '''

    '''
    Setters
    '''

#------------------------------------------------------------------------------------------------------------------------------------------------


class Estudiante:
    """Clase asociada a la entidad estudiante
    
    En python todos los atributos asociados a un objeto son publicos (esto es que pueden ser accedidos desde cualquier parte del código)
    para limitar su uso directo y que solo puedan ser consultados/modificados a traves de los métodos de la clase en python se usa el mecanismo
    llamado name mangling(Self.__<nombreatributo>) que permite simular la propiedad de privados a los atributos. 
    Esta es la forma más cercana de realizar encapsulamiento en python
    """
    
    def __init__(self, listadatos: list) -> None:
        """Constructor de la clase estudiante que recibe, id, nombres, apellidos, email y grupo
        Args:
        listadatos: debe tener la informacion en el siguiente orden:    
            idEstudiante (int): Id del estudiante
            nombres (str): Nombres del estudiante
            apellidos (str): Apellidos del estudiante
            email (str): Email del estudiante
            grupo (int): Grupo del estudiante
            
        """
        self._IDEstudiante = listadatos[0]
        self.__nombres = listadatos[1]
        self.__apellidos = listadatos[2]
        self.__email = listadatos[3]
        self.__grupo = listadatos[4]

    '''
    Getters
    Son métodos que permiten acceder o consultar los atributos de una clase
    
    Las expresiones que comienzan con @ se llaman decoradores, los decoradores en python definen cierto comportamiento para el método o atributo 
    que acompaña. El decorador property le indica a python que este método deberá ser tratado como un atributo, especificamente uno de 
    lectura para estos metodos.
    Los métodos getters deben tener el nombre del atributo que retorna
    '''
    
    @property
    def IDEstudiante(self)->int:
        """Retorna la id del estudiante
        Returns:
            int: la id del estudiante
        """
        return self._IDEstudiante
    
    @property
    def nombres(self)->str:
        """Retorna los nombres del estudiante
        Returns:
            str: Los nombres del estudiante
        """
        return self.__nombres  

    @property
    def apellidos(self)->str:
        """Retorna los apellidos del estudiante
        Returns:
            str: Los apellidos del estudiante
        """
        return self.__apellidos 
    
    @property
    def email(self)->str:
        """Retorna el correo del estudiante
        Returns:
            str: El correo del estudiante
        """
        return self.__email 
        
    @property
    def grupo(self)->int:
        """Retorna el grupo al que pertenece el estudiante
        Returns:
            int: El grupo al que pertenece el estudiante
        """
        return self.__grupo
    
    '''
    Setters
    Son métodos que permiten actualizar un atributo
    
    Para los métodos setters se aconseja que tenga el mismo nombre del atributo y se le debe indicar
    el decorador @<nombreatributo>.setter y de manera obligatoria recibe un parámetro para realizar
    la actualización de dicho atributo.
    '''

    @nombres.setter
    def nombres(self,nombres:str)->None:
        """Actualiza el nombre del estudiante
        Args:
            nombres (str): El nuevo nombre del estudiante
        """
        self.__nombres=nombres
        
    @apellidos.setter
    def apellidos(self, apellidos:str )-> None:
        """Actualiza los apellidos del estudiante
        Args:
            apellidos (str): Los nuevos apellidos del estudiante
        """
        self.__apellidos=apellidos
    
    @email.setter
    def email(self, email:str )-> None:
        """Actualiza el correo del estudiante
        Args:
            email (str): El nuevo correo del estudiante
        """
        self.__email = email
    
    @grupo.setter
    def grupo(self, grupo:str )-> None:
        """Actualiza el grupo del estudiante
        Args:
            grupo (str): El nuevo grupo del estudiante
        """
        self.__grupo = grupo 

#------------------------------------------------------------------------------------------------------------------------------------------------

class Grupo:
    """Clase asociada a la entidad grupo
    """
  
    def __init__(self, listadatos: list) -> None:
        '''
        Args:
        listadatos: debe tener la informacion en el siguiente orden:    
            idgrupo (int): Id del grupo
            periodo (int): año de estudio
            horario (str): Franja horaria de estudio
            activo (int):  Estado del grupo: 1 activo / 0 inactivo
            materias (list): Lista de materias a estudiar
            profesores (list): Lista de materias profesores en el mismo orden de las materias
        '''
        self._IDGrupo = listadatos[0]
        self.__periodo = listadatos[1]
        self.__horario = listadatos[2]
        self.__activo = listadatos[3]
        self.__materias = listadatos[4]
        self.__profesores = listadatos[5]
        
    '''
    Getters
    '''
    
    @property
    def IDGrupo(self)->int:
        """Retorna la id del grupo
        Returns:
            int: la id del grupo
        """
        return self._IDGrupo

    @property
    def periodo(self)->int:
        """Retorna el periodo del grupo
        Returns:
            int: El periodo del grupo
        """
        return self.__periodo

    @property
    def horario(self)->str:
        """Retorna el horario del grupo
        Returns:
            str: El horario del grupo
        """
        return self.__horario

    @property
    def activo(self)->int:
        """Retorna si el grupo esta activo o no
        Returns:
            int: 1 si el grupo está activo, 0 si no lo está 
        """
        return self.__activo
    
    @property
    def materias(self)->list:
        """Retorna la lista de materias del grupo
        Returns:
            list: La lista de materias del grupo
        """
        return self.__materias

    @property
    def profesores(self)->list:
        """Retorna la lista de profesores del grupo
        Returns:
            list: La lista de profesores del grupo
        """
        return self.__profesores

    '''
    Setters
    '''

    @periodo.setter
    def periodo(self,periodo:int)->None:
        """Actualiza el periodo del grupo
        Args:
            periodo (int): El nuevo periodo del grupo
        """
        self.__periodo=periodo
        

    @horario.setter
    def horario(self,horario:str)->None:
        """Actualiza el horario del grupo
        Args:
            horario (str): El nuevo horario del grupo
        """
        self.__horario=horario
        
    @activo.setter
    def activo(self, activo:int)->None:
        """Actualiza el estado de vigencia del grupo
        Args:
            activo (int): El nuevo estado de vigencia del grupo (activo:1, inactivo:0)
        """
        self.__activo=activo
    
    @materias.setter
    def materias(self, materias:list)->None:
        """Actualiza la lista de materias del grupo
        Args:
            materias (list): La lista de materias del grupo
        """
        self.__materias=materias
    
    @profesores.setter
    def profesores(self, profesores:list)->None:
        """Actualiza la lista de profesores del grupo
        Args:
            profesores (list): La lista de profesores del grupo
        """
        self.__profesores=profesores
#------------------------------------------------------------------------------------------------------------------------------------------------
