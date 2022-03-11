usercount = int(input("Enter users count:"))
users =[]
for i in range(0,user_count):
    name=input("Enter user.name: ")
    age=input("Enter user.age: ")
    user_dict ={
        "name" : name,
        "age" : age
    }
    users.append(user_dict)
searched_name = input("Enter name to search:")

flag = False
for i in range(0,user_count):
    if users[i]["name"] == searched_name:
        print(users[i]["age"])
        flag = True
        break
if not flag:
    print("there is no user with given name!")