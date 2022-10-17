import math
import matplotlib.pyplot as plt 
import os

def clear():
  return os.system("cls")

with open('users-data.txt', 'r') as u:
    lines = u.readlines()

with open('aed-data.txt', 'r') as a:
    aed = a.readlines()

# Store Users' data
users = []

for line in lines:
    line = line.strip()
    line = line.split(';')
    [userid, username, usercity, latitude, longitude] = line
    users.append((userid, username, usercity, (float(latitude), float(longitude))))

# Stores AEDs' data
aeds = []

for defi in aed:
    defi = defi.strip()
    defi = defi.split(';')
    [aedid, aedname, aedlat, aedlong] = defi
    aeds.append((aedid, aedname, (float(aedlat), float(aedlong))))

# Calculate distance between two points
def distance(a, b):
    sidea = (b[0] - a[0])
    sideb = (b[1] - a[1])
    distance = sidea**2 + sideb**2
    return math.sqrt(distance)

# Draw plot with locations on the Map
def draw_plot(x, y, title, label):
    plt.plot(x, y, 'r*')
    plt.axis([0, 100, 0, 100])

    for i,j,n in zip(x,y,label):
        plt.text(i,j,n.format(i,j))

    plt.title(title)
    plt.show()

# Display Users on Map
users_x = []
users_y = []
users_names = []

for user in users:
    users_x.append(user[3][0])
    users_y.append(user[3][1])
    users_names.append(user[1])

#draw_plot(users_x,users_y,'Users on Map', users_names)

# Display AEDs on Map
aed_x = []
aed_y = []
aed_names = []

for defi in aeds:
    aed_x.append(defi[2][0])
    aed_y.append(defi[2][1])
    aed_names.append(defi[1])

#draw_plot(aed_x, aed_y, 'AEDS on Map', aed_names)

test = True

valid = []
for n in range(0, 101):
    valid.append(n)

while test:
    print(input('This is a very simple prototype of the Emergency System '))
    print(input('You will simulate the job of the ECC operator.. '))
    print(input('You receive an emergency call and you fill the form with the details of the emergency '))
    coord1 = input('Please, insert the latitude value (from 0 to 100): ')
    while int(coord1) not in valid:
        coord1 = input('Please enter a valid number (from 0 to 100):' )
    coord2 = input('Please insert the longitude value (from 0 to 100): ')
    while int(coord2) not in valid:
        coord2 = input('Please enter a valid number (from 0 to 100):' )

    emergency_coord = (float(coord1), float(coord2))

    nearest_user = min(users, key = lambda k: distance(emergency_coord, k[3]))
    nearest_aed = min(aeds, key = lambda k: distance(emergency_coord, k[2]))

    print('The closest First Responder is: ', nearest_user)
    print('The closest AED is: ', nearest_aed)

    yn = input('Do you want to add another emergency? (y/n): ')
    if yn == 'n':
        test = False

    clear()