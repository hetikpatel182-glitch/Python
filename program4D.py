name = input("Enter Your Name : ")
age = int(input("Enter Age : "))
weight = int(input("Enter Weight (in kg) : "))

print("Person Name :", name)
print("Age :", age)
print("Weight :", weight)

if age >= 18:
    if weight >= 50:
        print("Status : Eligible to donate blood")
    else:
        print("Status : Not eligible to donate blood (underweight)")
else:
    print("Status : Not eligible to donate blood (underage)")
