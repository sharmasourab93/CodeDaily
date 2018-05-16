#!/usr/bin/env python2

import watchdog.events
import watchdog.observers
import sh
import time
import os

# Detach
if os.fork(): os._exit(0)

coffee = sh.coffee.bake('-c')
less = sh.lessc

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.less', '*.coffee'],
            ignore_directories=True, case_sensitive=False)

    def on_modified(self, event):
        if event.src_path.lower().endswith('.less'):
            try: less(event.src_path, event.src_path[:-5] + '.css')
            except sh.ErrorReturnCode_1 as e: print e.stderr
        if event.src_path.lower().endswith('.coffee'):
            try: coffee(event.src_path)
            except sh.ErrorReturnCode_1 as e: print e.stderr

    on_created = on_modified

if __name__ == "__main__":
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
