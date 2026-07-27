<div align="center">

```
 ███╗   ██╗██╗████████╗██████╗  ██████╗        █████╗ 
 ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗      ██╔══██╗
 ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║█████╗╚█████╔╝
 ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║╚════╝██╔══██╗
 ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝      ╚█████╔╝
 ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚════╝ 
```

# Nitro-8 &nbsp;·&nbsp; Custom 8-bit CPU

[![Built With](https://img.shields.io/badge/Built%20With-Logisim%20Evolution-0a74da?style=for-the-badge)](https://github.com/logisim-evolution/logisim-evolution)
[![Language](https://img.shields.io/badge/Assembler-Python%203-f7c948?style=for-the-badge&logo=python&logoColor=000)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-8--bit-e03c3c?style=for-the-badge)](#architecture)
[![Display](https://img.shields.io/badge/Display-16×16%20RGB-8b5cf6?style=for-the-badge)](#rgb-display)
[![Instructions](https://img.shields.io/badge/Instructions-16+-f97316?style=for-the-badge)](#instruction-set)
[![RAM](https://img.shields.io/badge/RAM-256%20Bytes-22c55e?style=for-the-badge)](#architecture)
[![ROM](https://img.shields.io/badge/ROM-2048%20Bytes-06b6d4?style=for-the-badge)](#architecture)
[![Storage](https://img.shields.io/badge/Storage-20%20Sprite%20Units-ec4899?style=for-the-badge)](#storage-system)
[![Status](https://img.shields.io/badge/Status-Active-16a34a?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-6b7280?style=for-the-badge)](#license)
[![Made In](https://img.shields.io/badge/Made%20In-Pakistan%20🇵🇰-009900?style=for-the-badge)](#author)

<br/>

> **Nitro-8** is a fully functional 8-bit CPU designed and built entirely from scratch in Logisim Evolution —
> featuring a hardwired ALU, custom 16-instruction ISA, banked ROM, 256-byte RAM,
> a 16×16 RGB pixel display, and a modular 20-unit sprite storage system.

<br/>

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Live Simulation](#live-simulation)
- [Circuit Screenshots](#circuit-screenshots)
- [Instruction Set](#instruction-set)
- [RGB Display](#rgb-display)
- [Storage System](#storage-system)
- [Python Assembler](#python-assembler)
- [Demo Programs](#demo-programs)
- [Build Order](#build-order)
- [Tools Used](#tools-used)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)

---

## Overview

Nitro-8 is a custom 8-bit processor built entirely from logic gates up — no shortcuts, no black-box components. Every subsystem, from the half adder at the bottom of the ALU to the MUX-driven sprite storage at the top, was constructed and verified gate by gate inside Logisim Evolution.

The CPU can **fetch, decode, and execute** real assembly instructions, perform arithmetic and bitwise operations, read and write memory, and render pixel-art graphics on a live 16×16 RGB display — all in a single integrated circuit.

> Built as part of a Computer Architecture course at NFC IET Multan, this project demonstrates end-to-end understanding of digital logic, processor microarchitecture, memory systems, and low-level programming.

---

## Features

| Category | Capability |
|---|---|
| **ALU** | ADD, SUB, AND, OR, XOR, NOT, SHL, SHR — all 8-bit |
| **Registers** | RegA, RegB — two general-purpose 8-bit registers |
| **Program Counter** | 8-bit PC with increment, load, and synchronous reset |
| **Instruction Register** | 16-bit IR with opcode / operand split |
| **Control Unit** | Hardwired, decodes 16+ instructions into micro-signals |
| **RAM** | 256 × 8 read/write data memory |
| **ROM** | 2048 × 16 banked program memory with SETBANK switching |
| **Video** | 16×16 RGB display, XTerm256 8-bit color, direct pixel write |
| **Storage** | 20 independent Sprite Unit ROMs, MUX-selected |
| **Assembler** | Custom Python assembler → Logisim ROM hex format |
| **Control Flow** | JMP, JZ (conditional), HLT, NOP |
| **Reset** | Full synchronous reset across all registers and memory |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         NITRO-8 CPU                             │
│                                                                 │
│   Clock ──► PC ──► ROM / Storage ──► IR ──► Control Unit       │
│                                                   │             │
│                              ┌────────────────────┘             │
│                              ▼                                  │
│                        RegA ──► ALU ◄── RegB                    │
│                              │                                  │
│                    ┌─────────┴──────────┐                       │
│                    ▼                    ▼                       │
│             VideoRAM ──► RGB Display   RAM (data)               │
└─────────────────────────────────────────────────────────────────┘
```

### Components Built from Scratch

- Half Adder → Full Adder → 8-bit Ripple Carry Adder
- 8-bit ALU (8 operations)
- 8-bit D flip-flop Register × 2
- 8-bit Program Counter (inc / load / reset)
- 16-bit Instruction Register (opcode + operand split)
- Hardwired Control Unit (16 instructions)
- RAM8 — 256×8 synchronous read/write
- ROM8 — 2048×16 with bank switching
- VideoRAM — direct pixel write to RGB Video component
- Storage System — 20 Unit ROMs, 5-bit MUX selection

---

## Live Simulation

<div align="center">

<br/>

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/demo/demo1.gif" width="1280" alt="Nitro-8 Live Simulation — CPU running sprite programs on the 16×16 RGB display"/>

<br/>

*Nitro-8 live simulation — the CPU fetching, decoding, and executing sprite programs,*
*cycling through all 20 Storage Units and painting pixel art on the 16×16 RGB display.*

<br/>

</div>

---

## Circuit Screenshots

<div align="center">

### ① &nbsp; Main CPU — Full Circuit

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/main.png" width="840" alt="Nitro-8 — Full Main CPU Circuit in Logisim Evolution"/>

*Complete Nitro-8 CPU — ALU, registers, PC, ROM, RAM, control unit, and video display, all wired and running.*

</div>

<br/>

<div align="center">

### ② &nbsp; Control Unit &nbsp;&nbsp;|&nbsp;&nbsp; ③ &nbsp; Storage System &nbsp;&nbsp;|&nbsp;&nbsp; ④ &nbsp; RGB Display Output

<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/ControlUnit.png" width="370" alt="Nitro-8 Hardwired Control Unit"/>&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/StorageUnit.png" width="370" alt="Nitro-8 Storage System — 20 Sprite Units"/>&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/NomanRafique01/Nitro-8/main/assets/screenshots/Screen.png" width="370" alt="Nitro-8 16×16 RGB Display Output"/>

*Left — Hardwired Control Unit &nbsp;·&nbsp; Centre — 20-Unit Sprite Storage with MUX selection &nbsp;·&nbsp; Right — 16×16 RGB pixel display rendering a sprite*

</div>

---

## Instruction Set

| Opcode | Mnemonic | Operation |
|:------:|----------|-----------|
| `10nn` | `LOAD_A n` | RegA ← n |
| `11nn` | `LOAD_B n` | RegB ← n |
| `2000` | `ADD` | RegA ← RegA + RegB |
| `2100` | `SUB` | RegA ← RegA − RegB |
| `2200` | `AND` | RegA ← RegA AND RegB |
| `2300` | `OR` | RegA ← RegA OR RegB |
| `30nn` | `STORE n` | RAM[n] ← RegA |
| `40nn` | `JMP n` | PC ← n |
| `50nn` | `JZ n` | if RegA = 0 → PC ← n |
| `60nn` | `VSTORE n` | VideoRAM[n] ← RegA (color) |
| `6100` | `VSTORE_B` | VideoRAM[RegB] ← RegA |
| `7000` | `INC` | RegA ← RegA + 1 |
| `7100` | `INC_B` | RegB ← RegB + 1 |
| `80nn` | `LOAD_RAM n` | RegA ← RAM[n] |
| `90nn` | `SETBANK n` | ROM bank ← n |
| `F000` | `HLT` | Halt execution |
| `0000` | `NOP` | No operation |

---

## RGB Display

The Nitro-8 drives a **16×16 pixel RGB display** using Logisim Evolution's RGB Video component in **XTerm256 8-bit color mode**, giving 256 distinct colors addressable by a single byte.

**Pixel addressing:**
```
Address = (row − 1) × 16 + (col − 1)
Row 1, Col 1 → 0x00      Row 16, Col 16 → 0xFF
```

**Programs rendered on the display:**
- Alphabet letters — N, I, T, R, O, 8
- Pixel-art sprites — heart, robot, rocket, car
- Rainbow stripe fill
- Checkerboard and border patterns
- Diagonal X pattern

---

## Storage System

The Storage subsystem contains **20 independent Unit ROMs**. Each Unit holds one complete sprite or letter program. A 5-bit counter advances the active Unit via a MUX — when one program halts, the next Unit fires automatically.

```
Storage
├── Unit 01  — Letter N
├── Unit 02  — Letter I
├── Unit 03  — Letter T
├── Unit 04  — Letter R
├── Unit 05  — Letter O
├── Unit 06  — Letter 8
├── Unit 07  — Sprite (expandable)
├── ...
└── Unit 20  — (expandable)
```

---

## Python Assembler

The project ships a Python assembler that compiles human-readable Nitro-8 assembly into the hex format expected by Logisim's ROM editor.

```bash
python assembler.py
```

**Input → Output example:**

```assembly
; Source
LOAD_A 05
LOAD_B 03
ADD
HLT
```

```
; ROM hex output
1005 0000 1103 0000 2000 0000 F000 0000
0000 0000 0000 0000 ...  (padded to 256 entries)
```

NOPs are automatically inserted between instructions to satisfy the CPU's fetch cycle, and output is zero-padded to 256 entries for direct paste into the Logisim ROM editor.

---

## Demo Programs

<details>
<summary><strong>5 + 3 = 8 &nbsp;(arithmetic)</strong></summary>

```assembly
LOAD_A 05
LOAD_B 03
ADD
HLT
```
</details>

<details>
<summary><strong>Countdown 5 → 0 &nbsp;(loop + branch)</strong></summary>

```assembly
LOAD_A 05
LOAD_B 01
SUB          ; RegA = RegA - 1
JZ   0B      ; if zero → halt
JMP  02      ; else loop
HLT
```
</details>

<details>
<summary><strong>Draw pink heart &nbsp;(VSTORE pixel painting)</strong></summary>

```assembly
LOAD_A D3    ; XTerm256 pink
VSTORE 34
VSTORE 35
VSTORE 37
VSTORE 38
; ... remaining pixel addresses
HLT
```
</details>

---

## Build Order

The CPU was assembled incrementally, each layer verified before the next was added:

```
 1  Half Adder               11  RAM
 2  Full Adder               12  JMP + JZ instructions
 3  8-bit Ripple Carry Adder 13  RGB Video Display
 4  ALU                      14  VSTORE + VSTORE_B
 5  8-bit Register           15  INC + INC_B
 6  Program Counter          16  LOAD_RAM
 7  ROM                      17  SETBANK + bank switching
 8  Instruction Register     18  Storage system (20 Units)
 9  Control Unit             19  Python assembler
10  Main CPU integration
```

---

## Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution) | v4.1.0 | Circuit design & simulation |
| Python | 3.x | Custom assembler |
| Git | — | Version control |
| GitHub | — | Hosting & CDN asset delivery |

---

## Project Structure

```
Nitro-8/
├── CPU.circ                  ← Main Logisim circuit
├── assembler.py              ← Python assembler
├── README.md
├── assets/
│   ├── demo/
│   │   └── demo1.gif         ← Live simulation recording
│   └── screenshots/
│       ├── main.png          ← Full CPU circuit
│       ├── ControlUnit.png   ← Hardwired control unit
│       ├── StorageUnit.png   ← 20-unit sprite storage
│       └── Screen.png        ← RGB display output
└── programs/                 ← Assembly programs (coming soon)
```

---

## Author

<div align="center">

<br/>

**Noman Rafique (Nomi)**

*BS Artificial Intelligence &nbsp;·&nbsp; NFC IET Multan, Pakistan*
*Semester 2 &nbsp;·&nbsp; GPA 4.0 / 4.0*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-NomanRafique01-181717?style=for-the-badge&logo=github)](https://github.com/NomanRafique01)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)

<br/>

</div>

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

<br/>

*Built with patience, logic gates, and a lot of debugging.* &nbsp;🧠

<br/>

![](https://img.shields.io/badge/From%20Zero%20to%20CPU-One%20Gate%20at%20a%20Time-ff6b6b?style=for-the-badge)

<br/>

</div>
