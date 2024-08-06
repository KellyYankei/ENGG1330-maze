# import sokoban
# import wordle 
# maze = open('maze.map')
# m = maze.read()
# m1 = m.splitlines()
# list1 = []

# maze_map= open('maze.map')
# maze_map=maze_map.read()
# print(list(maze_map))
#开始 选择玩/查最高分和历史游戏记录
import _2048
import maze
import sokoban
import wordle
def main ():
    welcome_txt= open('background.txt')
    welcome_txt=welcome_txt.read()
    print(welcome_txt)
    x=_2048.main()

    
def creating_map():
    global map_list
    position=0
    map_=open('maze.map')
    map_=map_.read()
    map_=list(map_)

    sublist=[]
    map_list=[]
    for i in range(len(map_)):
        if map_[position] !='\n':
            sublist.append(map_[position])
        elif map_[position] == '\n':
            map_list.append(sublist)
            sublist=[]
        position+=1


def printer():
    for i in range (len(map_list)):
        print(''.join(map_list[i]))
main()
creating_map()
printer()













