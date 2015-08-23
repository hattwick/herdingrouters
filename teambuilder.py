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
