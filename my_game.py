from pygame import *

mixer.init()
mixer.music.load('bg_music.ogg')

mixer.music.play(loops = -1)

img_back = "Background.png"


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    display.update()
        