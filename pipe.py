import random
import pygame
from globals import MAX_HEIGHT, MAX_WIDTH, GOING_LEFT_SPEED,\
    PIPE_WIDTH, STANDARD_PIPE_HEIGHT

class PipeManager:
    pipes = []
    def create_pipe():
        random_position = random.randrange(250, MAX_HEIGHT - 250)
        pipe = Pipe(random_position, STANDARD_PIPE_HEIGHT)
        PipeManager.pipes.append(pipe)
        return pipe
    
    def cleanup():
        for pipe in PipeManager.pipes:
            if pipe.pos_x < -50:
                PipeManager.pipes.remove(pipe)
                del pipe



class Pipe:
    hole_position: int # Y where is the hole
    hole_height: int # how much space is to jump through
    pos_x: int

    def __init__(self, hole_position, hole_height):
        self.hole_position = hole_position
        self.hole_height = hole_height
        self.pos_x = MAX_WIDTH + 100

    def draw(self, surface):
        # upper element
        position_upper = pygame.Rect(self.pos_x, 0, PIPE_WIDTH, self.hole_position - self.hole_height/2)
        pygame.draw.rect(surface, "red", position_upper)
        # bottom element
        position_bottom = pygame.Rect(self.pos_x, self.hole_position + self.hole_height/2, PIPE_WIDTH, MAX_HEIGHT - self.hole_position - self.hole_height/2)
        pygame.draw.rect(surface, "red", position_bottom)

    def update(self):
        self.pos_x -= GOING_LEFT_SPEED