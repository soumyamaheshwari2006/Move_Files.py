import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir= "C:/users/public"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("Hey",{event.src_path},"has been created")
    
    def on_deleted(self, event):
        print("Oops! someone deleted",{event.src_path},"!")

    def on_modified(self, event):
        print("Hey",{event.src_path}, "is modified")

    def on_moved(self, event):
        print("Hey", {event.src_path},"is moved")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...") 
except KeyboardInterrupt:
    print("stop")
    observer.stop()