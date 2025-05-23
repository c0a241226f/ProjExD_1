import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    bg_img2 =pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2後半
    #kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()  # 練習１０－１：こうかとんRectの抽出
    kk_rct.center = 300, 200  # 練習１０－２：こうかとんRectの中心座標を指定
 
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return   
        key_lst = pg.key.get_pressed() #10.3
        if key_lst[pg.K_UP]:
            y=-1
            z=-1
           # kk_rct.move_ip(0, -1)  # 練習１０－４
        elif key_lst[pg.K_DOWN]:
            y=-1
            z=1
           #  kk_rct.move_ip(0, +1)  # 練習１０－４
        elif key_lst[pg.K_LEFT]:
            y=-1
            z=0
           #  kk_rct.move_ip(-1, 0)  # 練習１０－４
        elif key_lst[pg.K_RIGHT]:
            y=1
            z=0
           # kk_rct.move_ip(+1, 0)  # 練習１０－４
        else:
             y=-1
             z=0
             #kk_rct.move_ip(-1, 0) #押してない時左に動く 演習1


        x=tmr%3200
        kk_rct.move_ip(y,z)
        #kk_rct.center = -x+400, 200
        screen.blit(bg_img,[-x, 0]) #練習6
        screen.blit(bg_img2,[-x+1600, 0]) #練習7
        screen.blit(bg_img,[-x+3200, 0]) #練習9
        screen.blit(kk_img,kk_rct)

        #screen.blit(kk_img,[300,200]) #練習４
        #screen.blit(kk_img,kk_rct) #練習10.5

        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()