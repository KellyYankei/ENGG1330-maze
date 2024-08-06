# with open('star_1.txt', 'r') as file:
#     text = file.read()
#     YELLOW = '\033[1;41;33m'
#     RESET = '\033[0m'
#     print(YELLOW + text + RESET)
import maze
for i in range (1,4):
    maze.printstar(i)
