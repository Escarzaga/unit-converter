print (" ---------- Welcome to the Unit Converter Robot ---------- ")
print ("             // Convert Kilometers to Miles //        ")
print (" ++ Please provide values below to convert kilometer [Km] to mile [mi] ++")

miles = .62
kilometers = None

while True:

     kilometers = int(input("Enter kilometers: "))
     print(kilometers * miles, "miles")

     nextconv = input("Would you like to do another conversion [yes/no]?: ")
     if nextconv == "yes":
        print(" ")
     elif nextconv == "no":
        print("Thank you for using the Unit Converter, Goodbye!")
        break
     else:
         print("Please enter yes or no")
         nextconv = input("Would you like to do another conversion [yes/no]?: ")
         if nextconv == "no":
             print("Thank you for using the Unit Converter, Goodbye!")
             break










