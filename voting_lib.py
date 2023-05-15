from colorama import Fore, Back

class Voting:
    def __init__(self, point_money=500):
        print(Back.BLACK)
        print(Fore.MAGENTA + "Initializing all data" + Fore.RESET)
        self.students = {0: {"name": "Kenedy", "mark": 0, "voter": []},
                         1: {"name": "Merry", "mark": 0, "voter": []},
                         2: {"name": "Penny", "mark": 0, "voter": []},
                         3: {"name": "Paul", "mark": 0, "voter": []},
                         4: {"name": "Mike", "mark": 0, "voter": []}}
        self.db:dict = {}
        self.p_money = point_money
        self.loadingAllData()

    def main_option(self):
        print(Fore.YELLOW+"***** Main Page *****"+Fore.RESET)
        option = 0
        try:
            option = int(input("Press "+Fore.BLUE+"1"+Fore.RESET+" to register, "
                               "Press "+Fore.BLUE+"2"+Fore.RESET+" to login, "
                               "and "+Fore.BLUE+"3"+Fore.RESET+" to exit: "))
            if option == 1:
                self.register()
            elif option == 2:
                self.login()
            elif option == 3:
                self.exitProgram()
            else:
                print(Fore.RED+"Invalid Option"+Fore.RESET)
                self.main_option()
        except ValueError:
            print(Fore.RED+"Only numbers are allowed"+Fore.RESET)  
            self.main_option() 

    def register(self):
        print(Fore.YELLOW+"***** Registeration *****"+Fore.RESET)
        while True:
            email_in = input("%-20s: "%("Enter EMAIL"))
            if self.is_email_existed(email_in) == -1:
                break
            else:
                print(Fore.RED+"EMAIL already existed"+Fore.RESET)
        name_in = input("%-20s: "%("Enter NAME"))
        while True:
            phone_in = input("%-20s: "%("Enter PH NO"))
            if self.is_phone_existed(phone_in) == -1:
                break
            else:
                print(Fore.RED+"PHONE NO already existed"+Fore.RESET)
        addr_in = input("%-20s: "%("Enter ADDRESS"))
        while True:
            pass_in_1 = input("%-20s: "%("Enter PASSWORD"))
            pass_in_2 = input("%-20s: "%("Confirm PASSWORD"))
            if pass_in_2 == pass_in_1:
                break
            else:
                print(Fore.RED+"PASSWORD Not Matched"+Fore.RESET)
        money_in = 0
        while True:
            try:
                money_in = int(input("%-20s: "%("Insert MONEY")))
                break
            except ValueError:
                print(Fore.RED+"Only numbers are allowed"+Fore.RESET)
        uid = len(self.db)
        data_form:dict = {uid: {"email": email_in, "name": name_in, "phone": phone_in,
                                "addr": addr_in, "password": pass_in_1, "money": money_in, "point": 0}}
        self.db.update(data_form)
        print(Fore.CYAN+"Registration succeeded"+Fore.RESET)
        option = 0
        while True:
            try:
                option = int(input("Press "+Fore.BLUE+"1"+Fore.RESET+" to login, "
                                "Press "+Fore.BLUE+"2"+Fore.RESET+" to main, "
                                "and "+Fore.BLUE+"3"+Fore.RESET+" to exit: "))
                if option == 1:
                    self.login()
                    break
                if option == 2:
                    self.main_option()
                    break
                if option == 3:
                    self.exitProgram()
                else:
                    print(Fore.RED+"Invalid Option"+Fore.RESET)
            except ValueError:
                print(Fore.RED+"Only numbers are allowed"+Fore.RESET)  

    def login(self):
        print(Fore.YELLOW+"***** Login Section *****"+Fore.RESET)
        db_len = len(self.db)
        u_id = -1
        while True:
            email_in = input("%-20s: "%("Enter EMAIL"))
            pass_in = input("%-20s: "%("Enter PASSWORD"))
            u_id = self.is_email_existed(email_in)
            if u_id != -1:
                if pass_in == self.db[u_id]["password"]:
                    break
                else:
                    print(Fore.RED+"PASSWORD not correct"+Fore.RESET)
            else:
                print(Fore.RED+"EMAIL not existed"+Fore.RESET)
        self.user_sector(u_id)

    def user_sector(self, u_idx):
        print(Fore.YELLOW+f"WELCOME, {self.db[u_idx]['name']}"+Fore.RESET)
        while True:
            try:
                option = int(input("Press "+Fore.BLUE+"1"+Fore.RESET+" to vote, "
                                "Press "+Fore.BLUE+"2"+Fore.RESET+" to buy points, "
                                "Press "+Fore.BLUE+"3"+Fore.RESET+" to inset money, "
                                "Press "+Fore.BLUE+"4"+Fore.RESET+" to check points, "
                                "Press "+Fore.BLUE+"5"+Fore.RESET+" to main, "
                                "and "+Fore.BLUE+"6"+Fore.RESET+" to exit: "))
                if option == 1:
                    print("Vote Someone")
                    for i in range(len(self.students)):
                        print(f'Id:{i}, Name: {self.students[i]["name"]:<10}, Current vote marks: {self.students[i]["mark"]:<3}')
                    while True:
                        try:
                            v_id = int(input("Enter ID number to vote: "))
                            if v_id > -1 and v_id < len(self.students):
                                if self.db[u_idx]["point"] > 0:
                                    self.db[u_idx]["point"] -= 1
                                    self.students[v_id]["mark"] += 1
                                    self.students[v_id]["voter"].append(self.db[u_idx]["name"])
                                    print(f"You voted {self.students[v_id]['name']}")
                                    print(f"Current voting marks: {self.students[v_id]['mark']}")
                                    print("Voters:")
                                    for i in range(len(self.students[v_id]["voter"])):
                                        print("   "+self.students[v_id]['voter'][i])
                                    break
                                else:
                                    print(Fore.RED+"You don't have enough points to vote"+Fore.RESET)
                                    break
                            else:
                                print(Fore.RED+"INVALID Option"+Fore.RESET)
                        except ValueError:
                            print(Fore.RED+"Only numbers are allowed"+Fore.RESET)    
                elif option == 2:
                    print("Buy some points [1 point = 500USD]")
                    while True:
                        try:
                            point_in = int(input("How many points?: "))
                            r_money = point_in * self.p_money
                            if r_money <= self.db[u_idx]["money"]:
                                self.db[u_idx]["money"] -= r_money
                                self.db[u_idx]["point"] += point_in
                                print("You've got {} points".format(self.db[u_idx]["point"]))
                                break
                            else:
                                print(Fore.RED+"You don't have enough money to buy points"+Fore.RESET)
                                break
                        except ValueError:
                            print(Fore.RED+"Only numbers are allowed"+Fore.RESET)
                elif option == 3:
                    print("Fill up some money [Basic 500USD per point]")
                    while True:
                        try:
                            money_fill = int(input("Insert your money: "))
                            self.db[u_idx]["money"] += money_fill
                            print("Your total money: {}".format(self.db[u_idx]["money"]))
                            break
                        except ValueError:
                            print(Fore.RED+"Only numbers are allowed"+Fore.RESET)
                elif option == 4:
                    print("%-20s: {}".format(self.db[u_idx]["point"]) %("POINTS left"))
                    print("%-20s: {}".format(self.db[u_idx]["money"]) %("MONEY left"))
                elif option == 5:
                    self.main_option()
                elif option == 6:
                    self.exitProgram()
                else:
                    print(Fore.RED+"INVALID OPTION"+Fore.RESET)
            except ValueError:
                print(Fore.RED+"Only numbers are allowed"+Fore.RESET)

    def exitProgram(self):
        self.recordingAllData()
        print(Back.RESET)
        exit(0)

    def is_email_existed(self, u_email):
        db_len = len(self.db)
        for idx in range(db_len):
            if u_email == self.db[idx]["email"]:
                return idx
        return -1
    
    def is_phone_existed(self, u_phone):
        db_len = len(self.db)
        for idx in range(db_len):
            if u_phone == self.db[idx]["phone"]:
                return idx
        return -1

    def recordingAllData(self):
        print(Fore.YELLOW+"****** Recording *****"+Fore.RESET)
        fp = open("program_data.dat", "w")
        student_count = len(self.students)
        for idx in self.students: #id,name,mark,voter1|voter2|voter3
            fp.write(f'{student_count-(idx+1)},{self.students[idx]["name"]},{self.students[idx]["mark"]}')
            voter_count = len(self.students[idx]["voter"])
            if voter_count > 0:
                fp.write(',')
            for i,voter in enumerate(self.students[idx]["voter"]):
                fp.write(voter)
                if i+1 < voter_count:
                    fp.write('|')
            fp.write('\n')
        user_count = len(self.db)
        for idx in self.db: #no,email,name,phone,address,password,money,point
            fp.write(f'{user_count-(idx+1)},{self.db[idx]["email"]},{self.db[idx]["name"]},{self.db[idx]["phone"]},')
            fp.write(f'{self.db[idx]["addr"]},{self.db[idx]["password"]},{self.db[idx]["money"]},{self.db[idx]["point"]}\n')
        fp.close()
        print(Fore.YELLOW+"DONE!"+Fore.RESET+Back.RESET)

    def loadingAllData(self):
        try:
            print(Fore.YELLOW+"***** Loading Data *****"+Fore.RESET)
            file_buffer = []
            fp = open("program_data.dat", "r")
            for line in fp:
                file_buffer.append(line.strip().split(','))
            fp.close()
            max_id = -1
            flip = False
            for ele in file_buffer:
                if not flip: #id,name,mark,voter1|voter2|voter3
                    if max_id == -1:
                        max_id = int(ele[0])
                    self.students[max_id-int(ele[0])]["mark"] = int(ele[2])
                    try:
                        voters = ele[3].strip().split('|') #voters list
                        for voter in voters:
                            self.students[max_id-int(ele[0])]["voter"].append(voter)
                    except IndexError:
                        pass
                    if int(ele[0]) == 0:
                        flip = True
                        max_id = -1
                else: #no,email,name,phone,address,password,money,point
                    if max_id == -1:
                        max_id = int(ele[0])
                    profile = {max_id-int(ele[0]): {"email": ele[1], "name": ele[2], "phone": int(ele[3]), "addr": ele[4],
                                                    "password": ele[5], "money": int(ele[6]), "point": int(ele[7])}}
                    self.db.update(profile)
        except FileNotFoundError:
            print(Fore.YELLOW+"Initial empty dataBase, Cool!"+Fore.RESET)