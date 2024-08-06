

# for the go_down,go_left,go_right,go_up function is to control the f"\033[1;33m{'P'}\033[0m" movment
# for checking_move is to check if the value in front of 
#only a with print 0 bug
# set the best record limit 
def best_record_projector():
    _2048=open('best_record_2048.txt').read()
    
    _2048=format_change_from_str_to_int(_2048)

    while min(_2048)<50:
        _2048.remove(min(_2048))

    sokoban=open('best_record_sokoban.txt').read()
    sokoban=format_change_from_str_to_int(sokoban)
    while min(sokoban)<20:
        sokoban.remove(min(sokoban))

    total=list(open('best_record_total.txt').read())
    total=format_change_from_str_to_int(total)

    while min(total)<100:
        total.remove(min(total))
    wordle=open('best_record_wordle.txt').read()
    wordle=format_change_from_str_to_int(wordle)
    print('The best of total  is :',min(total),'s')
    print('The best of sokoban is :',min(sokoban),'s')
    print('The best of 2048 is :',min(_2048),'s')
    print('The best of wordle is :',min(wordle),'s')
    input('Please press enter to start the game ')


def format_change_from_str_to_int(l):
    return_list=[]
    l=list(l)
    i=0
    button=False
    while 1:
        
        if len(l)==0:
            break
        
        elif l[i]=='\n':
            return_list.append(''.join(l[:i]))
            del l[:i+1]
            i=0
            button =True

        if ''in return_list:
            return_list.remove('')   
        if button == False:
            i+=1
        elif button == True:
            button=False
        
        
        
    for j in range (len(return_list)):
        return_list[j]=float(return_list[j])
        return_list[j]=int(return_list[j])
        
    
    return return_list
def creat_map_list():
    maze_only=0
    position=0
    sublist=[]
    x=open('maze.map')
    contents=x.read()
    contents=list(contents)
    while True:
        if position == len(contents):
            data.append(sublist)
            break
        if contents[position] == '\n':
            data.append(sublist)
            sublist=[]
            position+=1
            continue
        sublist.append(contents[position])
        position+=1
    for i in range (len(data)):
        for a in range(len(data[i])):
            k,l = data[i][a],["1","2","3","$","E","X","I","T","P"]
            if k in l[:3]:
                data[i][a] = f"\033[1;31m{data[i][a]}\033[0m"
            elif k in l[3:-1]:
                data[i][a] = f"\033[1;36m{data[i][a]}\033[0m"
            elif k in l[-1:]:
                data[i][a] = f"\033[1;33m{data[i][a]}\033[0m"
            elif k == "x":
                data[i][a] = f"\033[40;30m{data[i][a]}\033[0m"
        
def print1(k):
    separator = "\033[33m-\033[0m" * ((98 - len(k)) // 2)
    output = separator + k + separator
    if len(output) < 98:
        output += "\033[33m-\033[0m"
    print("\033[33m{}\033[0m".format(output))
    return
def print2():
    print("\033[33m'\033[0m"*84)
    return

def printer ():
    import os 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    import time 
    time.sleep(0.01)
    for i in range(len(data)):
        print("".join(data[i]))
        # for a in range(len(data[i])):
        #     if data[i][a] == f"\033[40m{data[i][a]}\033[0m": data[i][a] = "x"
def main ():
    import time
    import _2048
    import sokoban
    import wordle
    asking_if_player_want_to_view_the_best_record=input('Before you start,do you want to view the best record?(if yes type yes , if no type no)')
    if asking_if_player_want_to_view_the_best_record.upper() == 'YES':
        best_record_projector()
    background=open('background.txt')
    w,p = "\033[1;36;5mWelcome to our game!\033[0m","\033[1;36;5mPlease enjoy\033[0m"
    print2()
    print1(w)
    print2()
    print1(p)
    print2()
    print(background.read())
    # asking_if_player_want_to_check_the_best_record=input('Do you want to check the best best_record of this game?')
    input('Please press enter when you are ready :')
    creat_map_list()
    printer()
    killer=0
    start_time=time.time()
    while 1 :
        making_move= str(input('Your movment(support muti-input): '))
        making_move=list(making_move.upper())
        for i in range (len(making_move)):
            if making_move[i] != 'W' and making_move[i] != 'A' and making_move[i] != 'S' and making_move[i] !='D' and making_move[i] !='Q':
                continue #finish checking the input from the player 
        for i in range (len(making_move)):
            if making_move[i] =='W':
                x=go_up()
                if x== 0:
                    continue
                elif x== 1:
                    sokoban_result , sokoban_time =sokoban.main() # once approach check point 1,activite game sokoban
                    checking_map_after_playing_subgame(making_move[i])
                    
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)

                    # with open('best_record.txt') as f:
                    #     f.write(sokoban_time)

                elif x== 2:
                    _2048_result, _2048_time= _2048.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 3:
                    wordle_result, wordle_time = wordle.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x==4:
                    killer=True
                    break
                     

            
            elif making_move[i] =='A':
                x=go_left()
                if x == 0:
                    continue
                elif x== 1:
                    sokoban_result , sokoban_time =sokoban.main() # once approach check point 1,activite game sokoban
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 2:
                    _2048_result, _2048_time= _2048.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 3:
                    wordle_result, wordle_time = wordle.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x==4:
                    killer=True
                    break

            elif making_move[i] =='S':
                x=go_down()
                if x == 0:
                    continue
                elif x== 1:
                    sokoban_result , sokoban_time =sokoban.main() # once approach check point 1,activite game sokoban
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 2:
                    _2048_result, _2048_time= _2048.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 3:
                    wordle_result, wordle_time = wordle.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x==4:
                    killer=True
                    break

            elif making_move[i] =='D':
                x=go_right()
                if x == 0:
                    continue
                elif x== 1:
                    sokoban_result , sokoban_time =sokoban.main() # once approach check point 1,activite game sokoban
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 2:
                    _2048_result, _2048_time= _2048.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x== 3:
                    wordle_result, wordle_time = wordle.main()
                    checking_map_after_playing_subgame(making_move[i])
                    input('Please press enter to continue')
                    printer()
                    continue
                    #time.sleep(2)
                elif x==4:
                    killer=True
                    break


            elif making_move[i] =='Q':
                exit()
            printer()
            time.sleep(0.1)
        if killer == True:
            break
    end_time=time.time()
    total_time_of_maze=end_time-start_time
    total_time_of_maze =round(total_time_of_maze,0)
    game_result=[sokoban_result,_2048_result,wordle_result]
    subgame_used_time=[sokoban_time,_2048_time,wordle_time,total_time_of_maze]
    evaluation(game_result,subgame_used_time)
    ########################################
    # thats the end of the maze , _2048 , sokoban and wordle
    # need to dicuss about how to evaluate
        
def printstar(i):
    with open(f'star_{i}.txt', 'r') as file:
        text = file.read()
        YELLOW = '\033[1;41;33m'
        RESET = '\033[0m'
        print(YELLOW + text + RESET)        
def go_up():
    row, col =locate_player()
    is_check = checking_move(data[row-1][col])
    if is_check == 0:
        return 0
    elif is_check == 1 :
        data[row-1][col]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif is_check ==2:
        return 1 
    elif is_check ==3:
        return 2 
    elif is_check ==4:
        return 3 
    elif is_check ==5:
        return 4 
    
def go_down():
    row, col =locate_player()
    is_check = checking_move(data[row+1][col])
    if is_check == 0:
        return 0
    elif is_check ==1 :
        data[row+1][col] = f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif is_check ==2:
        return 1 
    elif is_check ==3:
        return 2 
    elif is_check ==4:
        return 3 
    elif is_check ==5:
        return 4 

def go_left():
    row, col =locate_player()
    is_check = checking_move(data[row][col-1])
    if is_check == 0:
        return 0
    elif is_check ==1:
        data[row][col-1]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif is_check ==2:
        return 1 
    elif is_check ==3:
        return 2 
    elif is_check ==4:
        return 3 
    elif is_check ==5:
        return 4 

def go_right():
    row, col =locate_player()
    is_check = checking_move(data[row][col+1])
    if is_check == 0:
        return 0
    elif is_check == 1:
        data[row][col+1]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif is_check ==2:
        return 1 
    elif is_check ==3:
        return 2 
    elif is_check ==4:
        return 3 
    elif is_check ==5:
        return 4 
    
    
def checking_move(value):
    if value == f"\033[40m{'x'}\033[0m":
        return 0
    elif value ==' ':
        return 1
    elif value == f"\033[1;31m{1}\033[0m":
        return 2
    elif value == f"\033[1;31m{2}\033[0m":
        return 3 
    elif value == f"\033[1;31m{3}\033[0m":
        return 4
    elif value == f"\033[1;36m{'$'}\033[0m":
        return 5
    
def checking_map_after_playing_subgame(movment):
    row,col=locate_player()
    if movment == 'W' and data[row-1][col]!='x':
        data[row-1][col]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif movment=='A'and data[row][col-1]!='x':
        data[row][col-1]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif movment=='S'and data[row+1][col]!='x':
        data[row+1][col]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '
    elif movment=='D'and data[row][col+1]!='x':
        data[row][col+1]=f"\033[1;33m{'P'}\033[0m"
        data[row][col]=' '

    

    
def locate_player():
    for i in range (len(data)):
        for j in range (len(data[i])):
            if f"\033[1;33m{'P'}\033[0m" in data[i]:
                row= i
            if f"\033[1;33m{'P'}\033[0m" == data[i][j]:
                col =j
    return row , col 

def evaluation(game_result,subgame_used_time):
    game_result_print_list=[]
    import time
    import os 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('measuring data.........\nPlease wait')
    time.sleep(3)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for i in range (len(game_result)):
        if game_result[i] == True:
            game_result_print_list.append('Pass')
        elif game_result[i]==False:
            game_result_print_list.append('Fail')
    

    print('subgame_one sokoban :',game_result_print_list[0],'Time used: ', subgame_used_time[0])
    print('subgame_two 2048 :',game_result_print_list[1],'Time used: ',subgame_used_time[1])
    print('subgame_three wordle :',game_result_print_list[2],'Time used: ',subgame_used_time[2])
    print('Total_time(add maze time ) is :',subgame_used_time[-1])
    if game_result[0]== True :
        with open('best_record_sokoban.txt','a') as _sokoban:
            _sokoban.write('\n'+str(subgame_used_time[0])+'\n')
    if game_result[1]== True :
        with open('best_record_2048.txt','a') as _2048:
            _2048.write('\n'+str(subgame_used_time[1])+'\n')
    if game_result[2]==True:
        with open('best_record_wordle.txt','a') as _wordle:
            _wordle.write('\n'+str(subgame_used_time[2])+'\n')
    with open('best_record_total.txt','a') as _total:
        _total.write('\n'+str(subgame_used_time[-1])+'\n')
    
    count_pass_game=0
    for i in range (len(game_result)):
        if game_result[i] == True:
            count_pass_game+=1
    if count_pass_game ==0:
        #################
        print("That's a scary adventure isn't it? Unfortunately, you failed all the hidden task!")
    elif count_pass_game ==1:
        printstar(1)#printing star # sting still want to add somthing 
        #################
        print('Good job! You survived and got a 24 karat golden star, sell it for cash??!!')
    elif count_pass_game ==2:
        printstar(2)
        ####################
        print('Well done! The two stars you got were made with 24karat gold, wonna be rich?')
    elif count_pass_game ==3:
        printstar(3)
        #################
        print('Marvelous! You are the true master of survival!')
        print('You were rewarded with three 24karat golden stars,I believe you will make good use of them!')
    # while 1 : 
    #     player_move=str(input('Your Move [wasdq]: '))
    #     player_move=player_move.upper()
    #     printer()       
data=[]
main()
