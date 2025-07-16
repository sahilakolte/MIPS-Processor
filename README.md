# MIPS Processor Design

## Project Overview
This project is a part of **EG 212: Computer Architecture Assignment-2**. The goal is to:
1. Implement **three programs** (Matrix Multiplication, Fibonacci, and Factorial) in **C**, convert them into **MIPS Assembly**, and generate **Machine Code** using the MARS Assembler.
2. Design and implement a **Non-Pipelined MIPS Processor** in Python that can execute the generated machine code following the 5-stage pipeline concept (without actual pipelining):  
   **IF → ID → EX → MEM → WB**

## Features Implemented
- **MIPS Processor Simulator**:
  - Implements 5 stages: Instruction Fetch, Decode, Execute, Memory Access, Write Back.
  - Maintains Program Counter and 32 MIPS registers.
  - Reads machine code from file and executes instructions.
- **Programs Implemented**:
  - **Matrix Multiplication (2x2 matrices)**
  - **Fibonacci Calculation**
  - **Factorial Calculation**
- **Machine Code Execution**:
  - Machine code generated from MARS Assembler for the above programs.
  - Processor reads and executes instructions sequentially.

## Project Structure
```
├── Main Codes/
│   ├── mips_processor.py      # Python implementation of the MIPS processor
│   ├── matrix_multiplication.c
│   ├── fibonacci.c
│   ├── factorial.c
│   ├── matrix_multiplication.asm
│   ├── fibonacci.asm
│   └── factorial.asm
└── Machine Code/
    ├── matrix_multiplication.txt
    ├── fibonacci.txt
    └── factorial.txt

```

## How It Works
- **Step 1:** Write the program in C → Convert it into MIPS Assembly → Generate machine code using **MARS Assembler**.
- **Step 2:** Place machine code files in `Machine Code/`.
- **Step 3:** Run the MIPS processor simulator by loading the machine code file.

## How to Run
1. Clone this repository.
2. Ensure you have Python 3 installed.
3. Open mips_processor.py and update the file path in the open() function (around line 196) to point to the correct machine code file.
4. Run the processor:
   ```bash
   python3 mips_processor.py
   ```

## Assumptions
- Control path is not implemented.
- Instruction & Data memory are implemented as Python dictionaries.
- Memory is **byte-addressable**.
- PC increments by **4** after each instruction fetch.

## Results
- **Matrix Multiplication:** Correct 2x2 matrix multiplication output.
- **Fibonacci:** Calculates nth Fibonacci number.
- **Factorial:** Calculates factorial for n > 0.

## Requirements
- **MARS MIPS Assembler** for generating machine code.
- **Python 3.x** for processor simulation.
