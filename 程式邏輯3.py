if __name__ =='__main__':
    n = input()
    num = []
    for i in range(int(n)):
        num.append(i+1)

    countto3 = 0
    countcurrentposition = 0
    while True:
        if num[countcurrentposition] != 0:
            countto3 += 1
        if countto3 == 3:
            num[countcurrentposition] = 0
            countto3 = 0

        countcurrentposition += 1
        if countcurrentposition == len(num):
            countcurrentposition = 0

        if num.count(0) == int(n)-1:
            break
    
    for i in num:
        if i != 0:
            print(i)       
