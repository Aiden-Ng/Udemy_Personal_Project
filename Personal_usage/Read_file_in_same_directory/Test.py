#with open("/Personal_usage/Read_file_in_same_directory/login_1.txt", "r") as file:
with open("Personal_usage/Read_file_in_same_directory/login_1.txt", "r") as file:
    # Read the first line and store it in a variable
    username = file.readline().strip()
    print(username)
    # Read the second line and store it in another variable
    password = file.readline().strip()
    print(password)
