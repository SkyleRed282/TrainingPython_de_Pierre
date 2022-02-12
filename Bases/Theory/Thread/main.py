
import threading
import time

def thread_function(name):
    while (True):
        time.sleep(1)
        print(f'Loop : {name}')


if __name__ == "__main__":

    print('debut\n')
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    y = threading.Thread(target=thread_function, args=(2,))
    y.start()

