#Мы не несём ответствености при изменении кода игры

import os #Управление файлами
from config import config, dir #Работа с конфигами

if os.path.isfile(f'{dir}\Logs\Log.txt'):
    open(f'{dir}\Logs\Log.txt')

file = open(f'{dir}\Logs\Log.txt','w')
file.write(
    '[Game] Help started\n'
    '[HELP] First loaded config\n'
    '[HELP] The second is loaded models\n'
    '[HELP] Third loaded control\n\n'
    '[HELP] If you dont know samethin, write to us\n'
    '[HELP] Discord @Ranger404#6813\n'
    '[HELP] VK @Ranger404\n'
    '[Game] Help saved\n'
    '[Game] Log started\n\n'
    f'[LOG] Config version >> {config["version"]}\n'
    '[LOG] Config loaded\n\n'
    f'[LOG] Models version >> {config["version"]}\n'
    '[LOG] Models loaded\n\n'
    f'[LOG] Control version >> {config["version"]}\n'
    '[LOG] Control loaded\n\n'
    f'[LOG] Game version >> {config["version"]}\n\n'
)
def save_log(log_line):
    file.write(f'[LOG] {log_line}\n')
def save_error(log_line):
    file.write(f'[ERROR] {log_line}\n')
def save_warn(log_line):
    file.write(f'[WARN] {log_line}\n')

def log_end(type=False, log_txt=None):
    if type == True:
        if log_txt==None:
            pass
        else:
            file.write(f'[LOG] {log_txt}')
        file.write('[ERROR] Stoped')
        file.write('[Game] Log stoped')
    elif type == False:
        file.write('[Game] Stoped by client')
        file.write('[Game] Log stoped')
    else:
        if log_txt==None:
            pass
        else:
            file.write(f'[LOG] {log_txt}')
        file.write('[Game] [ERROR] Unknown error')
        file.write('[Game] Log stoped')