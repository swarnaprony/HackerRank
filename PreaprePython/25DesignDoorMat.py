if __name__ == '__main__':
    number = list(set(map(int,input().split())))
    number.sort()
    n= int(number[0])

    for i in range(1,n+1):
        if i == int(n/2) +1:
            print((7+3*(int(n-i-3)))*'-'+'WELCOME'+(7+3*(int(n-i-3)))*'-')
        elif i< int(n/2) +1:
            print(3*(int(n/2)-i+1)*'-'+(2*i-1)*'.|.'+3*(int(n/2)-i+1)*'-')
        else:
            print(((3*(i-(int(n/2)+1))*'-')+(n-2*(i-(int(n/2)+1)))*'.|.')+ (3*(i-(int(n/2)+1))*'-'))