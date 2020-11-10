# The program allows user to login if user is admin then the user can register other users 
# and generate reports and view the reports.
# Users can add tasks, view all tasks and tasks only assigned to them
import sys
import re
import datetime

def add_task():
    
        tasks_file = open('tasks.txt', 'a+')

        user = input("Enter your username: ")
        task_title = input("Enter title of your task: ")
        task_description = input("Enter description of your task: ")
        assigned_date = input("Enter the date the task was assigned: ")
        due_date = input("Enter the due date of your task: ")
        is_completed = input("Is the task completed: ")

        tasks_file.write(f"\n{user}, {task_title}, {task_description}, {assigned_date}, {due_date}, {is_completed}")
        tasks_file.close()
        return None

def reg_user():
        credentials = False
    
        while credentials == False:
            user_file = open('user.txt', 'a+')
            new_user = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm password: ")

            if new_password != confirm_password:
                credentials = False
                print("Your passwords don't match")
            user_file.seek(0)
            
            for line in user_file:
                valid_user = line.split(',')
                if new_password == confirm_password and new_user != valid_user[0]:
                    credentials = True
                    user_file.write(f"\n{new_user}, {new_password}")
                    print("Your gredentials are updated successfully")
                    return None
                    
            if new_user == valid_user[0]:
                print("User name already exist. Try again")
                credentials = False
                user_file.seek(0)

            
        user_file.close()

def view_all():
    

        tasks_file = open('tasks.txt', 'r')
        i = 1
        for line in tasks_file:
            user, task_title, task_description, assigned_date, due_date, is_completed = line.split(", ")
            i += 1

            print(f"""
            {i})  User                : {user}
                Task title          : {task_title}
                Assigned date       : {assigned_date}
                Due date            : {due_date}
                Completion status   : {is_completed}
                Task description    : {task_description}
            """)

def view_mine():
    task_number = 0

    while task_number != -1:
        tasks_file = open('tasks.txt', 'r')
        i = 0
        for line in tasks_file:
            user, task_title, task_description, assigned_date, due_date, is_completed = line.split(", ")
            i += 1

            if username == user:
                print(f"""
                {i})  User                : {user}
                    Task title          : {task_title}
                    Task description    : {task_description}
                    Assigned date       : {assigned_date}
                    Due date            : {due_date}
                    Completion status   : {is_completed}
                """)
        task_number = int(input("Enter the number of the task you want to edit or -1 to go back to the manu: "))
        
        if task_number != -1:

            with open('tasks.txt', "r") as f:
                data = f.readlines()
                item = data[task_number - 1].split(',')

            complete = input("Do you want to mark the task as complete?(Yes/No): ")
            uppercase_complete = complete.upper()
            uppercase_Yes = item[5].upper()

            if uppercase_Yes == " YES" or uppercase_Yes == " YES\n":
                print("Selected option cannot be edited")
                return None

            if uppercase_complete != "YES" and (uppercase_Yes != " YES" or uppercase_Yes != " YES\n"):
                user = input("Edit user assigned: ")
                due_date = input("Edit due date: ")
                items = data[task_number - 1].split(',')
                items[0] = user
                items[4] = due_date
                data[task_number - 1] = str(items)[1:-1].replace('\'', ' ')
                data[task_number - 1].strip('\n')
                print("Edit was successfull")
            
            if task_number == len(data) and uppercase_complete != "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}")
                return None

            if task_number != len(data) and uppercase_complete != "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}\n")
                return None

            if uppercase_complete == "YES":
                items = data[task_number - 1].split(',')
                items[5] = "Yes"
                data[task_number - 1] = str(items)[1:-1].replace('\'', ' ')
                data[task_number - 1].strip('\n')
                print("Edit was successfull")

            if task_number == len(data) and uppercase_complete == "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}")
                return None
            
            if task_number != len(data) and uppercase_complete == "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}\n")
                return None

        if task_number == -1:
            return None
        tasks_file.close()
        return None

def generate_reports():

    x = 0
    y = 0
    z = 0
    i = 0
    a = 0
    b = 0
    c = 0
    uppercase_username = username.upper()

    with open('tasks.txt') as f:
        tasks = f.readlines()
        num_tasks = len(tasks)

        for line in tasks:
            items = line.upper().split(',')
            if items[5] == " YES\n" or items[5] == " YES":
                i += 1 #completed tasks

            if items[5] == " NO\n" or items[5] == " NO":
                x += 1 #uncompleted tasks

            date = datetime.datetime.strptime(items[4], " %d %b %Y")
            date_now = datetime.datetime.now()
            if date_now >  date and (items[5] == " NO\n" or items[5] == " NO"):
                y += 1 #over due tasks
            
            if uppercase_username == items[0]:
                z += 1 #tasks assinged to user

            if uppercase_username == items[0] and (items[5] == " YES" or items[5] == " YES\n"):
                a += 1 #tasks assigned to user and completed

            if uppercase_username == items[0] and (items[5] == " NO" or items[5] == " NO\n"):
                b += 1 #tasks assgned to user and incomplete

            if uppercase_username == items[0] and (items[5] == " NO" or items[5] == " NO\n") and date_now >  date:
                c += 1 #tasks assigned to user and incomplete and overdue
     
            percentage_incomplete = float((x/len(tasks))*100)
            percentage_overdue = float((y/len(tasks))*100)
            percentage_assined = float((z/len(tasks))*100)
            percentage_assined_complete = float((a/len(tasks))*100)
            percentage_assined_incomplete = float((b/len(tasks))*100)
            percentage_assined_incomplete_overdue = float((c/len(tasks))*100)

    f.close()

    task_overview = open('task_overview.txt', 'w+')
    task_overview.write(f"""    Total number of tasks                           : {num_tasks}
    Total number of completed tasks                 : {i}
    Totla number of uncompleted tasks               : {x}
    Total number of tasks uncomplete and overdue    : {y}
    Percentage of tasks uncomplete                  : {percentage_incomplete}
    Percentage of tasks uncompleted and overdue     : {percentage_overdue}
                        """) 
    task_overview.close()
            

    with open('user.txt', 'r') as f:
        user = f.readlines()
        users = len(user)
    
    user_overview = open('user_overview.txt', 'w+')
    user_overview.write(f"""    Total number of users                       : {users}
    Total number of tasks                       : {num_tasks}
    Tatal tasks assgined to you                 : {z}
    Percentage of tasks assigned to you         : {percentage_assined}
    Percentage of tasks you completed           : {percentage_assined_complete}
    Percentage of tasks incomplete              : {percentage_assined_incomplete}
    Percentage of tasks incomplete and overdue  : {percentage_assined_incomplete_overdue}
                        """)
    user_overview.close()

    print("Reports successfully generated")
    return None

def display():
    
    display_user = open('user_overview.txt', 'r')
    
    print("HERE IS YOUR OVERVIEW:\n")
    for line in display_user:
        print(line)

    print("HERE IS THE TASK OVERVIEW:\n")
    display_task = open('task_overview.txt', 'r')
    for line in display_task:
        print(line)
    print

    return None

# Check if the username and password are in the file

user_file = open('user.txt', 'r')
login = False

while login == False:
    choice = None
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for line in user_file:
        valid_user, valid_password = line.split(', ')

    if username != valid_user or password != valid_password:
        print("Your password or username is incorrect")
        login = False

    elif username == valid_user and password == valid_password and username != "admin":
        choice = input("""
        Please select the one of the following options:
        a   - add task
        va  - view all taskes
        vm  - view my taskes 
        e   - exit
        """)

    elif username == "admin" and password == "adm1n":
        choice = input("""
        Please select the one of the following options:
        r   - register user
        a   - add task
        va  - view all taskes
        vm  - view my taskes 
        gr  - generate reports
        ds  - display statistics
        e   - exit
        """)

    if choice == "r":
        reg_user()

    # Check the choice made and interact with the user accordingly
    elif choice == "a":
        add_task()

    elif choice == "va":
        view_all()

    elif choice == "vm":
        view_mine()

    elif choice == "gr":
        generate_reports()

    elif choice == "ds":
        display()

    elif choice == "e":
        login = True
    elif choice != "e" and choice != "vm" and choice != "va" and choice != "a" and choice != "r" and choice != None: 
        print("Your selection is incorrect try again")
    
    user_file.seek(0)

# Check if username is admin to enable user to register another user

#credentials = False


print("Have a nice day")
      


