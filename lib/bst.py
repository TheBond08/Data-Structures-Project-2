def binary_search_tree():
    import csv
    from matplotlib import pyplot as plt
    import time

    file = open("MOCK_DATA.csv", newline='')
    reader = csv.reader(file)

    header = next(reader)

    # Πινακας αποθήκευσης δεδομένων csv
    dataRecord = []
    # Τροποποίηση δεδομένων απο str σε ο,τι επιθημούμε
    for row in reader:
        id = int(row[0])
        firstname = str(row[1])
        lastname = str(row[2])
        email = str(row[3])

        dataRecord.append([id, firstname, lastname, email])


    class node:
        def __init__(self):
            self.id = int
            self.firstname = ""
            self.lastname = ""
            self.email = " "
            self.left = None
            self.right = None




    def createNode():
        r = node()
        r.id = dataRecord[i][0]
        r.firstname = dataRecord[j][1]
        r.lastname = dataRecord[k][2]
        r.email = dataRecord[l][3]

        return r


    def addInOrder(root, newNode):
        if newNode.id <= root.id:
            if root.left == None:
                root.left = newNode
            else:
                addInOrder(root.left, newNode)

        else:
            if root.right == None:
                root.right = newNode
            else:
                addInOrder(root.right, newNode)


    def InOrder(root):
        if root != None:
            InOrder(root.left)
            print((root.id, root.firstname, root.lastname, root.email))
            InOrder(root.right)

    def PostOrder(root):
        if root != None:
            PostOrder(root.left)
            PostOrder(root.right)
            print((root.id, root.firstname, root.lastname, root.email))

    def PreOrder(root):
        if root != None:
            print((root.id, root.firstname, root.lastname, root.email))
            PreOrder(root.left)
            PreOrder(root.right)

    def countNodes(root):
        result = 0
        if root != None:
            result = countNodes(root.left)
            result = result + 1
            result += countNodes(root.right)
        return result


    def findByID(root, id):
        result = None

        if root != None:
            if id < root.id:
                result = findByID(root.left, id)
            elif id == root.id:
                result = root
            else:
                result = findByID(root.right, id)

        return result

    i = 0
    j = 0
    k = 0
    l = 0

    root = None
    count=0
    time_taken=0.0
    amount_of_data=[100]
    flag=True
    
    flag_mock_data = False

    while True:
        print("-------------------Menu-----------------------")
        if flag_mock_data == False:
            print("    1. Add mock data to the tree")
        else:
            print("""    2. Show in order
    3. Find student by ID""")
        
        print("0. Exit")

        ch = input("Choice: ").strip()

        if ch == "0":
            break
        elif ch == "1" and flag_mock_data == False:
            flag_mock_data = True
            start = time.time()
            while count<=99:

                temp = createNode()
                if root == None:

                    root = temp
                    i = 1
                    j = 1
                    k = 1
                    l = 1
                else:

                    addInOrder(root, temp)
                    i = i + 1
                    j = j + 1
                    k = k + 1
                    l = l + 1
                count= count + 1
            end= time.time()

            time_taken = end - start

            #Χρονος Εισαγωγης Στοιχειων (Διαγραμμα)
            plt.plot(amount_of_data, time_taken, color="blue", marker="o", linestyle="solid")
            plt.grid(axis='x')
            plt.grid(axis='y')
            plt.xticks(amount_of_data)
            plt.title(" Χρόνος - Πλήθος Δεδομένων")
            plt.ylabel("Χρόνος")
            plt.xlabel("Πλήθος Δεδομένων")
            plt.show()
            plt.close()

        elif ch == "2" and flag_mock_data == True:
            print("""Ways Of Order:
                1.Inorder
                2.Postorder
                3.Preorder""")

            choice = int(input("Select Way:"))

            while flag==True:
                if (choice>3 or choice<1):
                    print("Try Again!")
                    choice=int(input("Select Way:"))
                else:
                    flag=False

            if choice == 1:
                InOrder(root)

            elif choice == 2:
                PostOrder(root)

            elif choice==3:
                PreOrder(root)

            print(("Number of node:%d") % (countNodes(root)))

        elif ch == "3" and flag_mock_data == True:
            id = int(input("Give ID: "))
            start=time.time()
            temp = findByID(root, id)
            end=time.time()
            if temp == None:
                print("Not found!")
            else:
                print(("%d %s %s %s") % (temp.id, temp.firstname, temp.lastname,
                                        temp.email))

                plt.plot(amount_of_data, time_taken, color="blue", marker="o", linestyle="solid")
                plt.grid(axis='x')
                plt.grid(axis='y')
                plt.xticks(amount_of_data)
                plt.title(" Χρόνος Εύρεσης Στοιχείου")
                plt.ylabel("Χρόνος")
                plt.xlabel("Πλήθος Δεδομένων")
                plt.show()
                plt.close()

        else:
            print("Try again!")
