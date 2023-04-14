import sys

def hex_to_binary(hex_val):
    bin_val = bin(int(hex_val, 16))[2:]
    bin_val = bin_val.zfill(32)
    return bin_val
input_file = sys.argv[1]
output = []

with open(input_file, 'rb') as f:
    file_content = f.read().decode('utf-8')

lines = file_content.split('\n')

for line in lines:
    if ":" in line:
        inst_parts = line.split(":")
        addr = inst_parts[0].strip()
        hex_values = inst_parts[1].strip().split(" ")
        # addr = 맨 앞 00000000, hex_values : 16진수 4비트씩
        result_list = []
        for el in range(0, len(hex_values), 2):
            result = str(hex_values[el])+str(hex_values[el+1])
            result_list.append(result)
        bin_result_list = []
        for char in result_list:
            bin_result_list.append(hex_to_binary(char))
        print(bin_result_list)
        for char in bin_result_list:
            opcode = char[:7]
            if opcode == "0010011":
                print("addi, slti, sltiu, xori, ori, andi")
            elif opcode == "1100111":
                print("jalr")
            elif opcode =="0000011":
                print("lb,lh,lw,lbu,lhu")
            elif opcode == "0110111":
                print("lui")
            elif opcode == "0010111":
                print("auipc")
            elif opcode == "0010011":
                print("slli, srli, srai")
            elif opcode == "0110011":
                print("add, sub, slt, sltu, xor, or, and, sll, srl, sra")
            elif opcode == "1101111":
                print("jal")
            elif opcode == "1100011":
                print("beq, bne, blt, bge, bltu, bgeu")
            elif opcode == "0100011":
                print("sb, sh, sw")
            else:
                print("unknown instruction")




