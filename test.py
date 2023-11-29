#匯入pygame
import pygame as pg
#pygame初始化
pg.init()


#設定視窗
width, height = 640, 480                        #遊戲畫面寬和高
screen = pg.display.set_mode((width, height))   #依設定顯示視窗
pg.display.set_caption("Sean's game")           #設定程式標題

bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))   #白色
pg.draw.rect(bg, (0,3,255),[70, 70, 500, 60], 4)
pg.draw.rect(bg, (100,3,255),[10, 30, 500, 60], 4)
pg.draw.rect(bg, (100,3,255),[10, 30, 50, 60], 4)
imag = pg.image.load("/Users/huangzongyan/Documents/pygame/頭貼.jpg")
imag.convert()
bg.blit(imag, (100,10))

font = pg.fpnt.SysFont("simhei", 24)
text = font.rnendeer("Hello", True, (0,0,255),(255,255,255))
bg.blit(text, (320,240))

#顯示
screen.blit(bg, (0,0))
pg.display.update()




#關閉程式的程式碼
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()        
