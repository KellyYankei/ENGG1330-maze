def welcome():
    wall=open('picture1.txt').read()
    print(wall)
    import time
    time.sleep(2)
    print("In front of you is a brick wall with a interesting board on it")
    print("Your goal is to add up all the '2's spawned on the board")
    print("Once you combine up to the number 256 on the board, you win")
    input('Please press enter before you start!')
def main ():
    # used_time=0
    # return True , used_time
    import time
    global a 
    global time_list
    a=False
    time_list=[]
    time_list.append(time.time())
    welcome()
    
    #print(time_list)
    
    creat_list()
    printer()
    while 1 :
        
        player_input = str(input("Your move is(wasd): "))
        if player_input.isalpha() == False :
            continue
        if len(player_input) !=1:
            continue
        player_input= player_input.upper()

        if player_input =='W':
            go_up()
        elif player_input =='A':
            go_left()
        elif player_input =='S':
            go_down()
        elif player_input =='D':
            go_right()
        elif player_input =='Q':
            time_list.append(time.time())
            used_time= time_list[-1] - time_list[0]
            used_time=round(used_time,0)
            #print('the time that you finish is :',used_time,'s')
            print('That`s it, BYE BYE!')
            return False ,used_time

###################################################
        
        #print(checker(),can_play_or_not())
        if checker_of_finding_highest_score() == True:
            printer()
            print('congratulations, you solved it successfully!')
            print("One of the brick started glowing, you figure out it's a brick shaped box with a piece of star inside.")
            print('Like a door, the wall opens up, leaving a clear pathway, you decided to keep going forward.')
            time_list.append(time.time())
            used_time= time_list[-1] - time_list[0]
            used_time=round(used_time,0)
            #print('the time that you finish is :',used_time,'s')
            return True, used_time 
                ################################
               
        elif checker() == True and can_play_or_not() == True:
            time_list.append(time.time())
            used_time= time_list[-1] - time_list[0]
            used_time=round(used_time,0)
            #print('the time that you finish is :',used_time,'s')
#######################################
            print('You would never know what you could unlock')
            print('As you have no way out, you brutally smashed the wall until you could go forward.')
            return False, used_time 

            ###############################################################
            break
        
        elif checker()== True and can_play_or_not() == False:
            print('wait and think~~\nIs not the end')


            continue
        
        adding_item()
        printer()
    


        

def printer():
    import os 
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
    import time
    time.sleep(0.01)
    for i in range (len(data)):
        for line in [data[i]]:
            print('{:>8} {:>8} {:>8} {:>8}'.format(*line))
            print('\n')


def creat_list ():
    global data
    data=[]
    sublist=[]
    x=4
    for j in range (x):
        for i in range (x):
            sublist.append('.')
        data.append(sublist)
        sublist=[]


def go_left():
    

    for i in range(len(data)):
        for j in range (len(data[i])-1):
            if data[i][j] == data[i][j+1] != '.':
                data[i][j] = data[i][j] + data [i][j+1] 
                data[i][j+1] = '.'
            if data[i][j]=='.' and data[i][j+1] !='.':
                data[i][j]=data [i][j+1]
                data[i][j+1]='.'
                go_left() 
            
                
    

def go_right():

    for i in range((len(data))):
        
        for j in range (-1,-(len(data[i])),-1):
            
            if data[i][j] == data[i][j-1] != '.':
                data[i][j] = data[i][j] + data [i][j-1] 
                data[i][j-1] = '.'
            if data[i][j]=='.' and data[i][j-1] !='.':
                data[i][j]=data [i][j-1]
                data[i][j-1]='.'
                go_right()
            
            
def go_up():
    for j in range((len(data))):
        
        for i in range (len(data[j])-1):
            
            if data[i][j] == data[i+1][j] != '.':
                data[i][j] = data[i][j] + data [i+1][j] 
                data[i+1][j] = '.'
            if data[i][j]=='.' and data[i+1][j] !='.':
                data[i][j]=data [i+1][j]
                data[i+1][j]='.'
                go_up()
    
def go_down():
    for j in range((len(data))):
        
        for i in range (-1,-(len(data[j])),-1):
            
            if data[i][j] == data[i-1][j] != '.':
                data[i][j] = data[i][j] + data [i-1][j] 
                data[i-1][j] = '.'
            if data[i][j]=='.' and data[i-1][j] !='.':
                data[i][j]=data [i-1][j]
                data[i-1][j]='.'
                go_down()

def checker():
    x=0
    for i in range(len(data)):
        for j in range (len(data[i])):
            if data[i][j] !='.':
                x+=1
    if x == len(data)*len(data):
        return True
    else:
        return False
def can_play_or_not():
    x=0
    y=0
    for i in range (len(data)):
        for j in range (len(data[i])-1):
            if data[i][j] != data[i][j+1] and data[i][j] !='.' and data [i][j+1] != '.':
                x+=1
    if x == 12:
        x=True
    for j in range (len(data)):
        for i in range (len(data[i])-1):
            if data[i][j] != data[i+1][j] and data[i][j] !='.' and data [i+1][j] != '.':
                y+=1
    if y == 12 :
        y = True
    if x == y == True :
        return True 
    else:
        return False


def checker_of_finding_highest_score():
    #print(a)
    if a == False:
        list1=[0]
        x=0
        for i in range (len(data)):
            for j in range (len(data[i])):
                if str(data[i][j]).isdigit() == True:
                    list1.append(data[i][j])
            if x< max(list1):
                x=max(list1)
            list1=[0]
        # if x== 256:
        #     time_list.append(time.time())
        if x== 256 :
            time_list.append(time.time())
            return True

    
def adding_item():
    while 1:
        col , row =location()
        if data[row][col] == '.':
            data [row][col] = 2
            break
        
    

def location():
    import random
    y= round(random.randint(0,3),0)
    x= round(random.randint(0,3),0)
    return x , y 

import time
######time not fix and also not having fulling size test

