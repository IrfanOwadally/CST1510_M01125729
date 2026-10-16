"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Irfan Owadally
Lane  :  IT     (delete two)
Date  : 07/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#Create a variable and assign a boolean to it
quit = "False"
#Create a variable and assign a value to it
Overlimit = 0
while quit == "False":
    #Prompt a user to enter the label
    label = input("Please enter a record or type quit to exit: ")
    if label == "quit":
        quit = "True"
    else:     
        #Prompt a user to enter a value
        value = float(input("Please enter a first value: "))     
        #Prompt a user to enter a limit
        limit = float(input("PLease enter a second value: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
        #Do the maths operation
        difference = (limit - value)   
        percent = (value / limit) * 100
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
        #Create a variable and store a string to it
        status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

        print()
        #Creating an open interface
        print("=" * 34)
        #Display the label
        print(f"  RECORD CHECK  -  {label}")
        #Creating another interface
        print("=" * 34)
        #Display used that a user has entered for the value
        print(f"  Used        : {value:<10.0f}")
        #Display total that a user has entered for the limit
        print(f"  Total       : {limit:<10.0f}")
        #Display status
        print(f"  Status      : {status:<10}")
        #Closing an interface
        print("=" * 34)
# your report lines go here
        #Creating an interface
        print("=" * 34)
        #Display the label
        print(f" RECORD CHECK    - {label}")
        #Creating another interface
        print("=" * 34)
        #Display Used and the value that a user has entered
        print(f" Used         : {value:>10.2f}")
        #Display Total and the limit that a user has entered
        print(f" Total        : {limit:>10.2f}")
        #Display Free and difference between value and limit
        print(f" Free         : {difference:>+10.2f}")
        #Display percent 
        print(f" Percent      : {percent:>10.2f}%")
        #check if percent is more than or equal to 100
        if percent >= 100:
        #Display the Status
            print(" Status       :         OVER LIMIT")
            #Increment Overlimit by 1
            Overlimit += 1
        #Check if percent is more than or equal to 90
        elif percent >= 90:
        #Display the Status
            print(" Status       :         WARNING")
        #Check if percent does not meet the two conditions above
        else:
            #Display Status
            print(" Status       :         OK")
        #Closing an interface
        print("=" * 34)
#Display the ovrelimit that is counted for the record
print("The over limit for the record is : ", Overlimit)
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
