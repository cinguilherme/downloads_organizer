import sys
import getpass
import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import RegexMatchingEventHandler

class ImageEventHandler(RegexMatchingEventHandler):

    IMAGES_REGEX = [r".*\.txt$"]

    def __init__(self):
        super().__init__(self.IMAGES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename}_alguma_coisa_processada.txt"

        print(filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    #find the downloads folder authomatcally
    username = getpass.getuser()
    downloads_folder = '/home/'+username+'/Downloads'
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = downloads_folder
    # ---------------------------------------

    #handlers
    event_handler = LoggingEventHandler()
    coisado = ImageEventHandler()
    #-----------

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    observer2 = Observer()
    observer2.schedule(coisado,path, recursive=True)
    observer2.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()