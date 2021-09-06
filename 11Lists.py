if __name__ == '__main__':
    arr = []
    N = int(input())
    for n in range(N):
        command = input()
        command = command.split()
        command_name = command[0]

        if command_name == 'insert':
            position = int(command[1])
            number = int(command[2])
            arr.insert(position, number)
        elif command_name == 'print':
            print(arr)
        elif command_name == 'remove':
            command_num = int(command[1])
            arr.remove(command_num)
        elif command_name == 'append':
            command_num = int(command[1])
            arr.append(command_num)
        elif command_name == 'sort':
            arr.sort()
        elif command_name == 'pop':
            arr.pop()
        elif command_name == 'reverse':
            arr.reverse()