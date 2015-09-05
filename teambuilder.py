# create roster of team members

import random, sys, os, math


# Initiate empty list
teammate = []

# Loop to gather team members
while True:
    print('Type the name of a team member ' + str(len(teammate) + 1) + ' and press enter.  Enter nothing and press Enter to stop: ')
    name = input()
    if name == '':
       break
    teammate = teammate + [name]

# Print list when finished entering
print('The team is:')
for name in teammate:
    print('  ' + name)

# Iterate slightly differently
for i in range(len(teammate)):
   print ('Index ' + str(i) + ' in teammates list is: ' + teammate[i])

# Sort the iterate again
teammate.sort()
for i in range(len(teammate)):
   print ('Index ' + str(i) + ' in sorted teammates list is: ' + teammate[i])

# Reverse the sort
teammate.sort(reverse=True)
for i in range(len(teammate)):
   print ('Index ' + str(i) + ' in teammates Reverse Sort list is: ' + teammate[i])
   
# Find index position of team member
while True:
    print('If there is someone you want to search for, Type the name here.  Enter nothing to finish without searching.')
    firstname = input()
    if name == '':
	      sys.exit() 
    print (teammate.index(firstname))

print('Done.')

sys.exit()

# End of program