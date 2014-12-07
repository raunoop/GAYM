__author__ = 'Mikk'
import pygame



class MoveableObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Character(MoveableObject):
    ...
class Player(Character):
    ...
class Enemy(Character):
    ...

