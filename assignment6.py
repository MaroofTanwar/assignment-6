def ds(roll_no,name):
     list=[roll_no,name]
     tuple=(roll_no,name)
     set={roll_no,name}
     dict={"roll_no":roll_no,"name":name}
     print("data structures:")
     print("List:",list)
     print("Tuple:",tuple)
     print("Set:",set)
     print("Dictionary:",dict)
     newroll_no = input("Enter Roll number: ")
     newName = input("Enter Name: ")
     list[0] = newroll_no
     list[1] = newName
     tuple = (newroll_no, newName)
     set.remove(roll_no)
     set.add(newroll_no)
     set.remove(name)
     set.add(newName)
     dict['roll_no'] = newroll_no
     dict['Name'] = newName
     print("updated:")
     print("List:",list)
     print("Tuple:",tuple)
     print("Set:",set)
     print("Dictionary:",dict)
     del list
     del tuple
     del set
     del dict
ds("61", "Maroof")