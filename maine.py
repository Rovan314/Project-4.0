import time
import csv
subject_file = 'subject.txt'

def add_subject():
    try:
        with open(subject_file, 'x') as file:
            pass 
    except FileExistsError:
        pass
    
    subject = input('Enter subject name: ')
    if not subject:
        print('Subject name can\'t be empty')
        add_subject()
    
    try:
     with open(subject_file, 'r') as file:
        subjects = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
     print('No subjects found. Add a subject first.')
     return
    
    if subject in subjects:
        print(f'{subject} as a subject already exists')
        return
    
    with open(subject_file, 'a') as file:
        file.write(subject + '\n')
    print(f'{subject} has been added')

def add_task():
    try:
        with open('task.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Subject', 'Task Name', 'Status'])
    except FileExistsError:
        pass

    try:
     with open(subject_file, 'r') as file:
        subjects = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
     print('No subjects found. Add a subject first.')
     return
    
    if subjects:
     print('Subjects available')
     for subject in subjects:
         print(subject)
    else: print('No subjects available')
    
    while True:
     subject = input('\nEnter a subject\'s name EXACTLY as shown: ')
     if subject in subjects:
         break
     print('Wrong subject input, try again')
    
    
    while True:
     task_name = input('Enter task name: ')
     if task_name:
         break
     else:print('Task name can\'t be empty')

    while True:
     priority = input('Enter the priority level (Low, Mid, High): ')
     if priority.upper() in ['LOW', 'MID', 'HIGH']:
         break
     else:print('Invalid priority level') 
 
    
    status = "Pending"
    
    with open('task.csv', 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([subject, task_name, status])
         print(f'{task_name} has been assigned to {subject}')
    
    while True:
     choice = input('Would you like to complete the task now? (yes or no): ')
     if choice.lower() in ['yes', 'y']:
        timer()
        break
     elif choice in ['no', 'n']:
        print('Understandable')
        main()
        break
     else:print('Invalid input')
     continue

def mark_tasks():
    task_name = input('Enter name of the task that was completed: ')
    updated = False
    try:
        with open('task.csv', 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)

        with open('task.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in tasks:
                if row[1].lower() == task_name.lower() and row[2] == 'Pending':
                    row[2] = 'Completed'
                    updated = True
                writer.writerow(row)

        if updated:
            print(f'{task_name} is now completed, good job')
        else:
            print(f'{task_name} was not found or is already completed')
    except FileNotFoundError:
        print('No tasks found. Start by adding a task.')

def sleep():
        print('Focus on nothing but the task at hand for two minutes, because it helps you concentrate and will keep you busy later on')
        time.sleep(5)
        
        mins = 2
        secs = 0
        taimer = mins * 60 + secs
        
        for x in range(taimer, 0, -1):
            minutes = x // 60
            seconds = x % 60
            print(f'{minutes:02}:{seconds:02}')
            time.sleep(1)
        
        print("time's up")
        
        while True:
         choice = input('Do you feel like you can do more? (yes or no): ')
         if choice.lower() in ['yes', 'y']:
            print('Excellent!')
            timer()
            break
         elif choice in ['no', 'n']:
          print('Good luck!')
          exit()
         else: 
          print('It\'s yes or no...')
         continue

def timer():
    taime = (input('Enter your desired time in minutes:seconds format:'))
    min, sec = map(int, taime.split(':'))
    taime = min*60 + sec
    
    for x in range(taime, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     print(f'{minutes:02}:{seconds:02}')
     time.sleep(1)
     
     print('Done')
    
    while True:
     choice = input('\nDo you need more time? (yes or no): ')
     if choice.lower() in ['yes', 'y']:
        print('Very well')
        timer()
        break
     elif choice.lower() in ['no', 'n']:
        while True:
         joyce = input('Is your task completed? (yes or no): ')
         if joyce.lower() in ['yes', 'y']:
            print('Good job')
            mark_tasks()
            break
         elif joyce.lower() in ['no', 'n']:
            print('Better luck next time')
            exit()
         else:print('Invalid input') 
         continue

def main():
    print('1. For a Timer')
    print('2. To help get focused')
    print('3. To add a subject')
    print("4. To add a subject's task")
    print('5. To mark a task as complete')
    print('6. To exit')
    choice = input('').lower()
    if choice in ['1', 'timer',]:
        timer()
    elif choice in ['2', 'help focus', 'help get focused', 'focus', 'help']:
        sleep()
    elif choice in ['3', 'add a subject', 'add subject', 'add sub', 'subject', 'sub']:
        add_subject()
    elif choice in ['4', 'add a task', 'add task', 'task']:
        add_task()
    elif choice in ['5', 'mark a task', 'mark task']:
        mark_tasks()
    elif choice in ['6', 'exit']:
        exit()
    else:print('Wrong input, enter the correct number')
    main()
if __name__ == '__main__':
 main()