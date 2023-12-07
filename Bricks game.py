import pygame as pg, random, math, time

# 建立球體
class Ball(pg.sprite.Sprite):
    def __init__(self, sp, srx, sry, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.direction = random.randint(40,70)  #移動角度

        # 繪製球體
        self.image = pg.Surface([radium*2, radium*2])  
        self.image.fill((255,255,255))
        pg.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  
        self.rect.center = (srx,sry)       

    def update(self):         
        radian = math.radians(self.direction)    
        self.dx = self.speed * math.cos(radian)  
        self.dy = -self.speed * math.sin(radian) 
        self.x += self.dx     
        self.y += self.dy
        self.rect.x = self.x  
        self.rect.y = self.y

        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
            self.bouncelr()
        elif(self.rect.top <= 10): 
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10): 
            return True
        else:
            return False
 
    def bounceup(self): 
        self.direction = 360 - self.direction

    def bouncelr(self): 
        self.direction = (180 - self.direction) % 360

# 磚塊類別            
class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38, 13]) 
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 板子類別
class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        pad_length = 17 * 5 
        self.image = pg.Surface([pad_length, 20]) 
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width) / 2)
        self.rect.y = screen.get_height() - self.rect.height - 30

    def update(self):  
        pos = pg.mouse.get_pos()  
        self.rect.x = pos[0]       
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

# 結束程式
def gameover(message): 
    global running
    text = ffont.render(message, 1, (255,0,255))  
    screen.blit(text, (screen.get_width()/2-150,screen.get_height()/2-20))
    pg.display.update()  
    time.sleep(5)       
    running = False      

pg.init()
score = 0 
dfont = pg.font.SysFont("Arial", 20)   
ffont = pg.font.SysFont("SimHei", 32)   

# 背景
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("5b0g0017黃宗彥")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pg.sprite.Group()
bricks = pg.sprite.Group()   

# 建立兩個球體
red_ball = Ball(5, 300, 350, 10, (255,0,0))  
blue_ball = Ball(5, 200, 350, 10, (0,0,255)) 
allsprite.add(red_ball)
allsprite.add(blue_ball)

pad = Pad()          
allsprite.add(pad)   

# 建立磚塊
for row in range(0, 5):          
    for column in range(0, 15):  
        if row == 1 or row == 0: 
            brick = Brick((153,205,255), column * 40 + 1, row * 15 + 1)   
        if row == 2: 
            brick = Brick((94,175,254), column * 40 + 1, row * 15 + 1)    
        if row == 3 or row == 4:  
            brick = Brick((52,153,207), column * 40 + 1, row * 15 + 1)  
        bricks.add(brick)     
        allsprite.add(brick)  

clock = pg.time.Clock()        
downmsg = "Press Left Click Button to start game!"
playing = False  
running = True

# 運行的程式碼
# 運行的程式碼
while running:
    clock.tick(40)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    buttons = pg.mouse.get_pressed() 
    if buttons[0]:         
        playing = True

    if playing == True:  
        screen.blit(background, (0,0))  
        red_fail = red_ball.update()
        blue_ball.update() # 更新藍色球的位置
        if red_fail:  
            gameover("You failed!See you next time~")
        pad.update()      

        # 紅色球的碰撞檢查
        hitbrick_red = pg.sprite.spritecollide(red_ball, bricks, True)
        hitpad_red = pg.sprite.collide_rect(red_ball, pad)
        if hitbrick_red:
            score += len(hitbrick_red)  
            red_ball.rect.y += 20 
            red_ball.bounceup()
        if hitpad_red:
            red_ball.bounceup()

        # 藍色球的碰撞檢查
        hitbrick_blue = pg.sprite.spritecollide(blue_ball, bricks, True)
        hitpad_blue = pg.sprite.collide_rect(blue_ball, pad)
        if hitbrick_blue:
            score += len(hitbrick_blue)  
            blue_ball.rect.y += 20 
            blue_ball.bounceup()
        if hitpad_blue:
            blue_ball.bounceup()

        if len(bricks) == 0:  # 所有磚塊消失
            gameover("Congratulations!!")

        allsprite.draw(screen)
        downmsg = "Score: " + str(score)
        message = dfont.render(downmsg, 1, (255,0,255))
        screen.blit(message, (screen.get_width()/2-125,screen.get_height()-30))
    pg.display.update()
pg.quit()
