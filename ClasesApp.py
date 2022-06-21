#Modulo para crear las diferentes clases a utilizar en la aplicacion

class Materia:
    """Clase asociada a la entidad Materia
    """
  
    def __init__(self, datos:list) -> None:
        """Constructor de la clase materia

        Args:
            datos (list): La lista con los datos de la materia
        """

        self.__id = datos[0]
        self.__materia = datos[1]
        self.__ciclo = datos[2]
        self.__creditos = datos[3]
        
    
    def __str__(self) -> str:
        """Retorna la cadena representativa de la clase materia

        Returns:
            str: La cadena representativa de la clase materia conformada por su id y su nombre
        """
        return self.__id+":"+self.__materia

    '''
    Getters
    '''
    
    @property
    def id(self)->str:
        """Retorna la id de la materia
        Returns:
            str: la id de la materia
        """
        return self.__id 
    
    @property
    def materia(self)->str:
        """Retorna el nombre de la materia

        Returns:
            str: El nombre de la materia
        """
        return self.__materia 
    
    @property
    def ciclo(self)->str:
        """Retorna el ciclo de la materia

        Returns:
            str: El ciclo de la materia
        """
        return self.__ciclo
    
    @property
    def creditos(self)->str:
        """Retorna el numero de creditos de la materia

        Returns:
            str: El numero de creditos de la materia
        """
        return self.__creditos  

    '''
    Setters
    '''

    @materia.setter
    def materia(self,materia:str)->None:
        """Actualiza el nombre de la materia

        Args:
            materia (str): El nuevo nombre de la materia
        """
        self.__materia=materia    

    @ciclo.setter
    def ciclo(self, ciclo:str)->None:
        """Actualiza el ciclo de la materia

        Args:
            ciclo (str): El nuevo ciclo de la materia
        """
        self.__ciclo=ciclo
    
    @creditos.setter
    def creditos(self, creditos:str)->None:
        """Actualiza el numero de creditos e la materia

        Args:
            creditos (str): El nuevo numero de creditos de la materia
        """
        self.__creditos=creditos

#------------------------------------------------------------------------------------------------------------------------------------------------  

class Profesor:
    """Clase asociada a la entidad profesor
    """
  
    def __init__(self, datos:list) -> None:
        """Constructor de la clase profesor

        Args:
            datos (_type_): Los datos del profesor
        """

        self.__id = datos[0]
        self.__nombre = datos[1]
        self.__materias = datos[2]
    
    def __str__(self) -> str:
        """Cadena representativa de la clase Profesor

        Returns:
            str: La cadena representativa de la clase profesor conformada por su id y nombre
        """
        return self.__id+":"+self.__nombre
        
    '''
    Getters
    '''
    
    @property
    def id(self)->str:
        """Retorna la id del profesor
        Returns:
            str: la id del profesor
        """
        return self.__id
    
    @property
    def nombre(self)->str:
        """Retorna el nombre del profesor

        Returns:
            str: El nombre del profesor
        """
        return self.__nombre
    
    @property
    def materias(self)->list[str]:
        """Retorna la lista de id de materias que puede dictar el profesor

        Returns:
            list[str]: La lista de materias que puede dictar el profesor
        """
        return self.__materias
    
    '''
    Setters
    '''
    
    @nombre.setter
    def nombre(self, nombre:str)->None:
        """Actualiza el nombre del profeslor

        Args:
            nombre (str): El nuevo nombre del profesor
        """
        self.__nombre=nombre

    @materias.setter
    def materias(self, materias:list[str])->None:
        """Actualiza la lista de id de materias que puede dictar el profesor

        Args:
            materias (list[str]): La nueva lista de materias que puede dictar el profesor
        """
        self.__materias=materias    

#------------------------------------------------------------------------------------------------------------------------------------------------

class Grupo:
    """Clase asociada a la entidad grupo
    """
    
    def __init__(self, datos:list) -> None:
        """Constructor de la clase gruo

        Args:
            datos (list): La lista de datos del grupo
        """
        self.__id = datos[0]
        self.__periodo = datos[1]
        self.__horario = datos[2]
        self.__activo = datos[3]
        self.__materias = datos[4]
        self.__profesores = datos[5]
    
    def __str__(self) -> str:
        """Retorna la cadena representativa de la clase grupo 

        Returns:
            str: La cadena representativa de la clase grupo conformada por su id, periodo, horario y su estado de activación
        """
        return self.__id+":"+self.__periodo+":"+self.__horario+":"+("activo" if self.__activo==1 else "inactivo")
        
    '''
    Getters
    '''
    
    @property
    def id(self)->str:
        """Retorna la id del grupo
        Returns:
            str: la id del grupo
        """
        return self.__id

    @property
    def periodo(self)->str:
        """Retorna el periodo del grupo
        Returns:
            str: El periodo del grupo
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
    def activo(self)->str:
        """Retorna si el grupo esta activo o no
        Returns:
            str: 1 si el grupo está activo, 0 si no lo está 
        """
        return self.__activo
    
    @property
    def materias(self)->list[Materia]:
        """La lista de materias del grupo

        Returns:
            list[Materia]: La lista de materias del grupo
        """
        return self.__materias

    @property
    def profesores(self)->list[Profesor]:
        """Retorna la lista de profesores del grupo

        Returns:
            list[Profesor]: La lista de profesores del grupo
        """
        return self.__profesores
    
    '''
    Setters
    '''

    @periodo.setter
    def periodo(self,periodo:str)->None:
        """Actualiza el periodo del grupo
        Args:
            periodo (str): El nuevo periodo del grupo
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
    def activo(self, activo:str)->None:
        """Actualiza el estado de vigencia del grupo
        Args:
            activo (str): El nuevo estado de vigencia del grupo (activo:1, inactivo:0)
        """
        self.__activo=activo
    
    @materias.setter
    def materias(self, materias:list[Materia])->None:
        """Actualiza la lista de materias del grupo

        Args:
            materias (list[Materia]): La nueva lista de materias del grupo
        """
        self.__materias=materias
    
    @profesores.setter
    def profesores(self, profesores:list[Profesor])->None:
        """Actualiza la lista de profesores del grupo

        Args:
            profesores (list[Profesor]): La nueva lista de profesores del grupo
        """ 
        self.__profesores=profesores
        
#------------------------------------------------------------------------------------------------------------------------------------------------ 

class Estudiante:
    """Clase asociada a la entidad estudiante
    
    En python todos los atributos asociados a un objeto son publicos (esto es que pueden ser accedidos desde cualquier parte del código)
    para limitar su uso directo y que solo puedan ser consultados/modificados a traves de los métodos de la clase en python se usa el mecanismo
    llamado name mangling(Self.__<nombreatributo>) que permite simular la propiedad de privados a los atributos. 
    Esta es la forma más cercana de realizar encapsulamiento en python
    """
    
    def __init__(self,datos:list) -> None:
        """Constructor de la clase estudiante

        Args:
            datos (list): Lista con los datos del estudiante que vienen desde el dataframe
        """
        self.__id = datos[0]
        self.__nombres = datos[1]
        self.__apellidos = datos[2]
        self.__email = datos[3]
        self.__grupo = datos[4]

    def __str__(self) -> str:
        """El método str define la manera en como se muestra un objeto al momento de imprimirlo a convertirlo a string
        Al redefinirlo de esta manera se indica que en vez de mostrar algo como objet at 02x0ax00x, muestra la id y los apellidos
        del estudiante

        Returns:
            str: La cadena que representa al objeto
        """
        return self.__id+":"+self.__nombres+" "+self.__apellidos
    
    '''
    Getters
    Son métodos que permiten acceder o consultar los atributos de una clase
    
    Las expresiones que comienzan con @ se llaman decoradores, los decoradores en python definen cierto comportamiento para el método o atributo 
    que acompaña. El decorador property le indica a python que este método deberá ser tratado como un atributo, especificamente uno de 
    lectura para estos metodos.
    Los métodos getters deben tener el nombre del atributo que retorna
    '''
    
    @property
    def id(self)->str:
        """Retorna la id del estudiante
        Returns:
            str: la id del estudiante
        """
        return self.__id
    
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
    def grupo(self)->Grupo:
        """Retorna el grupo al que pertenece el estudiante
        Returns:
            str: El grupo al que pertenece el estudiante
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
    def grupo(self, grupo:Grupo )-> None:
        """Actualiza el grupo del estudiante
        Args:
            grupo (str): El nuevo grupo del estudiante
        """
        self.__grupo = grupo 
        
#------------------------------------------------------------------------------------------------------------------------------------------------

class Nota:
    """Clase asociada a la entidad nota
    """
    def __init__(self, datos:list) -> None:
        """Constructor de la clase nota

        Args:
            datos (list): La lista de datos de la nota
        """
        self.__id = datos[0]
        self.__estudiante = datos[1]
        self.__nota = datos[2]
        self.__materia = datos[3]
    
    def __str__(self) -> str:
        """Cadena representativa de la clase nota

        Returns:
            str: La cadena representativa de la clase nota conformada por su id, estudiante y materia
        """
        return self.__id+":"+str(self.__estudiante)+":"+str(self.__materia)
        
    '''
    Getters
    '''
    
    @property
    def id(self)->str:
        """Retorna la id del profesor
        Returns:
            str: la id del profesor
        """
        return self.__id

    @property
    def estudiante(self)->Estudiante:
        """Retorna el estudiante asociado a la nota

        Returns:
            Estudiante: El estudiante asociado a la nota
        """
        return self.__estudiante
    
    @property
    def nota(self)->str:
        """Retorna la calificación númerica asociada a la nota

        Returns:
            str: _description_
        """
        return self.__nota

    @property
    def materia(self)->Materia:
        """Retorna la materia asociada a la nota

        Returns:
            Materia: La materia asociada a la nota
        """
        return self.__materia
    
    '''
    Setters
    '''
    
    @estudiante.setter
    def estudiante(self, estudiante:Estudiante)->None:
        """Actualiza el estudiante asociado a la nota

        Args:
            estudiante (Estudiante): El nuevo estudiantes asociado a la nota
        """
        self.__estudiante=estudiante
    
    @nota.setter
    def nota(self, nota:str)->None:
        """Actualiza la calificación numerica asociada a la nota

        Args:
            nota (str): La nueva calificación numérica de la nota
        """
        self.__nota=nota

    @materia.setter
    def materia(self, materia:Materia)->None:
        """Actualiza la materia asociada a la nota

        Args:
            materia (Materia): La nueva materia asociada a la nota
        """
        self.__materia=materia
        