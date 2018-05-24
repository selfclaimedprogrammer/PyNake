import pygame
import random

class Game:
    def __init__(self, gameFrame, color, env):
        self.env = env
        self.font = pygame.font.SysFont(None, self.env["default_font_size"])
        self.color = color
        self.gameFrame = gameFrame
        self.EXIT = False
        self.run()
        self.stop()

    def run(self):
        self.gameOver = False
        self.gaw = self.env['game_area_width']
        self.gah = self.env['game_area_height']
        self.block = self.env['block_snap']

        self.x_pos = self.env['frame_width']/2
        self.y_pos = self.env['frame_height']/2

        self.x_change = 0
        self.y_change = 0

        self.player_list = []
        self.player_len = 1
        
        self.fps = pygame.time.Clock()

        self.apple_x_pos = round(random.randrange(self.env['x_start'], self.env['x_end']-10)/10)*10
        self.apple_y_pos = round(random.randrange(self.env['y_start'], self.env['y_end']-10)/10)*10

        # Maingame Logic
        while not self.EXIT:

            # Gameover Logic
            while self.gameOver == True:
                self.gameFrame.fill(self.color['background2'])
                self.showText("Game Over!", self.color['danger'],[170, self.env['game_area_height']/2],40)
                self.showText("Press C to Continue or Q to Quit!", self.color['player'],[100, (self.env['game_area_height']/2)+30],30)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.EXIT = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.EXIT = True
                            self.gameOver = False
                        if event.key == pygame.K_c:
                            self.gameOver = False
                            self.run()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.EXIT = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change = -self.block
                        self.y_change = 0
                    if event.key == pygame.K_RIGHT:
                        self.x_change = self.block
                        self.y_change = 0
                    if event.key == pygame.K_UP:
                        self.y_change = -self.block
                        self.x_change = 0
                    if event.key == pygame.K_DOWN:
                        self.y_change = self.block
                        self.x_change = 0

            if self.x_pos >= self.env['x_end'] or self.x_pos < self.env['x_start'] or self.y_pos >= self.env['y_end'] or self.y_pos < self.env['y_start']:
                #print ("({},{})".format(self.x_pos,self.y_pos))
                self.x_change = 0
                self.y_change = 0
                self.gameOver = True
            
            self.x_pos += self.x_change
            self.y_pos += self.y_change

            self.gameFrame.fill(self.color['background'])
            
            # Sections
            self.topSection = self.sections(self.gameFrame, self.color['default'], [0,0,500,50])
            self.gameSection = self.sections(self.gameFrame,self.color['crayWhite'], [0,50,self.gaw,self.gah])
            self.bottomSection = self.sections(self.gameFrame,self.color['background'], [0,450,500,50])
            
            # Player 
            self.player_head = []
            self.player_head.append(self.x_pos)
            self.player_head.append(self.y_pos)
            self.player_list.append(self.player_head)
            if len(self.player_list) > self.player_len:
                del self.player_list[0]

            self.player(self.player_list)


            # Spawn Apple
            self.spawnApple(self.apple_x_pos, self.apple_y_pos)
            
            pygame.display.update()
            
            if self.x_pos == self.apple_x_pos and self.y_pos == self.apple_y_pos:
                self.spawnNewApple()

            self.fps.tick(self.env['frame_fps'])
            
    def stop(self):
        pygame.quit()
        quit()
    
    def sections(self, gameFrame, fill, cords):
        pygame.draw.rect(gameFrame, fill, cords)

    def player(self, s_list):
        for xny in s_list:
            pygame.draw.rect(self.gameFrame, self.color['player'], [xny[0],xny[1],self.block,self.block])

    def showText(self, text, color, cords, size):
        if size != 0:
            self.font = pygame.font.SysFont(None, size)
        textRen = self.font.render(text, True, color)
        self.gameFrame.blit(textRen, cords)

    def spawnApple(self, x, y):
        pygame.draw.rect(self.gameFrame, self.color['apple'], [x,y,self.block, self.block])

    def spawnNewApple(self):
        self.apple_x_pos = round(random.randrange(self.env['x_start'], self.env['x_end']-10)/10)*10
        self.apple_y_pos = round(random.randrange(self.env['y_start'], self.env['y_end']-10)/10)*10
        self.player_len += 1

