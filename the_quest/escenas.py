import os

import pygame as pg

from . import ALTO, ANCHO, COLOR_TITULO, COLOR_INSTRUCCIONES

class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
       super().__init__(pantalla)

       font_file_titulo = os.path.join("resources", "fuentes", "SIXTY.TTF")
       self.tipografia = pg.font.Font(font_file_titulo, 120)
    """Preguntar lo de las tipografías"""
       #font_file_instrucciones = os.path.join("resources", "fuentes", "leadcoat.ttf")
       #self.tipografia = pg.font.Font(font_file_instrucciones, 80)


    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True

            if event.type == pg.QUIT:
                salir = True

        self.pantalla.fill((99, 99, 99))
        self.pintar_titulo()
        self.pintar_instrucciones()
        pg.display.flip()


    def pintar_titulo(self):
        mensaje = "THE QUEST"
        texto = self.tipografia.render(mensaje, True, COLOR_TITULO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2 
        pos_y = .25 * ALTO
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_instrucciones(self):
        mensaje = "Pulsa espacio para jugar"
        texto = self.tipografia.render(mensaje, True, COLOR_INSTRUCCIONES)       
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = .65 * ALTO
        self.pantalla.blit(texto, (pos_x, pos_y))

class Levelone(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 99, 00))
        pg.display.flip()


class Leveltwo(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 00, 99))
        pg.display.flip()


class Records(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((00, 99, 99))
        pg.display.flip()
