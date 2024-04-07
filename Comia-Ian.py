# Comia, Ian Emmanuel M. 
# CS - 1201
# Messenger

messages = {
    "a" : {"Messages" : ["\n\t\t\t\tpatambay sa dorm \n\t\t\t\t-b"]}, 
    "b" : {"Messages" : []},
    "c" : {"Messages" : []},
    "d" : {"Messages" : []}
                }

user_account = {"a" : {"Password" : "a", "Friends" : ['b', 'c', 'd'], "active" : False, "Block" : []},
                "b" : {"Password" : "b", "Friends" : ['c'], "active" : False, "Block" : []},
                "c" : {"Password" : "c", "Friends" : [], "active" : False, "Block" : []},
                "d" : {"Password" : "d", "Friends" : ['c'], "active" : False, "Block" : []}
                }

user_info = {"a" : {"Bio" : "No Bio Yet"},
             "b" : {"Bio" : "No Bio Yet"},
             "c" : {"Bio" : "No Bio Yet"},
             "d" : {"Bio" : "No Bio Yet"},
             }

def main():
    print("\n\t\t\t\tWelcome to Messenger")
    while True:
        try:
            print("\n\t\t\t1. Log In")
            print("\n\t\t\t2. Sign Up")
            print("\n\t\t\t3. Exit")

            choice = int(input("\n\t\t\tEnter Choice: "))

            if choice == 1:
                login()
            elif choice == 2:
                signup()
            elif choice == 3:
                exit()
            else:
                main()
        except ValueError as e:
            main()

def login():
    print("\n\t\t\t\t---Log In---")
    while True:
        try:
            username = input("\n\t\t\tEnter username: ")
            if not username:
                main()
            password = input("\n\t\t\tEnter password: ")
            if user_account.get(username) and user_account[username]['Password'] == password:
                print("\n\t\tLogin Successful")
                user_account[username]["active"] = True
                usermain(username)
            else:
                print("\n\t\t\tInvalid username or password")
        except ValueError as e:
            print(e)
            main()

def signup():
    print("\n\t\t\t\t---Messenger Sign Up---")
    while True:
        try:
            username = input("\n\t\t\tEnter Username: ")
            if not username:
                main()
            elif username in user_account:
                print("\n\t\t\tUsername already exists. Try another username.")
                continue
            while True:
                try: 
                    password = input("\n\t\t\tInput password (at least 8 characters): ")
                    if len(password) < 7:
                        print("\n\t\t\tPassword is not at least 8 characters")
                        continue
                    elif len(password) > 7:
                        user_account[username] = {"Password" : password, "Friends" : [], "active" : False, "Block" : []} 
                        messages[username] = {"Messages" : []} 
                        user_info[username] = {"Bio" : "No Bio Yet"}
                        print("\n\t\t\tSign Up successful!")
                        main()
                    else:
                        print("\n\t\t\tInvalid input.")
                        continue 
                except ValueError as e:
                    signup()   
        except ValueError as e:
            signup()

def view_user_profile(username):
    print("\n\t\t\t\t---User Profile---")
    while True:
        try:
            print(f"\n\t\t\tUsername: {username}")
            print(f"\n\t\t\t{user_info[username]["Bio"]}")

            print(f"\n\t\t\t{username}'s Friends:  ")
            for friends in user_account[username]["Friends"]:
                print(f"\n\t\t\t{friends}")

            choice = int(input("\n\t\t\t1. Go back to main\n\n\t\t\t2. Edit profile\n\n\t\t\tChoice: "))
            if choice == 1:
                usermain(username)
            elif choice == 2:
                edit_user_profile(username)
            else:
                view_user_profile(username)
        except ValueError as e:
            view_user_profile(username)

def edit_user_profile(username):
    print("\n\t\t\t\tEdit User Profile")
    while True: 
        try:
            print("\n\t\t\tWhat would you like to change? ")
            print("\n\t\t\t1. Username")
            print("\n\t\t\t2. Bio")
            choice = int(input("\n\t\t\tChoice: "))

            if not choice:
                view_user_profile(username)
            elif choice == 1:
                new_username = str(input("\n\t\t\tEnter new Username: "))
                if new_username in user_account:
                    print("\n\t\t\tUsername Taken. Try again")
                    edit_user_profile(username)
                else:
                    confirmation = str(input("\n\t\t\tAre you sure you want to continue? y/n: "))

                    if confirmation == 'y':
                        user_account[new_username] = user_account.pop(username)
                        user_info[new_username] = user_info.pop(username)
                        messages[new_username] = messages.pop(username)
                        print("\n\t\t\tUsername changed successfully.")

                        for friend in user_account:
                            if username in user_account[friend]['Friends']:
                                res = [sub.replace(username, new_username) for sub in user_account[friend]["Friends"]]
                                user_account[friend]["Friends"] = res
                            else:
                                continue
                        username = new_username
                        edit_user_profile(username)
                    else:
                        edit_user_profile(username)
            elif choice == 2:
                new_bio = str(input("\n\t\t\tEnter new bio: "))
                confirmation = str(input("\n\t\t\tAre you sure you want to continue? y/n: "))
                if confirmation == 'y':
                    user_info[username]["Bio"] = new_bio
                    print("\n\t\t\tBio changed successfully.")
                    edit_user_profile(username)
                else:
                    edit_user_profile(username)
            else:
                edit_user_profile(username)
        except ValueError as e:
            view_user_profile(username)

def view_messenger_users_profile(username):
    for user in user_account:
        print(f"\n\t\t\t{user}")
    who = str(input("\n\t\t\tEnter the username of the user you want to view the profile: "))
    while True:
        if not who:
            usermain(username)
        elif who in user_account:
            print(f"\n\t\t\t{who}'s Profile")
            print(f"\n\t\t\tUsername: {who}")
            print(f"\n\t\t\tBio: {user_info[who]["Bio"]}")
            print(f"\n\t\t\t{who}'s Friend List: ")
            for friend in user_account[who]["Friends"]:
                print(f"\n\t\t\t{friend}")
            choice = str(input("\n\t\t\tWould you like to go back? y/n: "))
            if choice == 'y':
                usermain(username)
            else:
                view_messenger_users_profile(username)
        elif who not in user_account:
            print("\n\t\t\tAccount doesn't exist. Try Again")
            view_messenger_users_profile(username)
        else:
            print("Invalid Input")

def block_user(username):
    print("\n\t\t\t\t---Messenger users--- ")
    for user in user_account:
        print(f"\n\t\t\t{user}")
    
    choice = int(input("\n\t\t\t1. Block a user\n\n\t\t\t2. Unblock a user\n\n\t\t\tChoice: "))

    if choice == 1:
        block_who = input("\n\t\t\tEnter username of the user you want to block: ")
        if not block_who:
            usermain(username)
        elif block_who in user_account[username]["Block"]:
            print("\n\t\t\tUser already blocked.")
            block_user(username)
        elif block_who not in user_account[username]["Block"]:
            confirmation = str(input(f"\n\t\t\tAre you sure you want to block {block_who}? y/n: "))
            if confirmation == 'y':
                user_account[username]["Block"].append(block_who)
                print(f"\n\t\t\t{block_who} blocked. He/She cant message you now.")
            elif confirmation == 'n':
                block_user(username)
            else:
                block_user(username)
        else:
            block_user(username)
    elif choice == 2:
        print("\n\t\t\tUsers you blocked")
        for blocked in user_account[username]["Block"]:
            print(f"\n\t\t\t{blocked}")
        
        unblock_who = str(input("\n\t\t\tEnter the username of the user you want to unblock: "))

        if not unblock_who:
            usermain(username)
        elif unblock_who not in user_account[username]["Block"]:
            print("\n\t\t\tUser not blocked.")
            block_user(username)
        elif unblock_who in user_account[username]["Block"]:
            user_account[username]["Block"].remove(unblock_who)
            print(f"\n\t\t\t{unblock_who} unblocked. He/She can message you now.")
            block_user(username)

def usermain(username):
    print(f"\n\t\t\t\t---Welcome {username}---")
    while True:
        try:
            if user_account[username]['active'] == True:
                print("\n\t\t\tOnline")
            else:
                print("\n\t\t\tOffline")

            for friends in user_account[username]['Friends']:
                if user_account[friends]['active'] == True:
                    print(f"\n\t\t\t{friends}: Online")
                else:
                    print(f"\n\t\t\t{friends}: Offline")

            print("\n\t\t\t1. Display Messages")
            print("\n\t\t\t2. Send Message")
            print("\n\t\t\t3. Add a Friend")
            print("\n\t\t\t4. Unfriend")
            print("\n\t\t\t5. User Profile")
            print("\n\t\t\t6. View other users profile")
            print("\n\t\t\t7. Block a user")
            print("\n\t\t\t8. Log out")

            choice = int(input("\n\n\t\t\tEnter Choice: "))

            if choice == 1:
                display_messages(username)
            elif choice == 2:
                send_message(username)
            elif choice == 3:
                add_friend(username)
            elif choice == 4:
                remove_friend(username)
            elif choice == 5:
                view_user_profile(username)
            elif choice == 6:
                view_messenger_users_profile(username)
            elif choice == 7:
                block_user(username)
            elif choice == 8:
                print("\n\t\t\tSigning Out...")
                main()
            else:
                print("\n\t\t\tInvalid Input")
        except ValueError as e:
            main()

def add_friend(username):
    print("\n\t\t\t---Add a Friend---")
    print("\n\t\t\t---Messenger Users---")

    for key, value in user_account.items():
        print(f"\n\t\t\t{key}")
    while True:
        try:            
            who_to_add = str(input("\n\t\t\tEnter the username of the user you want to add: "))

            if not who_to_add:
                usermain(username)
            elif who_to_add == username:
                print("\n\t\t\tYou can't add yourself")
                add_friend(username)
            elif who_to_add not in user_account:
                print("\n\t\t\tUser does not Exist. Try Again")
                add_friend(username)
            elif who_to_add in user_account[username]["Friends"]:
                print("\n\t\t\tUser is already your friend.")
                add_friend(username)
            elif who_to_add not in user_account[username]["Friends"]:
                confirmation = str(input("\n\t\t\tPress y to continue: "))
                if confirmation == 'y':
                    add = user_account[username]["Friends"]
                    add.append(who_to_add)

                    print(f"\n\t\t\tSuccessfully added {who_to_add}. You can now send messages to {who_to_add}")

                    print("\n\t\t\tUpdated Friends List")
                    for friends in user_account[username]['Friends']:
                        print(friends)
                    usermain(username)
                else:
                    add_friend(username)
            else:
                print("\n\t\t\tInvalid Input. Try Again.")
                add_friend(username)
        except ValueError as e:
            usermain(username)

def remove_friend(username):
    print("\n\t\t\t\t---Unfriend---")
    while True:
        try:
            user = str(input("\n\t\t\tEnter the username of the user you want to unfriend: "))

            if user in user_account and user not in user_account[username]["Friends"]:
                print("\n\t\t\tUser is not on your Friends list")
                remove_friend(username)
            elif user not in user_account:
                print("\n\t\t\tUser does not exist")
            elif not user:
                usermain(username)
            elif user in user_account[username]["Friends"]:
                choice = str(input(f"\n\t\t\tAre you sure you want to unfriend {user}? y/n: "))
                if choice == 'y':
                    to_unfriend = user_account[username]["Friends"]
                    to_unfriend.remove(user)

                    print(f"\n\t\t\tYou've unfriended {user}")

                    print("\n\t\t\tUpdated Friends List")
                    for friends in user_account[username]['Friends']:
                        print(friends)
                    usermain(username)
                elif choice == 'n':
                    remove_friend(username)
                else:
                    remove_friend(username)
            else:
                remove_friend(username)
        except ValueError as e:
            usermain(username)          

def send_message(username):
    print("\n\t\t\t\t---Send a message---")
    while True:
        receiver = input("\n\t\t\tEnter the usename of the use you want to send a message to: ")

        if not receiver:
            usermain(username)
        elif username in user_account[receiver]["Block"]:
            print("\n\t\t\tThis user is not available.")
            send_message(username)
        elif receiver not in user_account[username]["Friends"]:
            print(f"\n\t\t\t{receiver} is not on your friends list. ")
            send_message(username)
        elif receiver not in messages:
            print("\n\t\t\tInvalid User. Try again")
            send_message(username)
        elif receiver in messages:
            input_message = str(input("\n\t\t\tEnter your message here: "))
            message += str(f"\n\t\t\t\t{input_message}\n\t\t\t\t-{username}")
            user = messages[receiver]["Messages"]
            user.append(message)
            print("\n\t\t\tMessage Sent.")
            usermain(username)
        else:
            print("\n\t\t\tTry Again")
            send_message(username)

def display_messages(username):
    print("\n\t\t\tHere are/is your latest message: ")
    while True:
        try:
            for message in messages[username]["Messages"]:
                print(message)
            choice = int(input("\n\t\t\t1. Send a reply\n\n\t\t\t2.Go back\n\n\t\t\tChoice: "))
        
            if not choice:
                usermain(username)
            elif choice == 1:
                send_message(username)
            elif choice == 2:
                usermain(username)
            else:
                print("\n\t\t\tInvalid Input Try again")
                display_messages(username)
        except ValueError:
            usermain(username)
main()

