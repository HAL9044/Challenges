def queue(queuers, pos):
    bool = False
    ind = 0
    while bool == False:
        for i in range(len(queuers)):
            if queuers[i] != 0:
                ind += 1
                queuers[i] = queuers[i] - 1
                if queuers[pos] == 0:
                    bool = True
                    break
                print(queuers)
            elif queuers[i] == 0:
                None
    print(ind)
queue([2, 5, 3, 6, 4],1)
