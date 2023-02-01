


master_code = "155274263153"  # falls on a sunday

day_of_the_week = int(input("Enter what day of the week that your birthday falls on in 2023 using the key: Monday = 1, Tuesday = 2, ect..\n\n>"))


for i in range(len(master_code)):
    
    if int(master_code[i]) + day_of_the_week > 7:
        master_code = master_code[:i] + str(int(master_code[i])+day_of_the_week-7) + master_code[i+1:]
    else:
        master_code = master_code[:i] + str(int(master_code[i])+day_of_the_week) + master_code[i+1:]
        

print("Your code is", master_code)






