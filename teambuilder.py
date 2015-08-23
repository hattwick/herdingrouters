# create roster of team members

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

print('Done.')
