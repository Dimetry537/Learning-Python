from colorama import init, Fore
# colorama needs to be initialized in order to be used
init()
def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')