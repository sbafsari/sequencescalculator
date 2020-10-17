torf = True
while torf:
        print("Welcome the calculator! ")
        print("Firstly type your the first two values")
        value1 = float(input("Value 1 is: "))
        value2 = float(input("Value 2 is: "))
        wanted = float(input("Which term of sequence is asked? "))
        print("Please type 1 for calcutions of arithmetic sequence or type 2 for calculations of geometric sequence.")
        selection1 = int(input("Your choice:"))
        if selection1 == 1:
                d = value2 - value1
                termar = value1 + (wanted-1)*d
                sumar = (wanted/2)*((2*value1)+((wanted - 1)*d))
                chose = int(input("For finding term type 3 or for finding sum type 4"))
                if chose == 3:
                        print(termar)
                elif chose == 4:
                        print(sumar)
                else:
                        print("You type wrong number. System is going to locked!")
                        torf = False
        elif selection1 == 2:
                r = value2/value1
                termge = value1 * (r**(wanted-1))
                sumge1 = (value1*(1-(r**(wanted-1))))/(1-r)
                sumge2 = (value1*((r**(wanted-1))-1))/(r-1)
                suminfinite = value1/(1-r)
                chose2 = int(input("For finding term type 5,for finding sum type 6 ,or finding sum of infinite sequence type 7"))
                if chose2 == 5:
                        print(termge)
                elif chose2 == 6:
                        if abs(r)<1:
                                print(sumge1)
                        elif abs(r)>1:
                                print(sumge2)
                        else:
                                print("There is not sum!")
                elif chose2 == 7:
                        if abs(r)<1:
                                print(suminfinite)
                        else:
                                print("There is not sum!")
                else:
                        print("You type wrong number! System is closing...")
                        torf = False
        else:
                print("You did not type correct number! System is stoping,sorry!")
                torf = False 

                        
        


               
