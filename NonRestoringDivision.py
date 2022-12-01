from binLibrary import BinOp
print("This program demonstrates Non Restoring Division\n\n")
dividend = int(input("Enter the dividend :"))
divisor = int(input("Enter the divisor :"))
# Initialization stage
M = BinOp(divisor)
MINUS_M = BinOp.replicate2sComplement(M)
Q = BinOp(dividend)
A = BinOp.nBitBinary(0, Q.nBits)
BinOp.equalize([M,MINUS_M, Q, A])
nCycles = Q.nBits
# Main Operation
print("A", " "*A.nBits, "Q"," "*Q.nBits, "nCycle\n")
for i in range(nCycles, 0, -1):
    print(A,Q,"   ", i)
    if(A.isNegative()):
        A.shiftLeft(Q)
        A.addBinary(M)
    else:
        A.shiftLeft(Q)
        A.addBinary(MINUS_M)
    if(not A.isNegative()):
        Q.binary[Q.nBits-1] = 1
    
    print(A,Q," \n")

else:
    if(A.isNegative()):
        A.addBinary(M)
        print("Final result :")
        print("Remainder : ", A)
        print("Quotient  :", Q)