"""Point to be noted cake is considered circular
   Minimum angle/Pieces = 1 Degree
   Maximum Pieces Possible = 360 """


"""First condition {(1). Cut the cake into N equal pieces.}"""

N=int(input("Enter The Number Of Cuts You Want 'N': "))   # Entering Number Of Cuts You Want
if N==1 or N==360:
    print("Enter the value of 'N' Such That 1 < N <= 360")
elif (360%N)==0:
    print("First Answer: YES",N,"Equal Pieces Are Possible")
else:
    print("First Answer: NO",N,"Equal Pieces Are Not Possible")



"""Second Condition {(2). Cut the cake into N pieces of any size}"""


sum=0
for i in range(N):
    a=int(input("Enter The Angle Size Total Of 360= "))
    sum=sum+a
if sum==360:
    print("Second Answer YES: Cake Can Be cutted  In ",N,"Pieces")
else:
    print("Second Answer NO: Total Is Not 360, Hence Re-Enter the Values")



""""Third Condition   {(3). Cut the Cake into N Pieces Such That No Any Two Of  Them Are Equal} """

"""Considering Minimum Angle Sum For  Maximum Output
 1+2+3+4+........23+24+25+35=360 
i.e N=26 
If N>=27 Small Angle Will Be Repeated And  Henceforth  
Larger Values Will Also Be Repeated  
"""

if N <= 26:
    print("Third Answer YES: Unequal Pieces Are Possible")
else:
    print("Third Answer NO: Unequal Pieces Are Not Possible")
