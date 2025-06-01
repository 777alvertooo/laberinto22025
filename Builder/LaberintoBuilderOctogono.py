from Builder.LaberintoBuilder import LaberintoBuilder
from Formas.Octogono import Octogono



class LaberintoBuilderOctogono(LaberintoBuilder):

    def fabricarFormaEspecifica(self, forma_str: str):
        forma_str_lower = forma_str.lower().strip()
        forma_obj = None

        if forma_str_lower == "octogono":
            print(f"BUILDER: Fabricando forma Octogono (especificada como '{forma_str}').")
            forma_obj = Octogono()
        else:
            print(f"BUILDER WARN: Forma '{forma_str}' desconocida o no implementada. Usando Octogono por defecto.")
            forma_obj = Octogono() 
        if forma_obj and hasattr(forma_obj, 'agregarOrientacion'):
            forma_obj.agregarOrientacion(self.fabricarNorte())
            forma_obj.agregarOrientacion(self.fabricarSur())
            forma_obj.agregarOrientacion(self.fabricarEste())
            forma_obj.agregarOrientacion(self.fabricarOeste())
            forma_obj.agregarOrientacion(self.fabricarNoreste())
            forma_obj.agregarOrientacion(self.fabricarNoroeste())
            forma_obj.agregarOrientacion(self.fabricarSureste())
            forma_obj.agregarOrientacion(self.fabricarSuroeste())
        elif forma_obj:
            print(f"BUILDER ERROR: La forma '{type(forma_obj).__name__}' creada no tiene método 'agregarOrientacion'.")
        else:
            print(f"BUILDER ERROR CRÍTICO: No se pudo crear un objeto forma. Creando Octogono vacío.")
            return Octogono() 

        return forma_obj
    
    def obtenerObjeto(self, cadena_orientacion: str): 
        obj = None
        cadena_lower = cadena_orientacion.lower().strip()
        if cadena_lower == 'norte': obj = self.fabricarNorte()
        elif cadena_lower == 'sur': obj = self.fabricarSur()
        elif cadena_lower == 'este': obj = self.fabricarEste()
        elif cadena_lower == 'oeste': obj = self.fabricarOeste()
        elif cadena_lower == 'noreste': obj = self.fabricarNoreste()
        elif cadena_lower == 'noroeste': obj = self.fabricarNoroeste()
        elif cadena_lower == 'sureste': obj = self.fabricarSureste()
        elif cadena_lower == 'suroeste': obj = self.fabricarSuroeste()
        else: print(f"BUILDER WARN: Orientación '{cadena_orientacion}' desconocida en obtenerObjeto.")
        return obj