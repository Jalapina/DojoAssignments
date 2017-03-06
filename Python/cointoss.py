def coin():
    import random
    count = 0
    tails=0
    heads=0
    for coins in range(5000):

        head_tails = random.randint(0,1)
        
        if head_tails==True:
            count+=1;
            heads+=1
            print "Attempt #",count,"Throwing a coin .... IT'S HEADS! You have", heads,'heads so far and',tails,'tails'
        
        else:
            count+=1;
            tails+=1;
            print "Attempt #",count,"Throwing a coin .... IT'S TAILS! you have",tails,'tails so far and',heads,'heads'

        
coin();

