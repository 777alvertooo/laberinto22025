
from abc import ABC, abstractmethod
from typing import  Optional, List  
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Juego.Juego import Juego
class Comando(ABC):
    @abstractmethod
    def ejecutar(self, juego: 'Juego', args: List[str]) -> Optional[str]:
        pass