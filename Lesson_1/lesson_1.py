print("Hello world!")
user_name = "Yaroslav"
print (user_name)

user_age = 5
print(user_age)

# user_age = user_age + 1
# print (user_age)

if user_age >= 18:
    print ("age is more then 18")
if user_age < 18:
    print ("age is less")


for f in user_name:
    print(f)
a = 3
b = 4
summ = a + b
dil = a / b
mn = a * b
vid = a - b
print(mn, dil, vid, summ, sep=",\n")