# from pyfiglet import Figlet as fig

# f = fig(font='isometric3',width=100)
# print(f.renderText("User Name Creator!"))

userName = input("Enter your first and last name: ").split()
#username = userName.split()
print()
print(f"your username is {userName[0][0]}{userName[1][0:7]}")