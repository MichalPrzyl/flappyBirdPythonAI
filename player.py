from globals import MAX_HEIGHT, GRAVITY_FORCE, PIPE_WIDTH
from pipe import PipeManager
import pygame


PLAYER_POS_X = 50


class Player:
    pos_x: int # FIXED VALUE
    pos_y: int

    def __init__(self):
        self.pos_x = PLAYER_POS_X
        self.pos_y = MAX_HEIGHT/2
        self.move = 0.0

    def apply_gravity(self):
        self.move += GRAVITY_FORCE
        self.pos_y += self.move
    
    def jump(self):
        self.move = -7.5

    def check_collisions(self):
        for pipe in PipeManager.pipes:
            if self.pos_x > pipe.pos_x and self.pos_x < pipe.pos_x + PIPE_WIDTH:
                # upper body
                if self.pos_y > pipe.hole_position + pipe.hole_height/2 or \
                    self.pos_y < pipe.hole_position - pipe.hole_height/2:
                    return True
