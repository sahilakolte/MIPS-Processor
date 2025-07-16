#Converts signed binary to decimal value
def to_dec(binary_str):
    is_negative = False
    if binary_str[0] == '1':
        is_negative = True
        binary_str = ''.join(['1' if bit == '0' else '0' for bit in binary_str])
        binary_str = bin(int(binary_str, 2) + 1)[2:]

    decimal_value = 0
    for digit in binary_str:
        decimal_value = decimal_value * 2 + int(digit)

    if is_negative:
        decimal_value *= -1

    return decimal_value

#converts decimal value to binary
def to_bin(num):
    if num == 0:
        return '0'
    
    if num > 0:
        binary = bin(num)[2:]
        return '0' + binary
    else:
        binary = bin(-num)[2:]
        num_bits = len(binary)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        carry = 1
        result = ''
        for bit in reversed(inverted_binary):
            if bit == '1' and carry == 1:
                result = '0' + result
            elif bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = bit + result
        return '1' + result

#Converts unsigned binary to decimal value    
def to_dec_u(binary_num):
    decimal_num = 0
    power = 0
    for digit in reversed(binary_num):
        decimal_num += int(digit) * (2 ** power)
        power += 1
    return decimal_num


#Dictionary to act as memory
memory = {}


#Class Mips to act as a mips processor   
class MIPS:
    def __init__(self):
        #initialized pc to 0
        self.pc = 0

        #initializing all registers
        self.zero = ["0"]
        self.at = ["0"]
        self.v0 = ["0"]
        self.v1 = ["0"]
        self.a0 = ["0"]
        self.a1 = ["0"]
        self.a2 = ["0"]
        self.a3 = ["0"]
        self.t0 = ["0"]
        self.t1 = ["0"]
        self.t2 = ["0"]
        self.t3 = ["0"]
        self.t4 = ["0"]
        self.t5 = ["0"]
        self.t6 = ["0"]
        self.t7 = ["0"]
        self.s0 = ["0"]
        self.s1 = ["0"]
        self.s2 = ["0"]
        self.s3 = ["0"]
        self.s4 = ["0"]
        self.s5 = ["0"]
        self.s6 = ["0"]
        self.s7 = ["0"]
        self.t8 = ["0"]
        self.t9 = ["0"]
        self.k0 = ["0"]
        self.k1 = ["0"]
        self.gp = ["0"]
        self.sp = ["0"]
        self.fp = ["0"]
        self.ra = ["0"]
        #mapping interger value of registers to their respective registers
        self.reg = {
            '0' : self.zero,
            '1' : self.at,
            '2' : self.v0,
            '3' : self.v1,
            '4' : self.a0,
            '5' : self.a1,
            '6' : self.a2,
            '7' : self.a3,
            '8' : self.t0,
            '9' : self.t1,
            '10' : self.t2,
            '11' : self.t3,
            '12' : self.t4,
            '13' : self.t5,
            '14' : self.t6,
            '15' : self.t7,
            '16' : self.s0,
            '17' : self.s1,
            '18' : self.s2,
            '19' : self.s3,
            '20' : self.s4,
            '21' : self.s5,
            '22' : self.s6,
            '23' : self.s7,
            '24' : self.t8,
            '25' : self.t9,
            '26' : self.k0,
            '27' : self.k1,
            '28' : self.gp,
            '29' : self.sp,
            '30' : self.fp,
            '31' : self.ra
        }

    #this method fetch four bytes of intruction from memory and then increments pc
    #this represents fetch phase
    def fetch(self):
        self.instruction = memory[self.pc] + memory[self.pc+1] + memory[self.pc+2] + memory[self.pc+3]
        self.pc += 4
        return
    
    #this method will run the program till self.running is true
    def run(self):
        self.running = True
        while self.running:
            self.fetch()
            self.execute()
    
    #this method decodes and execute the instruction
    #this represents decode, execute, mem access and write back phase
    def execute(self):
        #syscall instruction
        if to_dec_u(self.instruction[26:32]) == 12:
            if to_dec_u(self.reg['2'][0]) == 10:                 #exits program
                self.running = False

            elif to_dec_u(self.reg['2'][0]) == 1:                #prints content of $a0
                print(to_dec_u(self.reg['4'][0]), end='')

            elif to_dec_u(self.reg['2'][0]) == 11:
                if to_dec_u(self.reg['4'][0]) == 32:             #prints space
                    print(" ", end='')

                elif to_dec_u(self.reg['4'][0]) == 10:           #prints newline
                    print('\n')
            
        #R format instruction
        elif to_dec(self.instruction[0:6]) == 0:
            #add instruction
            if to_dec_u(self.instruction[26:32]) == 32: #checks function field
                self.reg[str(to_dec_u(self.instruction[16:21]))][0] = to_bin(int(to_dec_u(self.reg[str(to_dec_u(self.instruction[6:11]))][0]))+int(to_dec_u(self.reg[str(to_dec_u(self.instruction[11:16]))][0])))[1:]
                
            #addu instruction
            elif to_dec_u(self.instruction[26:32]) == 33: #checks function field
                self.reg[str(to_dec_u(self.instruction[16:21]))][0] = to_bin(to_dec_u(self.reg[str(to_dec_u(self.instruction[6:11]))][0])+to_dec_u(self.reg[str(to_dec_u(self.instruction[11:16]))][0]))[1:]
                           
        #mul instruction
        elif to_dec(self.instruction[0:6]) == 28: #checks opcode
            self.reg[str(to_dec_u(self.instruction[16:21]))][0] = to_bin(to_dec_u(self.reg[str(to_dec_u(self.instruction[6:11]))][0])*to_dec_u(self.reg[str(to_dec_u(self.instruction[11:16]))][0]))[1:]


        else:
            #addiu intruction
            if to_dec(self.instruction[0:6]) == 9: #checks opcode
                self.reg[str(to_dec_u(self.instruction[11:16]))][0] = to_bin(to_dec_u(self.reg[str(to_dec_u(self.instruction[6:11]))][0])+int(to_dec_u(self.instruction[16:32])))[1:]
                
            #addi instruction
            elif to_dec(self.instruction[0:6]) == 8: #checks opcode
                self.reg[str(to_dec_u(self.instruction[6:11]))][0] = to_bin(to_dec_u(self.reg[str(to_dec_u(self.instruction[11:16]))][0])+int(to_dec(self.instruction[16:32])))[1:]
                
            #bgtz instruction
            elif to_dec(self.instruction[0:6]) == 7: #checks opcode
                if to_dec_u(self.reg[str(to_dec_u(self.instruction[6:11]))][0]) > 0:
                    self.pc += to_dec(self.instruction[16:32])*4
                else:
                    return
            

#Reading binary text file and then storing it in memory
command = open("test.txt", "r")
inst = command.readlines()
for i in range(0, len(inst)):
    memory[i*4] = inst[i][0:8]
    memory[i*4 + 1] = inst[i][8:16]
    memory[i*4 + 2] = inst[i][16:24]
    memory[i*4 + 3] = inst[i][24:32]


# # print memory
# for i in range(0, len(inst)*4):
#     print(i, '=' , memory[i])


#creating an object to act as mips processor   
mips = MIPS()
mips.run()    #this runs the program

#clearing the instruction from memory to run other program
memory.clear()