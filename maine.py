import time

def main():
    print('Press 1 for a timer')
    print('Press 2 for a motivational exercise')
    choice = input('')
    if choice == '1':
        taimer()
    elif choice == '2':
        sleep()
    elif choice == '3':
        print('Goodbye')
        exit()
    else:print('I\'s only 1 or 2 \n now')
    main()

def sleep():
        print('Focus on nothing but the task at hand for two minutes, because it helps you concentrate and will keep you busy later on')
        time.sleep(1)
        taim = int(input('Enter your desired time in minutes:seconds format:'))
min, sec = map(int, taim.split(':'))
taim = min*60 + sec
for x in range(taim, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     print(f'{minutes:02}:{seconds:02}')
     time.sleep(1)
print('Done1')



def taimer():
    taim = int(input('Enter your desired time in minutes:seconds format:'))
    min, sec = map(int, taim.split(':'))
    taim = min*60 + sec
    for x in range(taim, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     print(f'{minutes:02}:{seconds:02}')
     time.sleep(1)
    print('Done1')

taimer()