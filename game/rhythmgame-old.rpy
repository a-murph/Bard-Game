init python:
    import time
    import pygame
    
    class RhythmD(object):
        def __init__(self, sprite, speed, delay, xpos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = xpos
            self.show.y = -50
            self.moving = False
            
        def update(self):
            if store.t + self.delay < time.time():
                self.moving = True
                self.y = self.y + self.speed
            else:
                pass
            
        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value
            
        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value
            
    def sprites_update(st):
        for sprite in sprites[:]:
            sprite.update()
            if sprite.y > config.screen_height:
                sprite.show.destroy()
                sprites.remove(sprite)
                store.health -= 10
                store.combo = 0
                if store.health <= 0:
                    store.lives -= 1
                    store.health = 50
                    renpy.jump("c1_gamefail")
                renpy.restart_interaction()
        return 0.03333333333 #should be 30fps

    def check_note_hit(targetX):
        hit = False
        for sprite in sprites[:]:
            if sprite.moving and int(sprite.y) in store.targetsY and int(sprite.x) == targetX:
                store.health += 5
                store.combo += 1
                if store.combo > store.maxCombo:
                    store.maxCombo = store.combo
                if store.health > 100:
                    store.health = 100
                hit = True
                sprite.show.destroy()
                sprites.remove(sprite)
                break
        if not hit:
            store.health -= 5
            store.combo = 0
            if store.health <= 0:
                store.lives -= 1
                store.health = 50
                renpy.jump("c1_gamefail")
        renpy.restart_interaction()

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_z:
                check_note_hit(store.targetX1)
            elif ev.key == pygame.K_x:
                check_note_hit(store.targetX2)
            elif ev.key == pygame.K_n:
                check_note_hit(store.targetX3)
            elif ev.key == pygame.K_m:
                check_note_hit(store.targetX4)
                
screen showVars:
    text "Health: [health] | Lives: [lives] | Combo: [combo] | MaxCombo: [maxCombo]" xalign 0.5 yalign 0.05 color "#000000"
    text "Z":
        pos (660, 1000)
    text "X":
        pos (860, 1000)
    text "N":
        pos (1060, 1000)
    text "M":
        pos (1260, 1000)

screen timerScreen:
    timer 26.0 action Jump("endgame")
                
label rhythmgame:
    Character("Programmer") "Entering Rhythm Minigame"

    play music busking
    stop ambience
    $ gameRunning = True
    show screen timerScreen

    python:
        health = 50
        lives = 3
        combo = 0
        maxCombo = 0
        t = time.time()
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        targetsY = set(1000+i for i in range(-50, 50))
        targetX1 = 660
        targetX2 = 860
        targetX3 = 1060
        targetX4 = 1260
        sprites = []
        chart1()

        renpy.show_screen("showVars")
        renpy.show("_", what=manager, zorder=1)

    window hide
    $ quick_menu = False

    while gameRunning:
        $ result = ui.interact()

    label endgame:
        $ gameRunning = False
        window show
        $ quick_menu = True
        scene smuggler carriage night destroyed
        hide screen showVars
        hide screen timerScreen
        hide manager

        jump chapter1_scene6