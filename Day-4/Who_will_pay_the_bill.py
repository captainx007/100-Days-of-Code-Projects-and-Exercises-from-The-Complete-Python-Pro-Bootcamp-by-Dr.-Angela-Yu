friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#first method
import random

rand_num = random.randint(0,4)
if rand_num == 0:
    print("Alice")
elif rand_num == 1:
    print("Bob")
elif rand_num == 2:
    print("Charlie")
elif rand_num == 3:
    print("David")
else:
    print("Emanuel")

#2nd method
choose = random.choice(friends)
print(choose)

#3rd method

random_index = random.randint(0,4)
print(friends[random_index])
