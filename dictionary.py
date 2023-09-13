usr/bin/python3
user={'don':'active','van':'actuve','hans':'active','vimal':'inactive','cool_lip':'active','trust':
  
for key, value in user.copy().items():
      if value == 'inactive':
          del user[key]
print("Active users are : "+ format(user))    
#deleting user in dictionary
