Consider a list (list = []). You can perform the following commands:
insert, print, remove, append, sort, pop, reverse

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CODE:
if __name__ == '__main__':
    n = int(input())
    arr1 = []
    commands = []
    for i in range(n):
        commands.extend(input().split())
    # print(commands)
    for i in range(len(commands)):
        if commands[i] == 'insert':
            j = int(commands[i + 1])
            k = int(commands[i + 2])
            arr1.insert(j,k)
            i += 3   
        elif commands[i] == 'print':
            print(arr1)
        elif commands[i] == 'remove':
            m = int(commands[i+1])
            for item in arr1:
                if item == m: 
                    arr1.remove(m)
                    break
            i += 2
        elif commands[i] == 'append':
            o = int(commands[i+1])
            arr1.append(o)
            i += 2
        elif commands[i] == 'sort':
            arr1.sort()
        elif commands[i] == 'pop':
            arr1.pop()
        elif commands[i] == 'reverse':
            arr1.reverse()
            
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
