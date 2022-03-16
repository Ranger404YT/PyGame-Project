#Мы не несём ответствености при изменении кода игры

import pygame #Основная библиотека
import os #Управление файлами
from log import log_end, save_log, save_error, save_warn #Работа с логами
from config import config, dir #Работа с конфигами
import sys #Управление системой

models_vault=3 #Количество моделей
models=[ #Только название, файлы в разширении png его писать не надо
    'icon',
    'player',
    'enemy'
]
model={}

def load_texturs():
    for model_namber in range(models_vault): #Обновление кахдой текстуры по очереди
        if os.path.isfile(f'{dir}{models[model_namber]}.png') and config['resourcepacks']:#Проверка есть ли файл с кастомная текстура
            try:
                model_load = pygame.image.load(
                    f'{dir}PyGame Files/ResourcePacks/{models[model_namber]}.png') #Загрузка кастомных текстур
                model[models[model_namber]]=model_load
            except FileNotFoundError: #При нинахождении файла выполняется следующее действие
                try:
                    model_load = pygame.image.load(
                        f'{dir}PyGame Files/assets/textur/{models[model_namber]}.png')  # Загрузка стандартных текстур
                    model[models[model_namber]]=model_load
                except FileNotFoundError: #При нинахождении файла выполняется следующее действие
                    save_warn('Models Error')
                    model_load = pygame.image.load(
                        f'{dir}PyGame Files/Debug/textur/DebugTextur.png')  # Загрузка стандартных текстур
                    model[models[model_namber]]=model_load
        else:
            try:
                model_load = pygame.image.load(
                    f'{dir}PyGame Files/assets/textur/{models[model_namber]}.png') #Загрузка стандартных текстур
                model[models[model_namber]]=model_load
            except FileNotFoundError: #При нинахождении файла выполняется следующее действие
                save_warn('Models Error')
                model_load = pygame.image.load(
                    f'{dir}PyGame Files/Debug/textur/DebugTextur.png')  # Загрузка стандартных текстур
                model[models[model_namber]]=model_load

#Вывод версии
print(f"[LOG] Models version >> {config['version']}")
print('[LOG] Models loaded\n')