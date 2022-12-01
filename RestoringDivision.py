from binLibrary import BinOp
print("This program demonstrates Restoring Division\n\n")
dividend = int(input("Enter the Dividend :"))
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
    A.shiftLeft(Q)
    A.addBinary(MINUS_M)
    if(A.isNegative()):
        A.addBinary(M)
    else:
        Q.binary[Q.nBits-1] = 1
    print(A,Q," \n")

else:
    print("Final result :")
    print("Remainder : ", A)
    print("Quotient  :", Q)
    