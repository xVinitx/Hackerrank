string = input('')
s_ar = string.split(' ')
final_ar = []
space = ' '
    
for w in s_ar:
    final_ar.append(w.capitalize())
print(space.join(final_ar))
