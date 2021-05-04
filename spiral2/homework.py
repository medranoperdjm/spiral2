def spiralize(size, n=1):
    """ Your code goes somewhere in here"""
    size = []
    x= sum(size)
    counter = 0
    incrt = 2
    total = 0
    
    while x <= n **2:
        total += x
        x += incrt
        counter += 1
        if counter ==4:
            incrt +=2
            counter = 0
    return_value = n
    return return_value
 