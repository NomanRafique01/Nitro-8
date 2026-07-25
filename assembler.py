# Nova-8 Assembler
# Converts assembly code to hex machine code

# Instruction set
INSTRUCTIONS = {
    'NOP':      '0000',
    'ADD':      '2000',
    'SUB':      '2100',
    'AND':      '2200',
    'OR':       '2300',
    'VSTORE_B': '6100',
    'INC':      '7000',
    'INC_B':    '7100',
    'HLT':      'F000',
}

INSTRUCTIONS_WITH_OPERAND = {
    'LOAD_A': '10',
    'LOAD_B': '11',
    'STORE':  '30',
    'JMP':    '40',
    'JZ':     '50',
    'VSTORE': '60',
}

def assemble(code):
    lines = code.strip().split('\n')
    machine_code = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):
            continue
            
        parts = line.split()
        instruction = parts[0].upper()
        
        if instruction in INSTRUCTIONS:
            machine_code.append(INSTRUCTIONS[instruction])
            
        elif instruction in INSTRUCTIONS_WITH_OPERAND:
            operand = int(parts[1], 16)
            opcode = INSTRUCTIONS_WITH_OPERAND[instruction]
            machine_code.append(f'{opcode}{operand:02X}')
            
    return machine_code

def format_for_rom(machine_code):
    with_nops = []
    for code in machine_code:
        with_nops.append(code)
        with_nops.append('0000')
    
    while len(with_nops) < 256:
        with_nops.append('0000')
    
    rows = []
    for i in range(0, 256, 8):
        row = ' '.join(with_nops[i:i+8])
        rows.append(row)
    
    return '\n'.join(rows)

if __name__ == "__main__":
    program = """
LOAD_A 0C
VSTORE 00
VSTORE 10
VSTORE 20
VSTORE 30
VSTORE 40
VSTORE 50
VSTORE 60
VSTORE 70
VSTORE 80
VSTORE 90
VSTORE A0
VSTORE B0
VSTORE C0
VSTORE D0
VSTORE E0
VSTORE F0
VSTORE 11
VSTORE 22
VSTORE 33
VSTORE 44
VSTORE 55
VSTORE 66
VSTORE 77
VSTORE 88
VSTORE 99
VSTORE AA
VSTORE BB
VSTORE CC
VSTORE DD
VSTORE EE
VSTORE 0F
VSTORE 1F
VSTORE 2F
VSTORE 3F
VSTORE 4F
VSTORE 5F
VSTORE 6F
VSTORE 7F
VSTORE 8F
VSTORE 9F
VSTORE AF
VSTORE BF
VSTORE CF
VSTORE DF
VSTORE EF
VSTORE FF
HLT
"""
    result = assemble(program)
    print("Machine code:")
    for i, code in enumerate(result):
        print(f"Address {i:02X}: {code}")
    
    print("\nROM contents (paste into Logisim):")
    print(format_for_rom(result))