# Assembly Programming Basics

## Overview
Assembly language is a low-level programming language that is closely tied to a computer’s instruction set architecture (ISA). It uses short mnemonic commands to represent machine instructions.

---

## Why Assembly Matters
Assembly is important because it helps explain how software interacts directly with hardware.

It is used in:
- Operating systems
- Embedded systems
- Reverse engineering
- Malware analysis
- Exploit development
- Performance-critical code

---

## Key Idea
Assembly is much lower-level than languages like Python, Java, or C.

That means:
- fewer abstractions
- more direct hardware control
- more detail for every operation

---

## ISA (Instruction Set Architecture)
An instruction set architecture is the interface between hardware and software.

Examples:
- x86
- x86-64
- ARM

Different ISAs use different assembly instructions and registers.

---

## Machine Code vs Assembly
- **Machine code** is binary instructions that the CPU executes directly
- **Assembly** is a human-readable representation of machine code

Assembly is translated into machine code by an **assembler**.

---

## Basic Structure
An assembly program is made of instructions that tell the CPU exactly what to do.

Common parts:
- instructions
- registers
- memory addresses
- labels
- directives

---

## Registers
Registers are very small, very fast storage locations inside the CPU.

They are used to:
- hold temporary values
- store memory addresses
- help perform calculations

Examples in x86-64:
- `rax`
- `rbx`
- `rcx`
- `rdx`
- `rsp`
- `rbp`

---

## Common Instructions

| Instruction | Purpose |
|------------|---------|
| `mov` | move data |
| `add` | add values |
| `sub` | subtract values |
| `cmp` | compare values |
| `jmp` | jump to another location |
| `call` | call a function |
| `ret` | return from a function |
| `push` | put value on stack |
| `pop` | remove value from stack |

---

## Example Instructions
- `mov` copies data from one place to another
- `add` adds values
- `sub` subtracts values
- `cmp` compares two values
- `jmp` changes program flow

---

## Program Flow
Assembly often controls flow using:
- comparisons
- jumps
- labels

This is how assembly handles logic like:
- if statements
- loops
- function calls

---

## Labels
Labels are names for locations in code.

They are often used as jump targets.

Example idea:
- a loop may jump back to a label
- a conditional branch may jump to a label if a condition is true

---

## The Stack
The stack is a region of memory used for temporary storage during program execution.

It commonly stores:
- function parameters
- local variables
- return addresses
- saved register values

Important stack-related instructions:
- `push`
- `pop`

Important registers:
- `rsp` = stack pointer
- `rbp` = base pointer

---

## Function Calls
When a function is called in assembly:
- arguments may go into registers or onto the stack
- the return address is saved
- local storage may be created on the stack
- the function eventually returns with `ret`

This creates a **stack frame**.

---

## Memory
Assembly can work directly with memory addresses.

This allows programs to:
- read data from memory
- write data to memory
- store pointers
- manipulate buffers

This power is useful, but mistakes can also be dangerous.

---

## Assembly and C
Assembly and C are closely related.

C is higher-level, but many C operations become assembly instructions after compilation.

Learning assembly helps explain:
- how variables are stored
- how functions work
- how memory is accessed
- how vulnerabilities happen

---

## Common Uses in Cybersecurity
Assembly is useful in cybersecurity for:
- reverse engineering programs
- analyzing malware
- understanding exploits
- studying buffer overflows
- reading disassembled code

---

## Common Mistakes
- confusing values and addresses
- forgetting how registers change
- misunderstanding stack behavior
- using the wrong instruction for the architecture
- assuming all assembly languages are the same

---

## Key Takeaways
- Assembly is a low-level language tied to a CPU architecture
- It uses mnemonics to represent machine instructions
- Registers and memory are central concepts
- The stack is important for function calls and local data
- Assembly is very useful in systems programming and cybersecurity
