import math

with open('users-data.txt', 'r') as u:
    lines = u.readlines()

with open('aed-data.txt', 'r') as a:
    aed = a.readlines()

users = []

for line in lines:
    line = line.strip()
    line = line.split(';')
    [userid, username, usercity, latitude, longitude] = line
    users.append((userid, username, usercity, (float(latitude), float(longitude))))

aeds = []

for defi in aed:
    defi = defi.strip()
    defi = defi.split(';')
    [aedid, aedname, aedlat, aedlong] = defi
    aeds.append((aedid, aedname, (float(aedlat), float(aedlong))))


def distance(a, b):
    sidea = (b[0] - a[0])
    sideb = (b[1] - a[1])
    distance = sidea**2 + sideb**2
    return math.sqrt(distance)


coord1 = input('Insert the latitude: ')
coord2 = input('Insert the longitude: ')
emergency_coord = (float(coord1), float(coord2))

nearest_user = min(users, key = lambda k: distance(emergency_coord, k[3]))
nearest_aed = min(aeds, key = lambda k: distance(emergency_coord, k[2]))

print('The closest First Responder is: ', nearest_user)
print('The closest AED is: ', nearest_aed)