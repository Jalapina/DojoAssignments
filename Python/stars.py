def draw_stars(star):
    length=len(star)
    for num in range(0,length):
        import numbers
        if isinstance(star[num], numbers.Integral):
            print ('*')*star[num]
        else:
            word=star[num]
            long=len(star[num])
            print word[0]*long


draw_stars([4,'Tom',1,'Michael',5,7,'Jimmy Smith']); 