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
VSTORE 01
VSTORE 02
VSTORE 03
VSTORE 04
VSTORE 05
VSTORE 06
VSTORE 07
VSTORE 08
VSTORE 09
VSTORE 0A
VSTORE 0B
VSTORE 0C
VSTORE 0D
VSTORE 0E
VSTORE 0F
LOAD_A E1
VSTORE 10
VSTORE 11
VSTORE 12
VSTORE 13
VSTORE 14
VSTORE 15
VSTORE 16
VSTORE 17
HLT
"""
    result = assemble(program)
    print("Machine code:")
    for i, code in enumerate(result):
        print(f"Address {i:02X}: {code}")
    
    print("\nROM contents (paste into Logisim):")
    print(format_for_rom(result))