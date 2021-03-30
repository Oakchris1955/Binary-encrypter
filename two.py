def main(seconds):
    import time
    #seconds = 5
    for x in range(seconds):
        print('This window will close in', seconds, 'seconds')
        seconds -= 1
        time.sleep(1)
