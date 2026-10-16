"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammad Irfan Owadally
Lane  :   IT     
Date  :   15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

#Define a function which is called status_of(percent)
def status_of(percent):
    """Check the status of percent if the later is either over limit or warning or ok."""
    #Check the condition if percent is greater than or equal to 100
    if percent >= 100:
        #Overlimit counter is incremented by 1
        Overlimit += 1
        #Return OVER LIMIT to a user
        return "ÖVER LIMIT"
    #Check the condition if percent is greater than or equal to 90
    elif percent >= 90:
        #Return WARNING to a user
        return "WARNING"
    #Check the condition if the two conditions above arer not meeting the criteria
    else:
        #Return OK to a user
        return "OK"
#Define a function which is called check(value, limit)
def check(value, limit):
    """Do difference between value and limit and percentage of value over limit times 100"""
    #Do the maths operation
    difference = limit - value
    percentage = (value / limit) * 100
    #Return difference and percentage to a user
    return difference, percentage
#Define a function which is called print_record(label, value, limit, difference, percent, status)
def print_report(label, value, limit, difference, percent, status):
    """Display all the fields available in the label"""
    #Display the label
    print(f"  RECORD CHECK  -  {label}")
    #Create another interface
    print("=" * 34)
    #Display the label of used and its value
    print(f"  Used         : {value:>9.2f}")
    #Display the label of total and its value
    print(f"  Total        : {limit:>9.2f}")
    #Display the label of free and its value
    print(f"  Free         : {difference:>9.2f}")
    #Display the label of percent and its value
    print(f"  Percent      : {percent:>9.2f}%")
    #Display the label of status and its value
    print(f"  Status       : {status:>9}")



# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#Create a variable and initialise it
quit = "False"
#Create a variable and initialise it
Overlimit = 0
#loop while quit condition is false
while quit == "False":
    #Prompt a user to enter the label
    label = input("Please enter the label or type quit to exit: ")
    #Check the condition if label is corresponding to quit
    if label == "quit":
        #Set quit to True to exit the while loop
        quit = "True"
    #Check the condition if one condition above is not meeting the criteria
    else:
        #Prompt a user to enter a value
        value = float(input("Please enter a value: "))
        #Prompt a user to enter a limit
        limit = float(input("Please enter a limit: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.
        #Call the function of check and store it on two variables at the same time
        difference, percent = check(value, limit)
        #Call the function of percent and store it on a variable
        status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.
        #Display nothing
        print()
        #Creating an open interface
        print("=" * 34)
        #Display the label 
        print(f"  RECORD CHECK  -  {label}")
        #Creating another interface
        print("=" * 34)
        #Display Used and the value that a user has entered
        print(f"  Used         : {value:.0f} ")
        #Display Total and the limit that a user has entered
        print(f"  Total        : {limit:.0f}")
        #Display the status
        print(f"  Status       : {status}")
        #Closing an interface
        print("=" * 34)
# your report lines go here
        #Creating an open interface
        print("=" * 34)
        #Call the function of print_record that contains 6 parameters and display the entire record
        print_report(label, value, limit, difference, percent, status)
        #Closing an interface
        print("=" * 34)
#Display how many overlimits have been found during the record?
print("The overlimit that finds during the records is : ", Overlimit)        

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
