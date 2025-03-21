print("WHat do you want to calculate?")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. annuity")

choice = input("Enter choice 1, 2, or 3: ")

if choice == '1':
    
    print("Calculate Simple Interest")
    
    P = float(input("Enter the principal:"))
    R = float(input("Enter the rate:"))
    T = float(input("Enter the time:"))

    SI = (P * R * T) / 100

    print("Simple Interest is:", SI)
    
elif choice == '2':
    
    print("Calculate Compound Interest")
    
    P = float(input("Enter the principal:"))
    R = float(input("Enter the rate:"))
    N = float(input("Enter the number of times that interest is compounded per year:"))
    T = float(input("Enter the time:"))
    
    A = P * (pow((1 + R / 100), N * T))
    
    CI = A - P
    
    print("Compound Interest is:", CI)
    
elif choice == '3':
   PMT = float(input("Enter the periodic payment:"))
   R = float(input("Enter annual interest rate (%): "))
   n = int(input("Enter number of periods per year: "))
   T = int(input("Enter total number of years: "))
   
   # Calculate total number of payments
   nt = n * T

   # Calculate future value of annuity using modified formula
   A = PMT * ((1 + R / 100) ** nt - 1) / (R / 100)
   
   print("Future value of annuity is:", A)
    
else: print("Invalid choice. Please enter 1, 2, or 3.")
