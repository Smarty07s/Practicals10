basic_salary = int(input("Enter basic salary: "))

if basic_salary >= 50000:
    print("Your salary is Rs."+basic_salary+1000, "with bonus")
elif 50000 < basic_salary >= 30000:
    print("Your salary is Rs."+basic_salary+1500, "with bonus")
elif 30000 < basic_salary >= 10000:
    print("Your salary is Rs."+basic_salary+2000, "with bonus")
elif basic_salary < 10000:
    print("Your salary is Rs."+basic_salary+2500, "with bonus")
