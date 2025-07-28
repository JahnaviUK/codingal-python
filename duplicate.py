student_data = {'id1':
 {
     'name':'jahnavi',
     'class' : "VII",
     'age' : 12
 },
 'id2':
 {
     'name':'momo',
     'class' : "VIII",
     'age' : 13
 },
 'id3':
 {
     'name':'jahnavi',
     'class' : "VII",
     'age' : 12
 },
 'id4' :
 {
     'name':'shreshta',
     'class' : "VI",
     'age' : 11
 },

                 }
result = {}
for key ,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)