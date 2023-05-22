import moviepy.editor
from pathlib import Path
import os


folder = input('Введите путь к видео: ')
file_name = input('Введите имя файла с расширением: ')
full_path = os.path.join(folder, file_name)
if Path(full_path).is_file():
    print('[+] Файл найден. Начинаю работу!')
    video = moviepy.editor.VideoFileClip(full_path)
    audio = video.audio
    try:
        # работа с файлом, stem - взять только имя файла, без расширения
        # audio.write_audiofile(f'{os.path.splitext(file_name)[0]}_audio.mp3')
        audio.write_audiofile(f'{Path(full_path).stem}.mp3')
    except Exception as ex:
        print(f'Ошибка: {ex}')
