from __future__ import annotations
from collections import deque

class BinOp:

    def __init__(self, dec:int=None, bitList=None) -> None:
        if(dec == None):
            self.binary = deque(bitList)
        elif(bitList == None):
            self.binary = deque([])
            self.decToBinary(dec)
        else:
            raise ValueError("Constructor passed with empty value")

    @classmethod
    def replicate(cls, obj:BinOp)-> BinOp:
        return cls(bitList=obj.binary)

    @classmethod
    def replicate2sComplement(cls, obj:BinOp)-> BinOp:
        newObj = cls.replicate(obj)
        newObj.binTo2sComplement()
        return newObj
    
    @classmethod
    def nBitBinary(cls, bit:int, nBit:int):
        if(bit != 0 and bit != 1):
            raise ValueError("Invalid bit")
        bitList = [int(x) for x in (str(bit)*nBit)] #no need of ones and zeros function of numpy
        return cls(bitList=bitList)
    
    @classmethod
    def equalize(cls, objList):
        max = objList[0].nBits
        for obj in objList:
            if(obj.nBits > max):
                max = obj.nBits

        for obj in objList:
            while(obj.nBits != max):
                obj.binary.appendleft(obj.binary[0])

    def decToBinary(self, n1):
        if(type(n1) != int):
            raise TypeError("not an integer")
        
        binaryVal= str(bin(n1)).split('b')[1]
        for bit in binaryVal : self.binary.append(int(bit))
        self.binary.appendleft(0)
        if(n1 < 0):
            self.binTo2sComplement()
        #End
    
    def binTo2sComplement(self):
        size = len(self.binary)
        doComplement = False
        for i in range (size-1,-1,-1):
            if(doComplement):
                if(self.binary[i] == 0) :
                    self.binary[i] = 1
                else:
                    self.binary[i] = 0
            elif(self.binary[i] == 1):
                doComplement = True
        #End

    def isNegative(self):
        if(len(self.binary)):
            return self.binary[0] == 1
        else:
            raise ValueError("No binary value found")

    def addBinary(self, obj:BinOp):
        carry = 0
        for i in range(self.nBits-1,-1,-1):
            # print(self.binary[i] , obj.binary[i] , carry)
            if(self.binary[i] == 0 and obj.binary[i] == 0 and carry == 0):
                self.binary[i] = 0
                carry = 0
            elif(self.binary[i] == 0 and obj.binary[i] == 0 and carry == 1):
                self.binary[i] = 1 
                carry = 0
            elif(self.binary[i] == 0 and obj.binary[i] == 1 and carry == 0):
                self.binary[i] = 1 
                carry = 0
            elif(self.binary[i] == 1 and obj.binary[i] == 0 and carry == 0):
                self.binary[i] = 1 
                carry = 0
            elif(self.binary[i] == 0 and obj.binary[i] == 1 and carry == 1):
                self.binary[i] = 0 
                carry = 1
            elif(self.binary[i] == 1 and obj.binary[i] == 0 and carry == 1):
                self.binary[i] = 0 
                carry = 1
            elif(self.binary[i] == 1 and obj.binary[i] == 1 and carry == 0):
                self.binary[i] = 0 
                carry = 1
            elif(self.binary[i] == 1 and obj.binary[i] == 1 and carry == 1):
                self.binary[i] = 1
                carry = 1

    def shiftRight(self, obj:BinOp, Q_1:int) -> int:
        if(len(self.binary) <= 1 or len(obj.binary) <= 1):
            raise ValueError("total bits are less than 2")
        temp = self.binary[0]
        self.binary.rotate(1)
        obj.binary.rotate(1)
        Q_1 = obj.binary[0]
        obj.binary[0] = self.binary[0]
        self.binary[0] = temp
        return Q_1

    def shiftLeft(self, obj:BinOp):
        if(len(self.binary) <= 1 or len(obj.binary) <= 1):
            raise ValueError("total bits are less than 2")
        temp = obj.binary[0]
        obj.binary.rotate(-1)
        self.binary.rotate(-1)
        self.binary[self.nBits-1] = temp
        obj.binary[self.nBits-1] = 0

    
    # Dunder method
    def __str__(self) -> str:
        return ''.join([str(x) for x in self.binary])
        # return f"{self.binary} - {len(self.binary)}"

    # Getters And Setters
    @property
    def nBits(self):
        return len(self.binary)        
