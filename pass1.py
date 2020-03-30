#Rana Mahmoud Amteer
#ID : 161050

inputFile = open("sic.txt" , "r")       #reas sic file
outputFile = open ("out.mdt" , "w")     #create output file
optab = {
"ADD":"18","AND":"40","COMP":"28",
"DIV":"24","J":"3C","JEQ":"30","JGT":"34",
"JLT":"38","JSUB":"48","LDA":"00","LDCH":"50",
"LDL":"08","LDX":"04","MUL":"20","OR":"44","RD":"D8",
"RSUB":"4C","STA":"0C","STCH":"54","STL":"14","STSW":"E8",
"STX":"10","SUB":"1C","TD":"E0","TIX":"2C","WD":"DC","LDB":"68",}       # define opcod for each mnemonic from appendX A
directives = ['START', 'END', 'BYTE', 'WORD',  'RESB', 'RESW', 'BASE', 'NOBASE' ]       #define the directives
file = inputFile.readline()     # read the input file line by line
line = file.strip().split()     # split each line

#separete each column as a list
labelList = list()
opcodeList = list()
operandList = list()
locList = list()
literalList = list()
symbol = {}

#calculate the value of LOCCTR for each instruction in the program
start = line[2].zfill(4)
locList.append(start)
outputFile.write(start + "     ")
outputFile.write("".join(file))
n = 0
noOfLiteral = 0
for i in inputFile.readlines() :
    if "." not in i[:8]:
        labelList.append(i[0:8])
        temp = i[0:8].strip()

        if temp not in directives and temp != "":
            symbol[temp] = str(hex(int(locList[n] , 16)))
        if i[9:15].strip() == "LTORG" or i[9:15].strip() == "RSUB":
            opcodeList.append(i[9:15].strip())
        else :
            opcodeList.append(i[9:15])

        if "=" in i[9:16]:
            if i[15:35].strip() not in literalList :
                literalList.append(i[15:35].strip())
                noOfLiteral += 1
        locct = str(hex(int(locList[n], 16))[2:])
        temp = i[9:15].strip()
        if temp in optab.keys() or temp == "WORD":
            locct = str(hex(int(locList[n],16)+3)[2:])
        elif temp == "RESW":
            tem = int(i[16:35].strip()) * 3
            locct = str(hex(int(locList[n], 16) + tem)[2:])
        elif temp == "RESB":
            locct = str(hex(int(locList[n],16)+int(i[16:35].strip()))[2:])
        elif temp == "BYTE":
            if i[16] == "X":
                 locct = str(hex(int(locList[n], 16) + int((len(i[16:35].strip()) - 3) / 2))[2:])
            elif i[16] == "C":
                 locct = str(hex(int(locList[n], 16) + (len(i[16:35].strip()) - 3))[2:])

        locList.append(locct.zfill(4))
        operandList.append(i[16:35].strip())
        if temp == "LTIRG" and noOfLiteral != 0 or temp == "END" and noOfLiteral != 0 :
            for r in range(noOfLiteral):
                n += 1
                labelList.append("        ")
                opcodeList.append(literalList[r])
                operandList.append("         ")
                if literalList[r][1] == "X":
                    locct = str(hex(int(locList[n], 16) + int((len(literalList[r]) - 4) / 2))[2:])
                elif literalList[r][1] == "C":
                    locct = str(hex(int(locList[n], 16) + (len(literalList[r]) - 4))[2:])
                locList.append(locct.zfill(4))
                noOfLiteral -= 1
            literalList.clear()
        n += 1

PRGNAME = line[0]               # selec what the program name
print("Final location counter : " + str(hex(int(locList[n],16))[2:]))
PRGLTH = str(hex(int(locList[n],16) - int(start,16))[2:])                   #calculate program length
print("Program Name : " + PRGNAME + "\n" + "Program Length : " + PRGLTH)    #print the name of program and length
#print symbol tabel which contain labels and its loc
print("SYMTAB : ")
print(symbol)

# print the intermediate file (result of pass 1 )
for i in range(n):
    outputFile.write(locList[i] + "     " + labelList[i] + "     " + opcodeList[i] +  "     " +operandList[i] + "\n" )

inputFile.close()
outputFile.close()