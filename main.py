#Мы не несём ответствености при изменении кода игры
import os

import pygame #Основная библиотека
from log import log_end, save_log, save_error, save_warn #Работа с логами
from config import config, dir
import models #Работа с моделями
from models import model #Работа с моделями
import control #Управление
from player import Player

def build():
    pygame.init()
    models.load_texturs() #Загрузка текстур
    screen = pygame.display.set_mode((int(config['x']),int(config['y']))) #Настройка расширения окна
    bg_color = (88, 88, 88)
    pygame.display.set_caption("Project 1")
    pygame.display.set_icon(model['icon'])
    player=Player(screen,model['player'])
    pass

    while 1:
        #screen.fill(bg_color) #Заполнение фоновым цветом
        control.events(screen, player) #Приём действий клиента
        player.update()
        player.output()
        pygame.display.flip() #Загрузка изменений


def main():
    print(f"[LOG] Game version >> {config['version']}\n") #Вывод версии, написанно в config.txt в файлах игры
    build()

#Проверка названия
if __name__ == '__main__':
    main() #Запуск функиции для старта
