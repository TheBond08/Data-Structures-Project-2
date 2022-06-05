import csv




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
        self.lastname= ""
        self.email = " "
        self.left = None
        self.right = None


i = 0
j = 0
k = 0
l = 0


def createNode():
    r = node()
    r.id = (dataRecord[i][0])
    r.firstname = dataRecord[j][1]
    r.lastname= dataRecord[k][2]
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

def showInOrder(root):
    if root != None:
        showInOrder(root.left)
        print((root.id, root.firstname, root.lastname, root.email))
        showInOrder(root.right)

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
        if id < root.id :
            result = findByID(root.left, id)
        elif id == root.id :
            result = root
        else:
            result = findByID(root.right, id)

    return result


root = None



while True:
    print("""-------------------Menu-----------------------")
1. Add in order
2. Show in order
3. Find student by ID
0. Exit""")
    
    ch = input("Choice: ").strip()

    if ch == "0":
        break
    elif ch == "1":
        temp = createNode()
        if root == None:

            root = temp
        else:
            i = i + 1
            j = j + 1
            k = k + 1
            l = l + 1
            addInOrder(root, temp)



    elif ch == "2":
        showInOrder(root)
        print(("Number of node:%d") % (countNodes(root)))

    elif ch == "3":
        id= int(input("Give ID: "))
        temp = findByID(root, id)
        if temp == None:
            print("Not found!")
        else:
            print(("%d %s %s %s") % (temp.id, temp.firstname, temp.lastname,
                                          temp.email))

    else:
        print("Try again!")
