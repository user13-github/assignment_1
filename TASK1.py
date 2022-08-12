
def my_fun5():
    to_save = f"USERNAMES :{USER_LIST}\nPASSWORDS :{PASWRD_LIST}"
    file=open('saved.txt','w')
    file.write(to_save)
    file.close()

def my_fun1():
  print('''Your password should contain atleast one uppercase character,\none lowercase character,one digit,one special character''')
  my_fun6()

def my_fun2():
  print('USERNAME DOES NOT SUPPORT')
  print('''Username should begin with alphabet, \nand must contain @ followed by . character \nFor ex:hsjs@gmail.com \nbut not "@ immediately followed by . character"''')
  my_Fun1()

def my_Fun1():
            global USERNAME
            USERNAME = input('USERNAME : ')
            h=0
            s=0
            for i in USERNAME:
                if i in '@':
                    for j in USERNAME:
                        if j in '.':
                           s+=1
            if s>0:
                k='@'
                m=USERNAME.index(k,1)
                n=USERNAME.index('.')
                if n>m and n!= m+1:
                    FORE=slice(0,m)
                    FORENAME=str(USERNAME[FORE])
                    FIRSTCHAR=FORENAME[0]
                    if FIRSTCHAR.isalpha()==True:
                        for x in USER_LIST:
                            if x != USERNAME:
                                h += 1
                        if h == len(USER_LIST):
                            USER_LIST.append(USERNAME)
                        else:
                            print('User Exist\n Try another!')
                            my_Fun1()
                        my_fun6()
                        return
                    else:
                        my_fun2()
                else:
                    my_fun2()
            else:
                my_fun2()
def my_Fun():
            global PASSWORD,USER_LIST, PASWRD_LIST
            PASSWORD = input('PASSWORD : ')
            global SIZE
            SIZE = len(PASSWORD)
def my_fun3():
            if SIZE <= 5 or SIZE >= 16:
                print('Password should contain 7-15 characters ')
                my_fun6()
def my_fun6():
    my_Fun()
    my_fun3()
    if 5 < SIZE < 16:
                    u, r, q, t, z, h = 0, 0, 0, 0, 0, 0
                    for l in range(SIZE):
                        if PASSWORD[l] in '[!@#$%^&*()_|\{}<>/*-+.]':
                            for q in range(SIZE):
                                if PASSWORD[q] in '1234567890':
                                    for r in range(SIZE):
                                        if PASSWORD[r] in 'abcdefghijklmnopqrstuvwxyz':
                                            for t in range(SIZE):
                                                if PASSWORD[t] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                                                    u += 1
                    if u > 0:
                        for y in PASWRD_LIST:
                            if y != PASSWORD:
                                z += 1
                        if z == COUNT:
                            PASWRD_LIST.append(PASSWORD)
                            print('Successfully Registered')
                            my_fun5()
                        if z == COUNT-1:
                            print("Password already exist\n Try another!")
                            my_fun6()
                    if u==0 or t == 0 or r == 0 or q == 0 or l == 0:
                          my_fun1()
def my_fun9():
        USERNAME = input('USERNAME : ')
        PASSWORD = input('PASSWORD : ')
        k=0
        usr=0
        for i in range(4):
            for j in range(4):
                if USERNAME == USER_LIST[i]:
                    usind=i
                    usr+=1
                    if j==i:
                        if PASSWORD == PASWRD_LIST[j]:
                            k+=1
        if usr==0:
            print("Wrong credential!\n Your account does not exist\n Please Register!")
            my_Fun1()
        if k==1:
            print('Login success')
        if k!=1:
            if PASSWORD != PASWRD_LIST[j]:
                            cpass = input('You have typed a wrong password\n Forgot password Y/N : ')
                            if cpass == 'Y' or cpass == 'y':
                                print('Type new password')
                                my_Fun()
                                my_fun3()
                                print('Successfully changed your password')
                            elif cpass == 'n' or cpass == 'N':
                                c = USER_LIST.index(USERNAME)
                                b = PASWRD_LIST[c]
                                print('Your password is ', b)
            elif a != USER_LIST[i]:
                    print('You do not have account!\nPlease register')
                    my_Fun1()
def my_fun8():
    SELECT=input('LOGIN/REGISTER :')
    if SELECT=='REGISTER'or SELECT=='register':
        my_Fun1()
    elif SELECT=='LOGIN' or SELECT=='login':
        my_fun9()
    else:
      print('Please type login or register')
      my_fun8()
USER_LIST = ['remya@gmail.com','somanathan@yahoo.com','rani@facebook.in','soniya@insta.in']
PASWRD_LIST = ["AB!@ab1","BC!@bc2","CD!@cd3","DE!@de4"]
COUNT=len(PASWRD_LIST)
my_fun8()


