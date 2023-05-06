import time

start_time = time.time()
while time.time() - start_time < 10:
    print('Flowing downhill due to gravity')
    time.sleep(1)
