# FILE NAME: cyber_suite_new_user.py

# NAME: Patrick Clark
# DATE: 2/23/2025 
# BRIEF DESCRIPTION: This program will ask the user for their name, id, and password. It will output a greeting with their name and id, 
# then show their password in hidden characters.  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience


# HINT: Tackle this one step at a time. First, just ask the name and the ID number
#       and then print those out. Once you get that working, add in the password.
#
#       Think about how to get the length of the password
#       Then, think about how to print out the Xs. Perhaps you can use string multiplication?



########## ENTER YER CODE BELOW THIS LINE ##########

your_name = input('Please enter your name: ')
user_id = int(input('Please enter your user id: '))
password = input('Please enter your password: \n')

characters = len(password)

print(f'Welcome, {your_name}. Your ID is {user_id}.')
print()
print(f'PASSWORD: ')
print("X" * characters)








########### END YER CODE ABOVE THIS LINE ###########
    


########################################
#          SAMPLE OUTPUT
########################################

'''
Please enter your name: Dave
Please enter your user id: 12345
Please enter your password: abc123

Welcome, Dave. Your ID is 12345.

PASSWORD: 
XXXXXX
'''

'''
Please enter your name: Katie
Please enter your user id: 13090
Please enter your password: PCT2024

Welcome, Katie. Your ID is 13090.

PASSWORD: 
XXXXXXX
'''

'''
Please enter your name: John
Please enter your user id: 10008
Please enter your password: TheOtherDayISawABearAGreatBigBear

Welcome, John. Your ID is 10008.

PASSWORD: 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''
1. This project has a bit of a speed bump (converting the password to XXXXs). What was your thought process?
# I knew I needed to find the number of characters that the password has since that is the only thing that can change the output. I found the len() function in 
# the jupyter notebook. This does exactly what I needed. I assigned a variable to the len() of the password so I could then use it to multiply "X" in the output.  





'''
