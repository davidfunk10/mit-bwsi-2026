# C Programming Basics

## Overview
C is a low-level, compiled programming language used for systems programming, embedded systems, and performance-focused software. It gives programmers direct control over memory and hardware.

---

## Why C Matters
C is widely used in:
- Operating systems
- Embedded devices
- Networking programs
- Cybersecurity tools
- High-performance software

Because C is close to the hardware, it helps build a strong understanding of how computers work.

---

## Basic Program Structure
A C program usually includes:
- Header files
- A `main()` function
- Statements ending in semicolons
- Braces `{}` to group code blocks

### Example
```c


int main() {
    printf("Hello, world!\n");
    return 0;
}
```

Important ideas:
- `main()` is the starting point of the program
- C code is compiled before it runs
- Most statements end with `;`

---

## Common Data Types

| Type | Use | Example |
|------|-----|---------|
| `int` | Whole numbers | `5` |
| `float` | Decimal numbers | `3.14` |
| `double` | More precise decimals | `3.14159` |
| `char` | Single character | `'A'` |

---

## Variables
Variables store data in memory.

Rules:
- A variable must have a type
- A variable should have a clear name
- Its value can change during the program

### Example
```c
int age = 15;
float temp = 72.5;
char grade = 'A';
```

---

## Input and Output
C uses standard input and output functions to interact with the user.

Main ideas:
- `printf()` displays output
- `scanf()` reads input
- `&` is often used in `scanf()` to give the variable’s memory address

### Example
```c
int num;
scanf("%d", &num);
printf("%d\n", num);
```

---

## Operators

### Arithmetic Operators
- `+` add
- `-` subtract
- `*` multiply
- `/` divide
- `%` remainder

### Comparison Operators
- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

### Logical Operators
- `&&` and
- `||` or
- `!` not

---

## Conditionals
Conditionals let a program make decisions.

Main forms:
- `if`
- `else if`
- `else`

### Example
```c
if (x > 0) {
    printf("Positive");
} else {
    printf("Not positive");
}
```

---

## Loops
Loops repeat code.

### `for` loop
Best when you know how many times something should repeat.

```c
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

### `while` loop
Best when the loop should continue until a condition changes.

```c
while (x > 0) {
    x--;
}
```

---

## Functions
Functions are reusable blocks of code that perform a specific task.

Why they matter:
- Make programs more organized
- Reduce repeated code
- Make debugging easier

### Example
```c
int add(int a, int b) {
    return a + b;
}
```

---

## Arrays
An array stores multiple values of the same type in one structure.

Key ideas:
- Arrays have fixed size
- The first element is at index `0`
- Arrays are useful for lists of numbers or characters

### Example
```c
int arr[3] = {1, 2, 3};
printf("%d\n", arr[0]);
```

---

## Strings
In C, a string is an array of characters ending with a null character.

Important idea:
- C does not have a built-in string type like some other languages
- Strings are usually stored as `char` arrays

---

## Pointers
Pointers store memory addresses.

Key ideas:
- `&` means “address of”
- `*` can mean “value at address”
- Pointers are used with arrays, functions, and dynamic memory

### Example
```c
int x = 10;
int *p = &x;
```

---

## Dynamic Memory
C allows memory to be allocated while the program is running.

Common functions:
- `malloc()` allocates memory
- `free()` releases memory

### Example
```c
int *arr = malloc(5 * sizeof(int));
free(arr);
```

Important idea:
- If memory is allocated and never freed, a memory leak can happen

---

## Compilation
C programs must be compiled before they run.

### Example
```bash
gcc program.c -o program
./program
```

---

## Common Mistakes
- Going out of bounds in an array
- Forgetting to free dynamically allocated memory
- Misusing pointers

---

## Key Takeaways
- C is low-level and fast
- It gives direct control over memory
- Pointers are essential to understand
- C is important for systems, embedded programming, and cybersecurity
