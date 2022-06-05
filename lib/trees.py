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
        self.am = ""
        self.on = ""
        self.ep = ""
        self.b = 0.0
        self.ap = 0
        self.left = None
        self.right = None

def createNode():
    r = node()
    textLine = input("Give data:")
    dataRecord = textLine.strip().split()
    r.am = dataRecord[0]
    r.on = dataRecord[1]
    r.ep = dataRecord[2]
    r.b = float(dataRecord[3])
    r.ap = int(dataRecord[4])
    return r

def addInOrder(root, newNode):
    if newNode.am <= root.am:
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
        print(("%s %s %s %.2f %d") % (root.am, root.on, root.ep, root.b, root.ap))
        showInOrder(root.right)

def countNodes(root):
    result = 0
    if root != None:
        result = countNodes(root.left)
        result = result + 1
        result += countNodes(root.right)
    return result

def findByAM(root, fAM):
    result = None

    if root != None:
        if fAM < root.am :
            result = findByAM(root.left, fAM)
        elif fAM == root.am :
            result = root
        else:
            result = findByAM(root.right, fAM)

    return result


root = None

print("-------------------Menu-----------------------")
print("1. Add in order")
print("2. Show in order")
print("3. Find student by AM")
print("0. Exit")
ch = input("Choice: ").strip()

while ch != "0":
    if ch == "1":
        temp = createNode()
        if root == None:
            root = temp
        else:
            addInOrder(root, temp)
    elif ch == "2":
        showInOrder(root)
        print(("Number of node:%d") % (countNodes(root)))
    elif ch == "3":
        userAM = input("Give AM: ")
        temp = findByAM(root, userAM)
        if temp == None:
            print("Not found!")
        else:
            print(("%s %s %s %.2f %d") % (temp.am, temp.on, temp.ep,
                                          temp.b, temp.ap))

    else:
        print("Try again!")
    print("-------------------Menu-----------------------")
    print("1. Add in order")
    print("2. Show in order")
    print("3. Find student by AM")
    print("4. Show last student by AM")
    print("5. Show maximum grade")
    print("0. Exit")
    ch = input("Choice: ").strip()
