import sys
import getpass
import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import RegexMatchingEventHandler

username = getpass.getuser()

source_dwl = '/home/'+username+'/Downloads/'
destination_dwl = '/home/'+username+'/Downloads_opt/'

class TxtEventHandler(RegexMatchingEventHandler):

    IMAGES_REGEX = [r".*\.txt$"]

    def __init__(self):
        super().__init__(self.IMAGES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        actual_name = filename.split("/").pop(-1)+ext

        source = filename+ext
        filename = f"{filename}_alguma_coisa_processada.txt"
        just_name = filename.split("/").pop(-1)
        destination = 'home/'+username+'/Downloads_opt/txt/'+just_name

        os.rename(source_dwl+actual_name, destination_dwl+actual_name)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    #find the downloads folder authomatcally

    downloads_folder = '/home/'+username+'/Downloads'
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = downloads_folder
    # ---------------------------------------

    #handlers_2
    event_handler = LoggingEventHandler()
    txt_handler = TxtEventHandler()
    #-----------

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    observer3 = Observer()
    observer3.schedule(txt_handler, path, recursive=True)
    observer3.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()