import random 

for students in range(0,10):
    score = random.randint(60,100)

    if score < 70:
        print "Score:",score,'; your grade is D'
    elif score < 80:
        print "Score:",score,'; your grade is C'
    elif score < 90:
        print "Score:",score,'; your grade is B'
    else:
        print "Score:",score,'; your grade is A'
