if __name__ =='__main__':
    initial_score = [int(x) for x in input().split()]
    print(initial_score)
    reverse_score = []
    for i in initial_score:
        reversed_string = "".join(reversed(str(i)))
        reverse_score.append(int(reversed_string))
    print(reverse_score)