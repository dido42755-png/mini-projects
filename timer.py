import time
mytime = int(input(' enter the time in seconds:'))

for x in range(mytime , 0, -1): 
    time.sleep(1)
    seconds = x % 60
    minutes = int(x // 60)
    hours = int(x // 3600) 
    days = int(x // 86400)
    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
print(' time is up')