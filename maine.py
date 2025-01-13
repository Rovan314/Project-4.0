import time

def sleep():
    wan = input('Write something: ')
    if wan.upper == 'HELLO':
        print('Hi')
        time.sleep(5)
        print('Bye')
    elif wan.upper == 'SOMETHING':
        print('Not funny')
        time.sleep(1)
        print('didn\'t laugh')
    else:
        print('Incomplete')
        time.sleep(1)
        print('\nReminder')
sleep()



def taimer():
    taim = int(input('What time in seconds only please?'))
    for x in range(taim, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     print(f'{minutes:02}:{seconds:02}')
     time.sleep(1)
    print('Done1')

taimer()