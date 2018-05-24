import variables as var
import colors as clr
import pygame
import game


env = var.EnvVariable()
color = clr.getColor() 

pygame.init()
gameFrame = pygame.display.set_mode((env['frame_width'], env['frame_height']))
pygame.display.set_caption(env['frame_name'])
fps = pygame.time.Clock()
game.Game(gameFrame, color, env)


