students = input("How many students are coming to the party?\n")
students = int(students)
no_sausage = input("How many of the students don't eat sausages?\n")
no_sausage = int(no_sausage)
no_beer = input("How many of the students don't drink beer?\n")
no_beer = int(no_beer)

sausage = (students - no_sausage) * 3
corncobs = no_sausage * 3
beer = (students - no_beer) * 4
cola = no_beer * 4

print("For the party, you will need" , sausage , "sausages,\n" , corncobs , "corncobs,\n" , beer ," beers and\n" , cola , "Cola-bottles.")
