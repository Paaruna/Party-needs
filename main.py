students = input("How many students are coming to the party?\n")
students = int(students)
no_sausage = input("How many of the students don't eat sausages?\n")
no_sausage = int(no_sausage)
shots = input("How many of the students want shots instead of beer?\n")
shots = int(shots)
no_alcohol = input("How many of the students don't drink alcohol?\n")
no_alcohol = int(no_alcohol)

sausage = (students - no_sausage) * 3
corncobs = no_sausage * 3
beer = (students - no_alcohol - shots) * 4
shots = int(shots) * 4
cola = no_alcohol * 4

print("For the party, you will need" , sausage , "sausages,\n" , corncobs , "corncobs,\n" , shots, "shots,\n", beer ," beers and\n" , cola , "Cola-bottles.")
