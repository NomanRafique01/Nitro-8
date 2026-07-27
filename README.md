<div align="center">

```
 ███╗   ██╗██╗████████╗██████╗  ██████╗        █████╗ 
 ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗      ██╔══██╗
 ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║█████╗╚█████╔╝
 ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║╚════╝██╔══██╗
 ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝      ╚█████╔╝
 ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚════╝ 
```

# Nitro-8 — Custom 8-bit CPU

![Built With](https://img.shields.io/badge/Built%20With-Logisim%20Evolution-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgo=)
![Language](https://img.shields.io/badge/Assembler-Python%203-yellow?style=for-the-badge&logo=python)
![Architecture](https://img.shields.io/badge/Architecture-8--bit-red?style=for-the-badge)
![Display](https://img.shields.io/badge/Display-16×16%20RGB-purple?style=for-the-badge)
![Instructions](https://img.shields.io/badge/Instructions-16+-orange?style=for-the-badge)
![RAM](https://img.shields.io/badge/RAM-256%20Bytes-green?style=for-the-badge)
![ROM](https://img.shields.io/badge/ROM-2048%20Bytes-cyan?style=for-the-badge&color=00bcd4)
![Storage](https://img.shields.io/badge/Storage-20%20Sprite%20Units-ff69b4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)
![Made In](https://img.shields.io/badge/Made%20In-Pakistan%20🇵🇰-009900?style=for-the-badge)

> A fully functional 8-bit CPU designed and built from scratch in Logisim Evolution, featuring an ALU, custom instruction set, RAM, ROM, RGB pixel display, and a modular sprite storage system.

</div>

---

## Live Demo

<div align="center">

<img src="https://github.com/NomanRafique01/Nitro-8/blob/main/assets/demo.gif/demo.gif?raw=true" width="720" alt="Nitro-8 Live Demo — CPU executing programs on the 16×16 RGB display"/>

*Nitro-8 executing sprite programs on the 16×16 RGB display in real time*

</div>

---

## Screenshots

<div align="center">

### Main CPU Circuit

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/main.png" width="720" alt="Nitro-8 Main CPU Circuit"/>

*Full Nitro-8 CPU — all components wired and running in Logisim Evolution*

</div>

<br/>

<div align="center">

### Control Unit

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/ControlUnit.png" width="380" alt="Nitro-8 Hardwired Control Unit"/>

*Hardwired Control Unit decoding 16+ instructions into micro-control signals*

</div>

<br/>

<div align="center">

### Storage Unit & Screen

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/StorageUnit.png" width="380" alt="Nitro-8 Storage Unit — 20 sprite ROMs"/>&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/Screen.png" width="380" alt="Nitro-8 RGB Display output"/>

*Left — Modular Storage System with 20 independent Sprite Units · Right — 16×16 RGB pixel display output*

</div>

---

## Overview

Nitro-8 is a custom 8-bit processor built entirely from logic gates up. It can fetch, decode, and execute real assembly instructions, perform arithmetic and logic operations, read and write memory, and draw pixel art graphics on a 16×16 RGB display.

This project was built as part of a Computer Architecture course and demonstrates deep understanding of digital logic, CPU design, memory systems, and low-level programming.

---

## Features

- 8-bit ALU (ADD, SUB, AND, OR, XOR, NOT, SHL, SHR)
- Two general-purpose registers (RegA, RegB)
- 8-bit Program Counter with increment, load, and reset
- 16-bit Instruction Register with opcode/operand split
- Hardwired Control Unit decoding 16+ instructions
- 256-byte RAM with read/write support
- 2048-byte banked ROM with bank switching
- 16×16 RGB Video Display (XTerm256 color)
- Modular Storage system with 20 Sprite Units
- Custom Python assembler
- Full reset and halt logic

---

## Instruction Set

| Opcode | Mnemonic    | Description                                   |
|--------|-------------|-----------------------------------------------|
| 10nn   | LOAD_A n    | Load immediate value into RegA                |
| 11nn   | LOAD_B n    | Load immediate value into RegB                |
| 2000   | ADD         | RegA = RegA + RegB                            |
| 2100   | SUB         | RegA = RegA - RegB                            |
| 2200   | AND         | RegA = RegA AND RegB                          |
| 2300   | OR          | RegA = RegA OR RegB                           |
| 30nn   | STORE n     | Store RegA to RAM[n]                          |
| 40nn   | JMP n       | Jump to address n                             |
| 50nn   | JZ n        | Jump to n if RegA = 0                         |
| 60nn   | VSTORE n    | Draw pixel at address n with color RegA       |
| 6100   | VSTORE_B    | Draw pixel at address RegB with color RegA    |
| 7000   | INC         | RegA = RegA + 1                               |
| 7100   | INC_B       | RegB = RegB + 1                               |
| 80nn   | LOAD_RAM n  | RegA = RAM[n]                                 |
| 90nn   | SETBANK n   | Switch ROM bank to n                          |
| F000   | HLT         | Halt the CPU                                  |
| 0000   | NOP         | No operation                                  |

---

## Architecture

```
Clock → PC → ROM/Storage → IR → Control Unit
                                      ↓
                          RegA → ALU → RegB
                                      ↓
                            VideoRAM → RGB Display
                                      ↓
                              RAM (data storage)
```

### Components Built from Scratch

- Half Adder
- Full Adder
- 8-bit Ripple Carry Adder
- 8-bit ALU
- 8-bit Register (D flip-flop based)
- Program Counter (with increment, load, reset)
- Instruction Register (16-bit with opcode/operand split)
- Control Unit (hardwired, 16 instructions)
- RAM8 (256×8)
- ROM8 (2048×16 with bank switching)
- VideoRAM (direct pixel write to RGB Video)
- Storage system (20 Units, MUX-based selection)

---

## RGB Display

The Nitro-8 has a 16×16 pixel RGB display using Logisim's RGB Video component in XTerm256 8-bit color mode.

**How it works:**
- RegA holds the color value
- VSTORE instruction writes color to pixel address
- Address formula: `Address = (row-1) × 16 + (col-1)`
- Row 1 Col 1 = 0x00, Row 16 Col 16 = 0xFF

**Programs that run on the display:**
- Letter rendering (N, I, T, R, O, 8)
- Pixel art sprites (heart, robot, car, etc.)
- Rainbow stripes
- Border patterns
- X pattern

---

## Storage System

The Storage subsystem contains 20 independent Unit ROMs. Each Unit stores one sprite or letter program. A 5-bit counter selects the active Unit via a MUX.

```
Storage
├── Unit1   (Letter N / Sprite 1)
├── Unit2   (Letter I / Sprite 2)
├── Unit3   (Letter T / Sprite 3)
├── Unit4   (Letter R / Sprite 4)
├── Unit5   (Letter O / Sprite 5)
├── Unit6   (Letter 8 / Sprite 6)
├── Unit7   (empty — expandable)
...
└── Unit20  (empty — expandable)
```

Each Unit executes independently. After HLT the next Unit activates automatically.

---

## Python Assembler

The project includes a Python assembler that converts human-readable assembly into Logisim ROM hex format.

**Usage:**
```bash
python assembler.py
```

**Example input:**
```assembly
LOAD_A 05
LOAD_B 03
ADD
HLT
```

**Example output:**
```
1005 0000 1103 0000 2000 0000 F000 0000
0000 0000 ...
```

The assembler automatically inserts NOPs between instructions and pads output to 256 entries for direct paste into Logisim ROM editor.

---

## Build Order

The CPU was built incrementally in this order:

1. Half Adder
2. Full Adder
3. 8-bit Ripple Carry Adder
4. ALU
5. 8-bit Register
6. Program Counter
7. ROM
8. Instruction Register
9. Control Unit
10. Main CPU (connected)
11. RAM
12. JMP and JZ instructions
13. RGB Video Display
14. VSTORE and VSTORE_B instructions
15. INC and INC_B instructions
16. LOAD_RAM instruction
17. SETBANK and bank switching
18. Storage system with 20 Units
19. Python assembler

---

## Demo Programs

**5 + 3 = 8**
```assembly
LOAD_A 05
LOAD_B 03
ADD
HLT
```

**Countdown from 5 to 0**
```assembly
LOAD_A 05
LOAD_B 01
SUB
JZ 0B
JMP 02
HLT
```

**Draw pink heart on screen**
```assembly
LOAD_A D3
VSTORE 34
VSTORE 35
VSTORE 37
VSTORE 38
; ... pixel addresses
HLT
```

---

## Tools Used

| Tool                    | Purpose                        |
|-------------------------|--------------------------------|
| Logisim Evolution v4.1.0| Circuit design and simulation  |
| Python 3                | Assembler                      |
| Git                     | Version control                |
| GitHub                  | Project hosting                |

---

## Project Structure

```
Nitro-8/
├── CPU.circ              Main Logisim circuit file
├── assembler.py          Python assembler
├── README.md             This file
├── assets/
│   ├── demo.gif/
│   │   └── demo.gif      Live demo animation
│   └── screenshots/
│       ├── main.png      Main CPU circuit
│       ├── ControlUnit.png  Control unit
│       ├── StorageUnit.png  Storage subsystem
│       └── Screen.png    RGB display output
└── programs/             Assembly programs (coming soon)
```

---

## Author

<div align="center">

**Noman Rafique (Nomi)**
BS Artificial Intelligence — NFC IET Multan, Pakistan
Semester 2 | GPA 4.0/4.0

[![GitHub](https://img.shields.io/badge/GitHub-NomanRafique01-181717?style=for-the-badge&logo=github)](https://github.com/NomanRafique01)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com)

</div>

---

## License

This project is open source and available under the MIT License.

---

<div align="center">

> Built with patience, logic gates, and a lot of debugging. 🧠

![Visitors](https://img.shields.io/badge/From%20Zero%20to%20CPU-One%20Gate%20at%20a%20Time-ff6b6b?style=for-the-badge)

</div>
