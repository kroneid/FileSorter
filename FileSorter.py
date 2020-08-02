from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - класс по отслеживанию изменений
from watchdog.events import FileSystemEventHandler


# Создаем класс наследник, через него может отслеживать изменения в папках
class Handler(FileSystemEventHandler):
	# При любых изменениях в папке, мы перемещаем файлы в ней
	def on_modified(self, event):
		# Перебираем все файлы в папке folder_track
		for filename in os.listdir(folder_track):
			# Проверяем расширенеи файла
			extension = filename.split(".")
			# Если это фото,
			if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg"):
				# то перемещаем файл в папку с фото
				file = folder_track + "/" + filename
				new_path = folder_dest + "/Photos/" + filename
				os.rename(file, new_path)
			# Если файл видео, то в папку с видео
			# Такое же можно прописать и для других расширений файлов
			elif len(extension) > 1 and extension[1].lower() == "mp4":
				file = folder_track + "/" + filename
				new_path = folder_dest + "/Videos/" + filename
				os.rename(file, new_path)


# Папка что отслеживается
folder_track = 'Путь папки'
# Папка куда перемещать будем
folder_dest = 'Путь папки 2'

# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

# Программа будет срабатывать каждые 10 милисекунд 
try:
	while(True):
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()
