
# =====importing libraries===========
from datetime import date

# Function definition
def menu_start():
    while True:
        # checking if the user 'admin' is the one accessing the program
        if username == "admin":
            admin_menu = input('''\nselect one of the following:
            s - statistics
            m - go to menu
            : ''').lower()

            if admin_menu == "s":
                # lists data structures to store user data
                total_num_tasks = []
                total_num_users = []

                # opening a file
                with open("tasks.txt", 'r+') as file_2:
                    information = file_2.readlines()

                    # appending user data to the lists
                    for i in information:
                        separator = i.split(",")
                        total_num_tasks.append(separator[1:2])
                        total_num_users.append(separator[:1])

                    print(f"Total number of tasks is: {len(total_num_tasks)}")
                    print(f"Total number of users is: {len(total_num_users)}")
                break
            else:
                # A menu message that provides user with different options
                # to choose from to execute a desired outcome
                menu = input('''\nSelect one of the following Options below:
                                r - Registering a user
                                a - Adding a task
                                va - View all tasks
                                vm - view my task
                                e - Exit
                                : ''').lower()

                if menu == 'r':
                    # getting user input
                    user_reg = input("Enter your name to continue: ").lower()

                    # checking if it is the right user responsible for registering the users
                    if user_reg == "admin":
                        # getting user input
                        new_username = input("Enter your username: ")
                        new_password = input("Enter your password: ")
                        confirm = input("confirm your password: ")

                        # the expression validates if the two inputted passwords
                        # are the same
                        if new_password == confirm:
                            file.write("\n" + new_username + "".join(", ") + new_password)

                            print("\nUser registered successfully.")
                        else:
                            print("The passwords doesnt match. Please try again.")
                    else:
                        print(f"{user_reg}, you are not permitted to register users.")

                    break

                elif menu == 'a':
                    # opening a file
                    with open("tasks.txt", 'a') as file_1:
                        # getting user input
                        assigned_to = input("Enter the username of the person the task is assigned to: ").lower()
                        title = input("Enter the title of the task: ").lower()
                        description = input("Enter the description of the task: ").lower()
                        date_assigned = date.today()
                        due_date = input("Enter the due date of the task: ").lower()
                        task_complete = "No".lower()

                        # writing the inputted data to a file
                        file_1.write("\n" + assigned_to.join(" ,") + title.join(" ,") + description.join(" ,") +
                                     str(date_assigned).join(" ,") + due_date.join(" ,") + " " + str(task_complete))

                        print("\nInformation added successfully.")
                        break

                elif menu == 'va':
                    # list data structures to store some data from users
                    task = []
                    description = []
                    assigned_to = []
                    date_assigned = []
                    due_date = []
                    task_complete = []

                    # opening a file
                    with open("tasks.txt", 'r+') as file_2:
                        information = file_2.readlines()

                        # appending user data to the lists
                        for i in information:
                            separator = i.split(",")
                            task.append(separator[1:2])
                            assigned_to.append(separator[:1])
                            date_assigned.append(separator[3:4])
                            due_date.append(separator[4:5])
                            task_complete.append(separator[5:6])
                            description.append(separator[2:3])

                    # displaying information to the console
                    print("\nAssigned to:")
                    for i, name in enumerate(assigned_to, 1):
                        print("{}. {}".format(i, " ".join(name)))

                    print("\nTask:")
                    for i, tsk in enumerate(task, 1):
                        print("{}. {}".format(i, " ".join(tsk)))

                    print("\nDate Assigned:")
                    for i, d_assigned in enumerate(date_assigned, 1):
                        print("{}. {}".format(i, " ".join(d_assigned)))

                    print("\nDue Date:")
                    for i, d_date in enumerate(due_date, 1):
                        print("{}. {}".format(i, " ".join(d_date)))

                    print("\nTask complete:")
                    for i, task_comp in enumerate(task_complete, 1):
                        print("{}. {}".format(i, " ".join(task_comp)))

                    print("\nDescription:")
                    for i, descrip in enumerate(description, 1):
                        print("{}. {}".format(i, " ".join(descrip)))
                    break

                elif menu == 'vm':

                    # getting user input
                    name = input("Enter the name of whom the task is assigned to: ").lower()

                    # opening a file
                    with open("tasks.txt", 'r+') as file_2:
                        information = file_2.readlines()

                        # displaying information associated with the user's inputted data to the console
                        for line_num in information:
                            if line_num.startswith(name.replace(name, " " + name)):
                                print(line_num)
                        break

                elif menu == 'e':
                    print('Goodbye!!!')
                    # exiting the program
                    exit()
                else:
                    print("You have made a wrong choice, Please Try again")


# ======Login section========
# getting user input
print("Please enter your login credentials.")
username = input("Enter your username: ").lower()
password = input("Enter your password: ").lower()

# opening a file to search and validate if the login credentials are correct
with open("user.txt", 'r+') as file:
    info = file.read()

    for line in info:
        if username in line and password in line:
            menu_start()
        else:
            print("Incorrect login credentials. Please try again.")
        break
