# Ask user for their name
username = input("What is your name? ")
# Ask user for their favorite integer
fav_num = int(input("Favorite Number? "))
# Double, half, then square the number
double = fav_num *2
half = fav_num / 2
squared = fav_num *fav_num
# Greet the user
print("Hello {}, your favorite number is {}".format(username, fav_num))
print()
# Output the results of doubling, halving and squaring their favorite number
print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()