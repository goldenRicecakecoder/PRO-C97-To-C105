import os
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir_project102 = "C:/Users/hepzi/Downloads"
to_dir_project102 = "C:/Users/Project102/Document_Files"


list_of_files_project102 = os.listdir(from_dir_project102)


print("Files in the source path:")
print(list_of_files_project102)


for file_name in list_of_files_project102:
  
    name, extension = os.path.splitext(file_name)

    if not extension:
        continue

    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    if extension in allowed_extensions:
        path1 = from_dir_project102 + '/' + file_name
        path2 = to_dir_project102 + '/' + "Document_Files"
        path3 = to_dir_project102 + '/' + "Document_Files" + '/' + file_name

        
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
           
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)




from_dir_project103 = "/path/to/track"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
        else:
            print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if event.is_directory:
            print(f"Directory moved/renamed: {event.src_path} to {event.dest_path}")
        else:
            print(f"File moved/renamed: {event.src_path} to {event.dest_path}")

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
        else:
            print(f"File deleted: {event.src_path}")


event_handler_project103 = FileEventHandler()
observer_project103 = Observer()
observer_project103.schedule(event_handler_project103, path=from_dir_project103, recursive=True)


observer_project103.start()

try:
    print("Press any key to stop the observer.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
  
    observer_project103.stop()


observer_project103.join()
