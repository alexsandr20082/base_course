names = ["John","Dima","Maria","Richrd"]
ages = [16,43,56,12]

def checker(user):
    name, age = user
    return age > 20
 
 
users = list(zip(names, ages))
canDrinkAlcohol = list(filter(checker, users))
print(canDrinkAlcohol)