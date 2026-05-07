from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4
import re

from exceptions import DatosInvalidosError

class EntidadSistema(ABC):
    def __init__(self, nombre):
        self._id = str(uuid4())[:8]
        self._fecha_creacion = datetime.now()
        self.nombre = nombre
        
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosError(
                f'El nombre debe ser una cadena de más de 3 caracteres. Recibido: {valor}'
            ) 
        self._nombre = valor.strip()
        
    @abstractmethod
    def resumen(self):
        pass
    

class Cliente(EntidadSistema):
    def __init__(self, nombre, documento, correo, telefono):
        super().__init__(nombre)
        self.documento = documento
        self.correo = correo
        self.telefono = telefono
        
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, valor):
        if not isinstance(valor, str) or not valor.isdigit() or len(valor) < 6:   
            raise DatosInvalidosError(
                f'El documento debe ser numerico y minimo 6 digitos. Recibido: {valor}'
            ) 
        self._documento = valor
        
    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, valor):
        patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise DatosInvalidosError(
                f'El correo debe ser una dirección de correo válida. Recibido: {valor}'
            )
        self._correo = valor.lower()
        
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.isdigit() or len(valor) < 7:
            raise DatosInvalidosError(
                f'El telefono debe ser numerico y minimo 7 digitos. Recibido: {valor}'
            )
        self._telefono = valor
        
    def resumen(self):
        return {
            f"Cliente: {self.nombre} - Documento: {self.documento} - Correo: {self.correo} - Telefono: {self.telefono}"
        }