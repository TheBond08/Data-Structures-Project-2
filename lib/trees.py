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
        self.arithmos_mitroou = ""
        self.onoma = ""
        self.eponimo= ""
        self.b = 0.0
        self.ap = 0
        self.left = None
        self.right = None

def createNode():
    r = node()
    textLine = input("Give data:")
    dataRecord = textLine.strip().split()
    r.arithmos_mitroou = dataRecord[0]
    r.onoma = dataRecord[1]
    r.eponimo = dataRecord[2]
    r.b = float(dataRecord[3])
    r.ap = int(dataRecord[4])
    return r

def addInOrder(root, newNode):
    if newNode.arithmos_mitroou <= root.arithmos_mitroou:
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
        print(("%s %s %s %.2f %d") % (root.arithmos_mitroou, root.on, root.eponimo, root.b, root.ap))
        showInOrder(root.right)

def countNodes(root):
    result = 0
    if root != None:
        result = countNodes(root.left)
        result = result + 1
        result += countNodes(root.right)
    return result

def findByarithmos_mitroou(root, farithmos_mitroou):
    result = None

    if root != None:
        if farithmos_mitroou < root.arithmos_mitroou :
            result = findByarithmos_mitroou(root.left, farithmos_mitroou)
        elif farithmos_mitroou == root.arithmos_mitroou :
            result = root
        else:
            result = findByarithmos_mitroou(root.right, farithmos_mitroou)

    return result

def maxarithmos_mitroou(root) :
    if root.right == None:
        result = root
    else:
        result = maxarithmos_mitroou(root.right)
    return result

def maxGrade(root):
    result = -1

    if root != None:
        result = maxGrade(root.left)
        if result < root.b:
            result = root.b
        resultRight = maxGrade(root.right)
        if result < resultRight:
            result = resultRight
    return result

root = None

while True:
    print("""-------------------Menu-----------------------")
1. Add in order
2. Show in order
3. Find student by arithmos_mitroou
4. Show last student by arithmos_mitroou
5. Show maximum grade
0. Exit""")
    
    ch = input("Choice: ").strip()

    if ch == "0":
        break
    elif ch == "1":
        temp = createNode()
        if root == None:
            root = temp
        else:
            addInOrder(root, temp)
    elif ch == "2":
        showInOrder(root)
        print(("Number of node:%d") % (countNodes(root)))
    elif ch == "3":
        userarithmos_mitroou = input("Give arithmos_mitroou: ")
        temp = findByarithmos_mitroou(root, userarithmos_mitroou)
        if temp == None:
            print("Not found!")
        else:
            print(("%s %s %s %.2f %d") % (temp.arithmos_mitroou, temp.on, temp.eponimo,
                                          temp.b, temp.ap))
    elif ch == "4":
        if root == None:
            print("Empty tree!")
        else:
            temp = maxarithmos_mitroou(root)
            print(("%s %s %s %.2f %d") % (temp.arithmos_mitroou, temp.on, temp.eponimo,
                                          temp.b, temp.ap))
    elif ch == "5":
        if root == None:
            print("Empty tree!")
        else:
            print(("Max grade: %.2f") % (maxGrade(root)))
    else:
        print("Try again!")
