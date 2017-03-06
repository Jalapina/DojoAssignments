def odd_even():
    for loops in range(1001):
        if loops%2==1:
            print 'Number is:',loops, 'This is an odd number'
        else:
            print 'Number is:',loops,'This is an even number'


def mult(list):
    length=len(list)
    final_list=[]
    for arr in range (0,length):
        lists=list[arr]
        final_list.append(lists*5)

    print final_list

mult([2,3,4,5])