"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Irfan Owadally
Lane  : IT     (delete two)
Date  : 23/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.
#Prompt a user to enter the data
label = input("Please enter the data: ")
#Prompt a user to enter a first value
first = float(input("Please enter a first value: "))  
#Prompt a user to enter a second value   
second = float(input("Please enter a second value: "))   


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.
#Do the maths operation
difference = (second - first)  
percent = ((first/second) * 100)


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
#Creating an open interface
print("=" * 34)
#Display the label
print(f"  RECORD CHECK  -  {label}")
#Creating another interface
print("=" * 34)
#Display Used that a user has entered for the first value
print(f"  Used        : {first:.0f}")
#Display Total that a user has entered for the second value
print(f"  Total       : {second:.0f}")
#Creating for closing the interface
print("=" * 34)

# : your report lines go here
#Creating an opening interface
print("=" * 34)
#Displaying the label
print(f" RECORD CHECK  - {label}")
#Creating another interface
print("=" * 34)
#Display Used that a user has entered for the first value 
print(f" Used         :  {first:>7.2f}")
#Display Total that a user has entered for the second value 
print(f" Total        :  {second:>7.2f}")
#Display the difference of two value that a user has entered
print(f" Free         :  {difference:>+7.2f}")
#Display the percentage of first value over second value that a user has entered 
print(f" Percent      :  {percent:>7.2f}%")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
