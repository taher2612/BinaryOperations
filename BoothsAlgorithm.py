from binLibrary import BinOp
print("This program demonstrates Booth Algorithm\n\n")
multiplicand = int(input("Enter the multiplicand :"))
multiplier = int(input("Enter the multiplier :"))
# Initialization stage
M = BinOp(multiplicand)
MINUS_M = BinOp.replicate2sComplement(M)
Q = BinOp(multiplier)
A = BinOp.nBitBinary(0, Q.nBits)
BinOp.equalize([M,MINUS_M, Q, A])
minusQ = 0
nCycles = Q.nBits
# Main Operation
print("A", " "*A.nBits, "Q"," "*Q.nBits, "Q-1", "nCycle")
for i in range(nCycles, 0, -1):
    print(A,Q,minusQ,"  ", i)
    if(Q.binary[Q.nBits-1] == 1 and minusQ == 0):
        A.addBinary(MINUS_M)
    elif(Q.binary[Q.nBits-1] == 0 and minusQ == 1):
        A.addBinary(M)
    minusQ = A.shiftRight(Q, minusQ)
    print(A,Q,minusQ)
else:
    if(A.isNegative()):
        A.binTo2sComplement()
        Q.binTo2sComplement()
    print("Final result :", A,Q,sep='')
    