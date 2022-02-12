import time
import threading

class Counter(threading.Thread):

    def get_thread(self):
        return threading.Thread(target=self.thread_function, args=(1,))

    def thread_function(self, name):

        while (True):
            time.sleep(1)
            print(f'Loop : {name}')
