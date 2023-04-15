def exo1():
    # Task 1 - create a list with manually added items and print these elements. These elements be random names
    names = ["Anna","Tom", "Adam", "Chris"]
    my_string = 12 #C'est un INT
    my_int = "13" #C'est un STRING

    print("Voici mon texte "+str(my_string)+" \nOn fait du python et on a "+my_int+" ans! ")
    print(f"Voici mon texte {my_string} On fait du python et on a {my_int} ans! \n")
    #    print(names)
    #    print(type(names))
    #    print("")
def exo2():
    names = ["Anna","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris","Tom", "Adam", "Chris"]
    for i in range(0,len(names),1):
            #len(names)-1 donnera l'indice du DERNIER élément de la liste
            #i prendra les valeurs de 0 à len(names)-1 en faisant des sauts de 1
        my_string= f"i vaut {i} et le nom correspondant est {names[i]}"
        print(my_string)
def exo3():
    # Task 4 - a loop that only ends if we add an existing index in the list
    j = len(names)
    print("Give an index and i'll show you that item in the list.")
    while j > len(names)-1 or j < -len(names):
        j = int(input("Give me a valid index:\n"))
        if j < len(names) and j >= -len(names):
            print(names[j])
        else:
            print("There is no such item in the list.")

exo2()
my_list = [] #list vide
for i in range(0,30,1):
    #i prendre les valeurs de 0 à 30-1 en faisant des sauts de 1
    my_list.append(i) #ajouter un élément à la fin de la liste
for i in range(len(my_list)):
    print(f"l'index vaut {i} et la valeur correspondante vaut {my_list[i]}")

def function():


    # Task 6 - create a new list and fill it with the first 50 positive integers with a loop
    numbers = []
    i = 1
    while i <= 50:
        numbers.append(i)
        i += 1
    print(numbers)

    # Task 7 - create a new list, which contains the first 20 odd numbers
    odd_numbers = []
    even_numbers = []
    i = 0
    while i < 20:
        if i % 2 == 1:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
        i += 1
    print("Odd numbers: " + str(odd_numbers))
    print("Even numbers: " + str(even_numbers))
    print("")

    # Task 8 - Switch two list elements each other
    list_1 = [1,2,3,4,5]
    list_2 = [11,23,34,45,57]
    print("Before switch: %s" %list_1)
    print("Before switch: %s" %list_2)

    i = 0
    while i < 5:
        temp = list_1[i]
        list_1[i] = list_2[i]
        list_2[i] = temp

        i += 1

    print("After switch: %s" %list_1)
    print("After switch: %s" %list_2)
    print("")

    # Task 9 - insert items into a list
    insertList = []
    insertList.insert(1,0)
    insertList.insert(10,1)
    insertList.insert(5,2)
    print(insertList)

    # Task 10 - deleting items from a list
    girl_names = ["Anne", "Elizabeth", "Elon", "Sophie", "Hannah"]
    boy_names = ["Thomas", "George", "Rick", "Olivia", "Noah"]
    print(girl_names)
    print(boy_names)
    girl_names.pop(2)
    boy_names.remove("Olivia")
    print(girl_names)
    print(boy_names)

    # Task 11 - sum of items
    numberList = [1,40,523,6851,0,346,321,8,1,457,123]
    i = 0
    sum = 0
    while i < len(numberList):
        sum += numberList[i]
        i += 1
    print(sum)

    # Task 12 - occurencies in the list
    repeatList = [1, 0, 1, 2, 0, 2, 2, 1, 0, 1, 2, 1, 1, 1, 0]
    i = 0
    occunences = 0
    value = int(input("What value are we looking for?\n"))
    while i < len(repeatList):
        if repeatList[i] == value:
            occunences += 1
        i += 1
    print("The number " + str(value) + " appears " + str(occunences) + " times in the list.")
