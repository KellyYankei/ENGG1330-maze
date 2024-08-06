def welcome():
    import time
    print('Suddenly, your eye spotted something \033[33;1mshiny\033[0m, you walk toward it,')
    print("It's a chest with alphabet lock! ")
    time.sleep(3)

def print_win1(k):  #different output forms use different function, but some intentions. 
    separator = "\033[33m-\033[0m" * ((74 - len(k)) // 2)
    output = separator + k + separator
    if len(output) < 74:
        output += "\033[33m-\033[0m"
    print("\033[33m{}\033[0m".format(output))
    return

def print_win2():
    print("\033[33m'\033[0m"*60)
    return

def check_in_dict(word): #check if player's input word is in the dictionary
    word_list = open('wordle_dict.map')
    words = word_list.read()
    dictionary = words.splitlines()
    if word in dictionary:
        return True
    else:
        return False

def print_current_answer(current_dict): #displace the correct one with the true word, else show in '*' form
    show = ['*','*','*','*','*']
    for key,value in current_dict.items():
        show[key]= value
    print("".join(show))
    return 0

def print_current_list(current_list):    #print the letters that player have guess. Output the list since they are stored there
    print("Current known letter:",end="")
    print(",".join(set(current_list)))
    return 0

def check_input1(player_input): #check if the input is a five-letter English word
    k = ""
    for i in player_input:
        k += i
    if len(player_input) == 5 and (all(i.isalpha() for i in player_input)) and check_in_dict(k) :
        return True
    else: 
        if not all(i.isalpha() for i in player_input):
            print("You input something that is not alphabet.")
        elif len(player_input) != 5:
            print("lenerror: the len of your input should be 5")
        else:
            print("Your input is not a word.")
        return False

def check_input2(answer,player_input,correct_dict,correct_list,try_time): #check the similarity of the answer and the player input, then return feedback
    import time,os
    global used_time
    for i in range(5):
        if all(answer[i]==player_input[i] for i in range(5)):
            if os.name == 'nt':          #use for clear the workplace
                os.system('cls') 
            else:
                os.system('clear') 
            c,w = "\033[1;31;5mCongratulations!\033[0m","\033[1;31;5mYou win!\033[0m"  #print win information
            time_list.append(time.time())   # stop timing 
            used_time = time_list[-1] - time_list[0]  #calculated used time
            used_time = round(used_time,0)  #get a int
            print_win2()  #print win
            print_win1(c)
            print_win2()
            print_win1(w)
            print_win2()
            return correct_list, correct_dict,True
        elif try_time == 1:    #last time
            if os.name == 'nt':
                os.system('cls') 
            else:
                os.system('clear') 
            print("Sorry, your last chance still missed.")
            return correct_list, correct_dict , False
        elif any(player_input[i] in answer for i in range(5)):
            if os.name == 'nt':
                os.system('cls') 
            else:
                os.system('clear') 
            print("Almost!\nThe answer is: ",end="")
            wrong_position_word = []
            for i in range(len(player_input)):
                if player_input[i] in answer:
                    correct_list.append(player_input[i])
                if player_input[i] == answer[i]:
                    correct_dict[i] = answer[i]
                if player_input[i] != answer[i] and player_input[i] in answer:
                    wrong_position_word.append(player_input[i])
            print_current_answer(correct_dict)
            if len(wrong_position_word) > 1:
                print("The following letters are in the word but at the wrong position: ",end="")
                print(",".join(wrong_position_word))
            elif len(wrong_position_word) == 1:
                print("The following letter is in the word but at the wrong position: ",end="")
                print(wrong_position_word[0])
            print_current_list(correct_list)
            return correct_list, correct_dict , False
        else:
            if os.name == 'nt':
                os.system('cls') 
            else:
                os.system('clear') 
            print("Sorry, all the letters in your input word is not in the correct word.")
            print("The answer is: ",end="")
            print_current_answer(correct_dict)
            print_current_list(correct_list)
            return correct_list, correct_dict, False

def wordle_play(answer):
    import time
    global used_time,game_win
    play, try_time, correct_dict, correct_list = True, 6, {}, []
    print("The code is a \033[1m5-letter English word\033[0m. You get \033[1m6 chances\033[0m to guess.") #statement
    print("Ready?")
    time.sleep(2)
    print("Go!")
    input('Please press \033[1menter\033[0m to start the game')
    while play:
        player_input=input('Please input a five-letter English word: ')
        player_input = player_input.lower()
        player_input=list(player_input) 
        if not check_input1(player_input):
            continue
        correct_list, correct_dict, result = check_input2(answer,player_input,correct_dict,correct_list,try_time)
        if not result:
            try_time -= 1
            if try_time > 1:
                print("You have",try_time,"chances left.")
                continue
            elif try_time == 1:
                print("The last chance! Come on.")
                continue
            else:
                print("Your chances have gone.")
                a = "".join(answer)
                time_list.append(time.time())
                used_time = time_list[-1] - time_list[0]
                used_time = round(used_time,0)
                game_win = False
                print(f"The answer is {a}.")
                break
        else:
            break

def main():
    welcome()
    global time_list,game_win,used_time
    import time,random
    time_list,used_time = [],0
    time_list.append(time.time())
    game_win = True
    used_time = 0
    word_list = open('wordle_gameword.map')
    words = word_list.read()
    dictionary = words.splitlines()
    answer = dictionary[random.randint(1,len(dictionary))]
    answer = list(answer)
    wordle_play(answer)
    return game_win,used_time
