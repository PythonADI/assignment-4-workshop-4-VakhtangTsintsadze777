names = ["dato", "nika", "gio"] #1
print(names[0])
print(names[1])
print(names[2])


print(f"hi {names[0]}") #2
print(f"hi {names[1]}")
print(f"hi {names[2]}")

transportation = ["bicycle", "bmw", "plane"] #3

print("I would like to own a " + transportation[0])
print("I would like to own a " + transportation[1])
print("I would like to own a " + transportation[2])

invite_list = ["dato", "nika", "gio"] #4
print(invite_list)

for name in invite_list:
    print(f"I wanna invite {name}")

invite_list = invite_list[:-1] #5

print(invite_list)

for name in invite_list:
    print(f"I wanna invite {name}")

invite_list.extend(["luka", "erekle", "leqso"]) #6

print(invite_list)

for i in range(len(invite_list)):
    print(f"Welcome {invite_list[i]}")


# 7

while len(invite_list) > 2:
    removed_guest = invite_list.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")


# 8

places = ["Paris", "New york", "London", "Berlin", "Rome"]
print(places)

print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print(places)

places.reverse() #reverse
print(places)

places.reverse() # reverse twice - original
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)


# 9

print(f"I am inviting {len(invite_list)} people to dinner.")


# 11
print(places[10])