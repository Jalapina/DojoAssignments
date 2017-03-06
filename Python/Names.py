
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for value in students:
     
    

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
    counter = 0
    for value in data: 
        counter+=1
        # print counter
        word_length= len(value['first_name'])+len(value['last_name'])

        print counter,value['first_name'],value['last_name'],'-',word_length

        

# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }

# for key, data in context.items():
#      #print data
#      for value in data:
#           print "Question #", value["id"], ": ", value["content"]
#           print "----"



