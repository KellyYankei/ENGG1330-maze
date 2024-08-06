def welcome():
    print()
k0 = open('sokobanmap.txt','r')
k1 = k0.read()
k2 = k1.splitlines()
no_0,list2,step,return_can,push= True,[],"",True,False
for i in k2:
    list1 = []
    for a in i:
        list1.append(a)
    list2.append(list1)
# 需要 改退出方式 选择关卡（加地图）
def printboard():
    for i in list2:
        for a in range(len(i)):
            if i[a] == "*":
                i[a] = "\033[32;42m·\033[0m"
            elif i[a] == "0":
                i[a] = "\033[1m0\033[0m"
            elif i[a] == "P":
                i[a] = "\033[1;33mP\033[0m"
            elif i[a] == "&":
                i[a] = "\033[34m&\033[0m"
            elif i[a] == "@":
                i[a] = "\033[36m@\033[0m"
        print("".join(i))
    for i in list2:
        for a in range(len(i)):
            if i[a] == "\033[32;42m·\033[0m":
                i[a] = "*"
            elif i[a] == "\033[1m0\033[0m":
                i[a] = "0"
            elif i[a] == "\033[1;33mP\033[0m":
                i[a] = "P"
            elif i[a] == "\033[34m&\033[0m":
                i[a] = "&"
            elif i[a] == "\033[36m@\033[0m":
                i[a] = "@"
def printmove(i):
    clear_screen()
    global step
    step = i
    if i == 'w': print('Making Move: N')
    if i == 'a': print('Making Move: W')
    if i == 's': print('Making Move: S')
    if i == 'd': print('Making Move: E')
    return step
def keep_0_there1(s2,p1):
    global list1,list2,no_0,return_can
    while list2[s2][p1]== 'P':
        no_0 = False
        printboard()
        inp = input("Your Move [w,a,s,d,q]: ")
        if inp == "q":
            time_list.append(time.time())
            used_time = time_list[-1] - time_list[0]
            used_time = round(used_time,0)
            game_win = False
            print("That's the first game, go for the next game")
            break
        elif inp == 'return':
            if return_can == True:
                if step == 'w': list2[s2+1][p1],return_can = 'P',False
                if step == 's': list2[s2-1][p1],return_can = 'P',False
                if step == 'a': list2[s2][p1+1],return_can = 'P',False
                if step == 'd': list2[s2][p1-1],return_can = 'P',False
                break
            else: 
                print("You have already returned once, and there's no more chance")
                continue
        else:
            printmove(inp)
            makemove(inp)
    list2[s2][p1],no_0='0',True
def stepmove_updown(s1,s2,s3,p1): # (s1,p1) is the location of the player, and (s2,p1),(s3,p1) is the respectively the place that changed by the movement
    global list1,list2,push
    if list2[s2][p1]==' ':  
        list2[s1][p1],list2[s2][p1],push=" ",'P',False
    elif list2[s2][p1]=='&':
        if list2[s3][p1]==" ":
            list2[s3][p1],list2[s2][p1],list2[s1][p1],push="&",'P',' ',True
        elif list2[s3][p1]=="0":
            list2[s3][p1],list2[s2][p1],list2[s1][p1],push='@','P',' ',True
    elif list2[s2][p1]=='0':
        if no_0 == True:
            list2[s2][p1],list2[s1][p1],push='P'," ",False
        else:
            list2[s2][p1],list2[s1][p1],push='P',"0",False
        keep_0_there1(s2,p1)
    elif list2[s2][p1] == "@":
        if list2[s3][p1]==" ":
            list2[s3][p1],list2[s2][p1],list2[s1][p1],push="&",'P',' ',True
            keep_0_there1(s2,p1)
        elif list2[s3][p1]=="0":
            list2[s3][p1],list2[s2][p1],list2[s1][p1],push='@','P',True
            if no_0 == True:
                list2[i][p1] = " "
            else:
                list2[i][p1] = "0"
            keep_0_there1(i,p2)
def stepmove_leftright(i,p1,p2,p3):
    global list1,list2
    if list2[i][p2]==' ':
        list2[i][p1],list2[i][p2],push=" ",'P',False
    elif list2[i][p2]=='&':
        if list2[i][p3]==" ":
            list2[i][p3],list2[i][p2],list2[i][p1],push="&",'P',' ',True
        elif list2[i][p3]=="0":
            list2[i][p3],list2[i][p2],list2[i][p1],push='@','P',' ',True
    elif list2[i][p2]=='0':
        if no_0 == True:
            list2[i][p2],list2[i][p1],push='P'," ",False
        else:
            list2[i][p2],list2[i][p1],push='P',"0",False
        keep_0_there1(i,p2)   
    elif list2[i][p2] == "@":
        if list2[i][p3]==" ":
            list2[i][p3],list2[i][p2],list2[i][p1],push="&",'P',' ',True
            keep_0_there1(i,p2)
        elif list2[i][p3]=="0":
            list2[i][p3],list2[i][p2],push='@','P',True
            if no_0 == True:
                list2[i][p1] = " "
            else:
                list2[i][p1] = "0"
            keep_0_there1(i,p2)

def makemove(m):
    global list1,list2
    for b in range(len(list2)):
        if 'P' in list2[b]:
            i = b
            p1 = list2[i].index('P')
    if m == 'w': stepmove_updown(i,i-1,i-2,p1)
    elif m == 's': stepmove_updown(i,i+1,i+2,p1)
    elif m == 'a': stepmove_leftright(i,p1,p1-1,p1-2)
    elif m == 'd': stepmove_leftright(i,p1,p1+1,p1+2)
def count_X(x,y):
    list3,t = [],0
    for i in range(len(list2)):
        for y1 in range(len(list2[i])):
            if list2[i][y1] == '*': list3.append((i,y1))
    for a1,a2 in list3:
        if a1 == x+1 and a2 == y: t+=1
        if a1 == x-1 and a2 == y: t+=1
        if a1 == x and a2 == y+1: t+=1
        if a1 == x and a2 == y-1: t+=1
    return t
def return_move_leftright(s1,p1,p2,p3):
    global list1,list2,return_can,push
    if list2[s1][p3]=='&':
        if push == True:
            list2[s1][p1],list2[s1][p2],list2[s1][p3],return_can,push = '&','P',' ',False,False
        else:
            list2[s1][p1],list2[s1][p2],list2[s1][p3],return_can = ' ','P','&',False
    if list2[s1][p2]==' ': list2[s1][p1],list2[s1][p2],return_can = " ",'P',False
    if list2[s1][p2]=='0':
        list2[s1][p2],list2[s1][p1],return_can='P'," ",False
        keep_0_there1(s1,p2)
    if list2[s1][p3] == "@": list2[s1][p3],list2[s1][p1],list2[s1][p2],return_can='0','&','P',False
def return_move_updown(s1,s2,s3,p1):
    global list1,list2,return_can,push
    if list2[s3][p1]=='&': 
        if push == True:
            list2[s1][p1],list2[s2][p1],list2[s3][p1],return_can,push = '&','P',' ',False,False
        else:
            list2[s1][p1],list2[s2][p1],list2[s3][p1],return_can = ' ','P','&',False
    if list2[s2][p1]==' ': list2[s1][p1],list2[s2][p1],return_can =" ",'P',False
    if list2[s2][p1]=='0':
        list2[s2][p1],list2[s1][p1],return_can='P'," ",False
        keep_0_there1(s2,p1)
    if list2[s3][p1] == "@": list2[s3][p1],list2[s1][p1],list2[s2][p1],return_can='0','&','P',False
def clear_screen():
    import os
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')
def return_last_step():
    for b in range(len(list2)):
        if 'P' in list2[b]:
            i = b
            p = list2[i].index('P')
    if step == 'w': 
        return_move_updown(i,i+1,i-1,p)
        clear_screen()
    elif step == 's': 
        return_move_updown(i,i-1,i+1,p)
        clear_screen()
    elif step == 'a': 
        return_move_leftright(i,p,p+1,p-1)
        clear_screen()
    elif step == 'd': 
        return_move_leftright(i,p,p-1,p+1)
        clear_screen()
    elif step == '': 
        print("You even don't have your first step!")
def check_stalemate():
    t = 0
    for i in range(len(list2)):
        for a in range(len(list2[i])):
            if list2[i][a] == "&":
                if count_X(i,a) >=2:
                    t +=1
    if t >0: return True
    else: return False
def checkfinish():
    t = 0
    for i in list2:
        t += i.count("0")
    if t == 0: return True
    else: return False
def notice():
        print('''\033[1;31mNotice\033[0m
\033[1;31mYou must push all the boxs to the correct positions or else the boxes would not disappear\033[0m
\033[34mfor boxes not at the right place\033[0m:\033[34m&\033[0m   
\033[36mfor boxes at the right place\033[0m:\033[36m@\033[0m  
\033[1mfor the place which boxes need to be at\033[0m:\033[1m0\033[0m  
\033[1;33mplayer\033[0m:\033[1;33mP\033[0m
to quit the game,input:"\033[1;4mq\033[0m"
if you want to return to the last step, input:"\033[1;4mreturn\033[0m", but you only had \033[1;4m1\033[0m attempt per step, be caution!''')
def main():
    welcome()
    # return True,0
    global time_list,game_win,used_time
    import time
    time_list,used_time = [],0
    time_list.append(time.time())
    print('''>>An old lady appeared, she asked you to help her put the boxs to the right positions. Please help her''')
    notice()
    while True:
        printboard()
        game_win = True
        used_time = 0
        inp = input("Your Move [wasdq]: ")
        if inp == "q":
            time_list.append(time.time())
            used_time = time_list[-1] - time_list[0]
            used_time = round(used_time,0)
            game_win = False
            print('You failed to help the old lady, she angrily left.')
            break
        elif inp == 'return':
            if return_can == True:
                return_last_step()
            else:
                print("You have already returned once, and there's no more chance")
            continue
        else:
            step = printmove(inp)
            makemove(inp)
            if checkfinish():
                printboard()
                time_list.append(time.time())
                used_time = time_list[-1] - time_list[0]
                used_time = round(used_time,0)
                game_win = True
                print("You succeed! The old lady gave you a star, you wondered what's the use of it...")
                break
            else:
                if check_stalemate():
                    printboard()
                    time_list.append(time.time())
                    used_time = time_list[-1] - time_list[0]
                    used_time = round(used_time,0)
                    print('You were in the stalemate. You failed to help the old lady, she angrily left.')
                    game_win = False
                    break
                else:
                    continue
    return game_win,used_time


