
from ast import Pass
import json
from model.Contacto import Contacto

class Agenda:

    def __int__(self):
        self.agenda = {"Contacto": []}

    def agregar_contactos(self, nombre, categoria, numero):
        Contactos = Contacto
        lista = []
        lista.append(Contactos(nombre, categoria, numero))
        self.agenda["Contacto"] = lista

        

    def __str__(self) -> str:
        return json.dump(self.__dict__)
