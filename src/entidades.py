import abc

class Entidad(abc.ABC):
    @abc.abstractmethod
    def validar(self):
        pass

    @abc.abstractmethod
    def descripcion(self):
        pass