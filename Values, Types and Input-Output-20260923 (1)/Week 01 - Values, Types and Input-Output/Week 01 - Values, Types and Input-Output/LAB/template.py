"""
RECORD CHECK  -  my version
===========================

Name  : Sri Geetika Kanakamedala
Lane  :  AI 
Date  : 27/9/26

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

hostname = input("enter host name:")      
used = float(input("Enter used space:"))    
total= float(input("Enter total space:"))  


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
difference = total - used  
percent = (used / total * 100)  
free = total - used


# =================================================================== OUTPUT


print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"ussed space: {used:>10.2f}")
print(f"total space: {total:>10.2f}")
print(f"difference: {difference:>+10.2f}")
print(f"percent: {percent:>10.2f}")
print(f"free space: {free:>10.2f}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
