#Script checks password complexity

import re
with open("passwords.txt") as passs:
   
   my_list = passs.read().split(',')
   correct = []

   for i in my_list:
      word = i

      #checking length of password
      if len(word) >= 4 or len(word) <= 20:
         continue

      #checking for blacklisted words
      if re.search(r'admin|root|password', word, re.IGNORECASE):
         continue

      #will remove capital letters, lowercase letters, numbers, and allowed special letters if there is atleast 1 capital letter
      if re.search(r'[A-Z]', word):
         word = re.sub(r'[A-Za-z0-9!@:&]', '', word)
      else:
         continue 
      
      #if any character is left in the word string then it violates the stated requirements
      if (word == ""):
         correct.append(i)

   print(len(my_list) - len(correct))
