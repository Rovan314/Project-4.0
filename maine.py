import time
import csv

def add_subject():
    subject = input('Enter subject name: ')
    with open('work.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([subject])
    if not subject:
        print('Subject name can\'t be empty')
        return None
    print(f'{subject} added successfully')
    return subject

def add_work():
    subject = input('Enter subject name: ')
    if not subject:
        print('Subject name can\'t be empty')
        return
    with open('work.csv', newline='') as file:
     x = csv.reader(file)
     for x in 'work.csv':
        print(f'{x}')


def sleep():
        print('Focus on nothing but the task at hand for two minutes, because it helps you concentrate and will keep you busy later on')
        time.sleep(5)
        mins = 0
        secs = 3
        taimer = mins * 60 + secs
        for x in range(taimer, 0, -1):
            minutes = x // 60
            seconds = x % 60
            print(f'{minutes:02}:{seconds:02}')
            time.sleep(1)
        print("time's up")
        choice = input('Do you feel like you can do more? (yes or no): ')
        if choice.lower() in ['yes', 'y']:
            print('Excellent!')
            taimer()
        elif choice in ['no', 'n']:
         print('Good luck!')
         exit()
        else: 
         print('It\'s yes or no...')
        return 


def taimer():
    taim = int(input('Enter your desired time in minutes:seconds format:'))
    min, sec = map(int, taim.split(':'))
    taim = min*60 + sec
    for x in range(taim, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     print(f'{minutes:02}:{seconds:02}')
     time.sleep(1)
    print('Done')

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

add_work()