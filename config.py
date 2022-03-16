#Мы не несём ответствености при изменении кода игры

import os #Управление файлами
import dotenv
from dotenv import load_dotenv

dir = f'{os.getcwd()}/'
os.chdir('PyGame Files')
dotenv.load_dotenv('config.txt') #Загрузка конфига

config = {
    'resourcepacks': os.environ.get('resourcepacks'),
    'version': os.environ.get('version'),
    'x': os.environ.get('x'),
    'y': os.environ.get('y')
}

#Вывод версии
print(f"\n[LOG] Config version >> {config['version']}")
print('[LOG] Config loaded\n')