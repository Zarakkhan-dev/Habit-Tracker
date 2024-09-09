from datetime import datetime
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Registration:
    def __init__(self):
        self.users = []

    def Signup(self, username, password):
        for user in self.users:
            if username == user.username:
                return "User already exists"
        new_user = User(username, password)
        self.users.append(new_user)
        return "Registered successfully"

    def Login(self, user_name, user_password):
        for user in self.users:
            if user_name == user.username and user_password == user.password:
                return "Login successfully"
        return "Invalid username or password"

class Habit:
    def __init__(self, name, frequency,username):
        self.username = username;
        self.name = name
        self.frequency = frequency
        self.progress = []
        self.timestamp = datetime.now()

    def add_completion(self, date):
        self.progress.append(date)

    def display_progress(self):
        print(f"Habit: {self.name}")
        print("Progress:")
        for date in self.progress:
            print(date)


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, frequency,username ):
        habit = Habit(name, frequency,username)
        self.habits.append(habit)
        print(f"Added habit: {name}")

    def log_completion(self, habit_name ,date,username):
        habit = self.find_habit(habit_name,username)
        if habit:
            habit.add_completion(date)
            print(f"Logged completion for habit '{habit_name}' on {date}")
        else:
             print(f"Habit '{habit_name}' not found")
       
    def find_habit(self, habit_name,username):
        for habit in self.habits:
            if (habit.name.lower() == habit_name.lower() and habit.username ==username ):
                return habit
        return None

    def display_all_habits_progress(self,username):
        
        for habit in self.habits:
            if(username ==habit.username):
                print("Habit Progress:")
                habit.display_progress()


login_system = Registration()
habit = HabitTracker()
while True:
    print("------------------------------")
    print("        Login System  ")
    print("------------------------------")
    print("      1: Registration ")
    print("      2: Login ")
    print("      e: Exit  ")
    print("------------------------------")
    login_selection = input("Select an Option: ")
    if login_selection == '1':
        print("")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        response = login_system.Signup(username, password)
        print(response)
    elif login_selection == '2':
        print("")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        response = login_system.Login(username, password)
        print("")
        if(response == "Login successfully"):
            print(response)
            while True:
                print("------------------------------")
                print("            Menu  ")
                print("------------------------------")
                print("       1: Add Habit ")
                print("       2: Habit Completed ")
                print("       3: Find Habit  ")
                print("       4: Display Habit  ")
                print("       5: Exit   ")
                print("------------------------------")
                user_selection = input("Select The One Option : ")
                if(user_selection == '1'):
                    print()
                    habit_name = input("Enter The habit name  : ");
                    frequency = input("Enter The Habit Frequency : ")
                    habit.add_habit(habit_name,frequency,username)
                elif(user_selection == '2'):
                    completed_habit = input("Enter The Habit due want to completed : ");
                    my_current_date = datetime.now();
                    habit.log_completion(completed_habit,my_current_date,username);
                elif(user_selection=='3'):
                    find_habit = input("Enter The Habit due want to find out : ");
                    single_habit =habit.find_habit(find_habit,username)
                    print(f'Habit Name is {single_habit.name} and frequency is {single_habit.frequency}')
                elif(user_selection == '4'):
                    habit.display_all_habits_progress(username);
                elif(user_selection == '5'):
                    break
                else:
                    print("Invalid inputs")
    

    elif login_selection == 'e':
        break

    else:
        print("Invalid Selection")
