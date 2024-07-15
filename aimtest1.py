#!/usr/bin/python

# Programmed by hXR16F
# hXR16F.ar@gmail.com, https://github.com/hXR16F

import time
import pygame
from random import randint


def main(first):
    global acc
    global avgct

    circle_rect[0], circle_rect[1] = randint(0, width - circle_size), randint(0, height - circle_size)

    clicks, misses = 0, 0
    finished = False

    if first:
        text_first_click_info = font.render("Click first circle to start.", True, (255, 255, 255))
    else:
        text_first_click_info = font.render("Click circle to start again.", True, (255, 255, 255))

    first_click = True
    start = 0
    start_ticks = pygame.time.get_ticks()
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if start == 0 and first_click:
            start = 1
        elif mouse_x >= circle_rect[0] and mouse_x <= circle_rect[0] + circle_rect[2] and mouse_y >= circle_rect[1] and mouse_y <= circle_rect[1] + circle_rect[3]:
            if first_click:
                first_click = False
                started = time.time_ns()
                start = 1
                start_ticks = pygame.time.get_ticks()

            circle_click.stop()
            circle_click.play()
            clicks += 1
            circle_rect[0], circle_rect[1] = randint(0, width - circle_size), randint(0, height - circle_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if finished:
            #
            #accuracy = 100 - round((misses / 30) * 100, 2)
            #avg_click_time = round(((time.time_ns() - started) / 30) / 1000000)
            #text_accuracy = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 255, 255))
            #text_avg_click_time = font.render("Average click time: " + str(avg_click_time) + " ms", True, (255, 255, 255))
            #acc = accuracy
            #avgct = avg_click_time
            return

        text_clicks = font.render("Clicks: " + str(clicks), True, (255, 255, 255))

        screen.fill(bg_color)
        screen.blit(circle, circle_rect)

        if start == 1:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        else:
            elapsed_time = total_time
        timer = font.render("Time : {}".format(str(int(total_time - elapsed_time))), True, (255, 255, 255))
        screen.blit(timer, (10, 10))

        if int(total_time - elapsed_time) == 0:
            finished = True

        if first_click:
            screen.blit(text_first_click_info, (width / 2 - text_first_click_info.get_width() / 2, height / 1.6))

        screen.blit(text_clicks, (40, 40))
        pygame.display.flip()
        clock.tick(fps)

        if finished:
            screen.blit(font.render("FINISHED!".upper(), True, (255, 255, 255)), (200, 200))


if __name__ == "__main__":
    fps = 100
    clock = pygame.time.Clock()
    size = width, height = 1200, 900
    screen = pygame.display.set_mode(size)
    bg_color = 40, 40, 40


    pygame.init()
    pygame.font.init()
    # pygame.mixer.init()

    font = pygame.font.Font("assets/Jura-Light.ttf", 36) # https://fonts.google.com/specimen/Jura
    circle_click = pygame.mixer.Sound("assets/click.wav") # https://www.zapsplat.com/music/single-click-screen-press-on-smart-phone-1
    circle = pygame.image.load("assets/circle.png") # https://www.pngwing.com/en/free-png-zuamu
    total_time = 100


    pygame.display.set_caption("aimtest")
    pygame.display.set_icon(circle)

    circle_size = 80
    circle = pygame.transform.scale(circle, (circle_size, circle_size))
    circle_rect = circle.get_rect()

    main(first=True)
    while True:
        main(first=False)
