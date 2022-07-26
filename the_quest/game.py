import os

import pygame as pg

from the_quest import ALTO, ANCHO
from the_quest.escenas import Portada, Levelone, Leveltwo, Records

class the_quest:
    def __init__(self) -> None:
        print("Comienza el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("The Quest")

        self.escenas = [
            Portada(self.display),
            Levelone(self.display),
            Leveltwo(self.display),
            Records(self.display)
        ]

    def jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()

