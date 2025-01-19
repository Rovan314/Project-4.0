import time
import csv
#Initially imported time since I wanted to go for a timer, but eventually imported csv for studying since that is what the timer was for.

subject_file = 'subject.txt' # Store the location in a variable since I couldn't get it to work directly

def add_subject():
    try:
        with open(subject_file, 'x') as file:
            pass 
    except FileExistsError:
        pass
    # The "x" command creates a file if the file doesn't exist, initially a neat excuse to use a try-except block
    
    subject = input('Enter subject name: ')
    if not subject:
        print('Subject name can\'t be empty')
        add_subject()
    # First and last recursive function, used to input a subject that will be created unless the input is wrong.
    
    try:
     with open(subject_file, 'r') as file:
        subjects = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
     print('No subjects found. Add a subject first.')
     return

    if subject in subjects:
        print(f'{subject} as a subject already exists')
        return
    # Used to check if the subject already exists

    with open(subject_file, 'a') as file:
        file.write(subject + '\n')
    print(f'{subject} has been added')
    # And if it doesn't, it adds it with "a" command. I could have used the "w" command, but I don't want to overwrite the file

def add_task():
    try:
        with open('task.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Subject', 'Task Name', 'Status'])
    except FileExistsError:
        pass
    # The "x" command as before, but this one can create a file with headings.
    
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
    # The tasks are assigned to a subject, and the subjects are displayed.
    
    while True:
     subject = input('\nEnter a subject\'s name EXACTLY as shown: ')
     if subject in subjects:
         break
     print('Wrong subject input, try again')
    # Input should be exact since including a broad range of subject input was difficult
    # I also used a while loop after I had a lot of trouble working out the global scope for the variables when I tried to use recursive functions
    
    while True:
     task_name = input('Enter task name: ')
     if task_name:
         break
     else:print('Task name can\'t be empty')
    # A while loop for the task name input
    
    while True:
     priority = input('Enter the priority level (Low, Mid, High): ')
     if priority.upper() in ['LOW', 'MID', 'HIGH']:
         break
     else:print('Invalid priority level') 
    # A while loop with specific input
    
    status = "Pending"
    # The status is supposed to be pending by default
    
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
    #Another while loop but with the elif if statement.

def mark_tasks():
    while True:
     task_name = input('Enter name of the task that was completed: ')
     if task_name:
         break
     else:print('Task name can\'t be empty')
    
    updated = False
    #Another while loop with an updated variable set to False
    
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
 #Whenever I deal with csv files, I used exception handling since the wrong input can cause error, I also used the "w" command this time since I need it to overwrite the file. I also used a for loop to overwrite the specific task that was completed and the square bracket was where the task status was located.

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
        # time.sleep is used to give the user a few seconds to read, and it is also used as a timer. But I wanted to show the time go by, hence the for loop.

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
 # If you focus on a task for about 2 minutes, it will build up motivation to end a task and keep you going, hence why I included this function. I also used a while loop for the input.

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
    #Same as before but this one requires an input

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
        # This while loop choice menu has a nested loop in it, I included the chance to mark the task complete as well.

def main():
    print('1. For a Timer')
    print('2. To help get focused')
    print('3. To add a subject')
    print("4. To add a subject's task")
    print('5. To mark a task as complete')
    print('6. To exit')
    choice = input('').lower()
    if choice in ['1', 'timer', 'time']:
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
    else:print('Wrong input, look at the choice and enter again.')
    main()
# The menu calls functions based on the input, since including a broad range of input was possible here, I included them in the elif statements. I also used a recursive function to loop the menu.

if __name__ == '__main__':
 main()
 # A standard construct I saw programmers use
