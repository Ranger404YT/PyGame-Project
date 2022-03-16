#Мы не несём ответствености при изменении кода игры

import pygame #Основная библиотека
import sys #Управление системой
from log import log_end, save_log, save_error, save_warn #Работа с логами
from config import config #Работа с конфигами

def events(screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log_end()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.mleft = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.mright = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.mdown = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.mup = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.mleft = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.mright = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.mdown = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.mup = False

#Вывод версии
print(f"[LOG] Control version >> {config['version']}")
print('[LOG] Control loaded\n')