#!/usr/bin/python

# Programmed by hXR16F
# hXR16F.ar@gmail.com, https://github.com/hXR16F

import time
import pygame
from random import randint

# 할 일
# Leaderboard 마무리
# -> 기록 제대로 표시 확인
# Calibration 화면 만들기


def main():
    global score
    global recorded
    recorded = 0
    circle_rect[0], circle_rect[1] = randint(0, width - circle_size), randint(0, height - circle_size)

    clicks, misses = 0, 0
    finished = False

    text_first_click_info = font.render("Touch first circle to start.", True, (255, 255, 255))
    calib_text = font.render("Calibration", True, (255, 255, 255))
    start = 0

    first_click = True
    start_ticks = pygame.time.get_ticks()
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (mouse_x-circle_rect[0]-circle_size/2)**2 + (mouse_y-circle_rect[1]-circle_size/2)**2 <= (circle_size/2+30)**2:
            if first_click:
                first_click = False
                started = time.time_ns()
                start_ticks = pygame.time.get_ticks()
                start = 1
                pygame.draw.rect(screen, bg_color, (width/6-calib_text.get_width()/2, 900, calib_text.get_height(), calib_text.get_height()))

            circle_click.stop()
            circle_click.play()
            clicks += 1
            circle_rect[0], circle_rect[1] = randint(0, width - circle_size), randint(0, height - circle_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if finished:
            score = clicks
            #accuracy = 100 - round((misses / 30) * 100, 2)
            #avg_click_time = round(((time.time_ns() - started) / 30) / 1000000)
            #text_accuracy = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 255, 255))
            #text_avg_click_time = font.render("Average click time: " + str(avg_click_time) + " ms", True, (255, 255, 255))
            #acc = accuracy
            #avgct = avg_click_time
            return

        text_clicks = font.render("Points: " + str(clicks), True, (255, 255, 255))

        screen.fill(bg_color)
        screen.blit(circle, circle_rect)
        if start == 1:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        else:
            elapsed_time = total_time
        timer = font.render("Time : {}".format(str(int(total_time - elapsed_time))), True, (255, 255, 255))
        screen.blit(timer, (40, 10))

        if int(total_time - elapsed_time) == 0 and start == 1:
            finished = True

        if first_click:
            screen.blit(text_first_click_info, (width/2-text_first_click_info.get_width()/2, height / 1.6))
            screen.blit(calib_text, (width / 6 - calib_text.get_width() / 2, 900))

        screen.blit(text_clicks, (40, 40))
        pygame.draw.circle(screen, (102,102,255),(mouse_x,mouse_y), 30)
        pygame.mouse.set_visible(False)
        clock.tick(fps)


        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if width/6-calib_text.get_width()/2 <= mouse_x <= width/6+calib_text.get_width()/2 and 900 <= mouse_y <= 900+calib_text.get_height() and first_click:
                    Calibration()
        pygame.display.flip()


def show_finished_screen():
    Leaderboard()
    global recorded
    recorded = 0
    while True:
        screen.fill(bg_color)
        Title = Bigbigfont.render("EYE-AIM", True, (255,255,255))
        screen.blit(Title, (width/2-Title.get_width()/2, 40))
        finished_text = font.render("Finished!".upper(), True, (255, 255, 255))
        screen.blit(finished_text,(width / 2 - finished_text.get_width() / 2, height / 2 - finished_text.get_height() / 2))
        Leaderboard_text = font.render("Leaderboard", True, (255, 255, 255))
        start_text = font.render("Start", True, (255, 255, 255))
        button1_x = (width * 3 / 2 / 2 - Leaderboard_text.get_width() / 2)
        button1_y = (height * 3 / 2 / 2 - Leaderboard_text.get_height() / 2)
        button2_x = (width / 2 - start_text.get_width() / 2)
        button2_y = (height * 3 / 4 / 2 - start_text.get_height() / 2)
        screen.blit(Leaderboard_text, (button1_x, button1_y))
        screen.blit(start_text, (button2_x, button2_y))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button2_rect = start_text.get_rect()
                if button1_x <= mouse_x <= button1_x + Leaderboard_text.get_width() and button1_y<=mouse_y<=button1_y + Leaderboard_text.get_height():
                    Leaderboard()
                    break
                elif button2_x <= mouse_x <= button2_x + button2_rect[2] and button2_y<=mouse_y<=button2_y + button2_rect[3]:
                    return
        pygame.display.flip()



def Leaderboard():
    global Search_text
    global recorded
    global Input
    while True:
        Input = kofont.render("기록하시겠습니까?", True, (255, 255, 255))
        Search_text = font.render("Search", True, (255, 255, 255))
        reset_Leaderboard()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if width/2-back_text.get_width()/2 <= mouse_x <= width/2+back_text.get_width()/2 and 900 <= mouse_y <= 900+back_text.get_height():
                    return
                if width/2-Input.get_width()/2 <= mouse_x <= width/2+Input.get_width()/2 and 500 <= mouse_y <= 500 + Input.get_height() and over == 0:
                    name = ''
                    while True:
                        Input = kofont.render(name, True, (255, 255, 255))
                        reset_Leaderboard()
                        out = 0
                        for ev2 in pygame.event.get():
                            if ev2.type == pygame.MOUSEBUTTONDOWN:
                                out = 1
                            elif ev2.type == pygame.KEYDOWN:
                                if ev2.key == pygame.K_RETURN:
                                    if recorded == 0:
                                        record[score].append(name)
                                        out = 1
                                        recorded = 1
                                    break

                                elif ev2.key == pygame.K_BACKSPACE:
                                    if name != '':
                                        name = name[:-1]
                                        reset_Leaderboard()
                                else:
                                    if len(name) <= 13:
                                        name += ev2.unicode
                                    else:
                                        pygame.draw.rect(screen, bg_color, [width / 2 - Input.get_width() / 2, 500, Input.get_width(),Input.get_height()])
                                        Input = kofont.render("최대 글자수 : 13자", True, (255, 150, 150))
                                        screen.blit(Input, (width / 2 - Input.get_width() / 2, 500))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        name = name[:13]
                                        Input = kofont.render(name, True, (255, 255, 255))
                                        reset_Leaderboard()
                                    break
                        name_text = kofont.render(name, True, (255, 255, 255))
                        screen.blit(name_text, (width/2-name_text.get_width()/2, 500))
                        pygame.display.flip()
                        if out == 1:
                            Input = kofont.render("기록하시겠습니까?", True, (255,255,255))
                            screen.blit(Input, (width/2-Input.get_width()/2, 500))
                            pygame.display.flip()
                            break
                if width / 2 - Search_text.get_width() / 2 <= mouse_x <= width / 2 + Search_text.get_width() / 2 and 700 <= mouse_y <= 700 + Search_text.get_height():
                    init = ''
                    while True:
                        Search_text = font.render(init, True, (255, 255, 255))
                        reset_Leaderboard()
                        out = 0
                        for ev2 in pygame.event.get():
                            if ev2.type == pygame.MOUSEBUTTONDOWN:
                                out = 1
                            elif ev2.type == pygame.KEYDOWN:
                                if ev2.key == pygame.K_RETURN:
                                    if sum(i.count(init) for i in record) != 0:
                                        show_ranking(init)
                                    else:
                                        pygame.draw.rect(screen, bg_color,
                                                         [width / 2 - Search_text.get_width() / 2, 700, Search_text.get_width(),
                                                          Search_text.get_height()])
                                        Search_text = kofont.render("Invalid Username", True, (255, 150, 150))
                                        screen.blit(Search_text, (width / 2 - Search_text.get_width() / 2, 700))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        Search_text =kofont.render("Search", True, (255, 255, 255))
                                        reset_Leaderboard()
                                    out = 1
                                    break

                                elif ev2.key == pygame.K_BACKSPACE:
                                    if init != '':
                                        init = init[:-1]
                                        reset_Leaderboard()
                                else:
                                    if len(init) <= 13:
                                        init += ev2.unicode
                                    else:
                                        pygame.draw.rect(screen, bg_color,
                                                         [width / 2 - Search_text.get_width() / 2, 700, Search_text.get_width(),
                                                          Search_text.get_height()])
                                        Search_text = kofont.render("최대 글자수 : 13자", True, (255, 150, 150))
                                        screen.blit(Search_text, (width / 2 - Search_text.get_width() / 2, 700))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        init = init[:13]
                                        Search_text = kofont.render(init, True, (255, 255, 255))
                                        reset_Leaderboard()
                                    break
                        init_text = font.render(init, True, (255, 255, 255))
                        screen.blit(init_text, (width / 2 - init_text.get_width() / 2, 700))
                        pygame.display.flip()
                        if out == 1:
                            Search_text = kofont.render("Search", True, (255, 255, 255))
                            screen.blit(Search_text, (width / 2 - Search_text.get_width() / 2, 700))
                            pygame.display.flip()
                            break
        if over == 1:
            break


def reset_Leaderboard():
    ranking = ["1st: ", "2nd: ", "3rd: ", "4th: ", "5th: "]
    global Search_text
    global Input
    global Title
    global back_text

    screen.fill(bg_color)
    Bigfont = pygame.font.Font("assets/Jura-Light.ttf", 48)
    Title = Bigfont.render("Leaderboard".upper(), True, (255, 255, 255))
    back_text = font.render("Back", True, (255, 255, 255))
    score_text = font.render("score : " + str(score), True, (255, 255, 255))
    screen.blit(Title, (width / 2 - Title.get_width() / 2, 50))
    cnt = 0
    for i in range(len(record)-1, -1, -1):
        if record[i] != []:
            for j in record[i]:
                cnt += 1
                if cnt > 5:
                    break
                screen.blit(font.render(ranking[cnt-1] + j + f" : {i}", True, (255,255,255)),
                            (width/2-font.render(ranking[cnt-1] + j + f" : {i}", True, (255,255,255)).get_width()/2, 110+50*(cnt-1)))

            if cnt > 5:
                break
    while cnt < 5:
        screen.blit(font.render(ranking[cnt] + "None", True, (255, 255, 255)),
                    (width / 2 - font.render(ranking[cnt] + "None", True, (255, 255, 255)).get_width() / 2,
                     110 + 50 * cnt))
        cnt += 1

    screen.blit(Input, (width / 2 - Input.get_width() / 2, 500))
    screen.blit(back_text, (width / 2 - back_text.get_width() / 2, 900))
    screen.blit(score_text, (40, 20))
    screen.blit(Search_text, (width / 2 - Search_text.get_width() / 2, 700))
    pygame.display.flip()


def show_ranking(name):
    global record
    back_text = font.render("Back", True, (255, 255, 255))
    Bigfont = pygame.font.Font("assets/Jura-Light.ttf", 48)
    screen.fill(bg_color)
    screen.blit(Bigfont.render(f"{name}'s Score", True, (255, 255, 255)), (width/2-Bigfont.render(f"{name}'s Score", True, (255, 255, 255)).get_width()/2, 40))
    screen.blit(back_text, (width / 2 - back_text.get_width() / 2, 900))
    cnt = sum(i.count(name) for i in record)
    pages = (cnt-1)//15+1
    column = 0
    gap = 200
    cnt = -1
    for i in range(len(record)-1, -1, -1):
        if name in record[i]:
            for j in record[i]:
                if j == name:
                    cnt += 1
                    if cnt % 15 == 0:
                        column += 1
                        cnt = 0
                    screen.blit(font.render(str(i), True, (255,255,255)), (width/2-font.render(str(i), True, (255, 255, 255)).get_width()/2+gap*(column-1)-(pages-1)*0.5*gap, 100+50*cnt))

    pygame.display.flip()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if width / 2 - back_text.get_width() / 2 <= mouse_x <= width/2 + back_text.get_width()/2 and 900 <= mouse_y <= 900 + back_text.get_height():
                    return


def Calibration():
    pygame.mouse.set_visible(True)
    click_n = [0 for i in range(9)]
    COLOR_CHANGE = [(200,200,255), (150,150,255), (100,100,255)]
    colors = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255),
              (255, 255, 255), (255, 255, 255), (255, 255, 255)]
    pos = [[40, 40], [width / 2, 40], [width - 40, 40], [40, height / 2], [width / 2, height / 2],
           [width - 40, height / 2], [40, height - 40], [width / 2, height - 40], [width - 40, height - 40]]
    while True:
        screen.fill(bg_color)
        for i in range(len(pos)):
            pygame.draw.circle(screen, colors[i],pos[i], 15)
        pygame.display.flip()
        clicked = []

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                for i in range(len(pos)):
                    if (mouse_x-pos[i][0])**2+(mouse_y-pos[i][1])**2 <= 225:
                        if click_n[i] <= 1:
                            click_n[i] += 1
                            clicked = pos[i]
                        colors[i] = COLOR_CHANGE[click_n[i]]

        print(clicked if clicked != [] else '', end='')
        if sum(click_n) == 18:
            return




if __name__ == "__main__":
    fps = 100
    clock = pygame.time.Clock()
    size = width, height = 1900,1080
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    bg_color = 40, 40, 40

    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    kofont = pygame.font.SysFont("malgungothic", 36)
    Bigbigfont = pygame.font.Font("assets/Jura-Light.ttf", 64)
    font = pygame.font.Font("assets/Jura-Light.ttf", 36) # https://fonts.google.com/specimen/Jura
    circle_click = pygame.mixer.Sound("assets/click.wav") # https://www.zapsplat.com/music/single-click-screen-press-on-smart-phone-1
    circle = pygame.image.load("assets/circle.png") # https://www.pngwing.com/en/free-png-zuamu
    total_time = 3

    pygame.key.set_repeat(800, 100)
    pygame.display.set_caption("EyeAim")
    pygame.display.set_icon(circle)

    circle_size = 120
    circle = pygame.transform.scale(circle, (circle_size, circle_size))
    circle_rect = circle.get_rect()
    record = list([] for i in range(200))
    over = 0

    while True:
        main()
        pygame.mouse.set_visible(True)
        show_finished_screen()
