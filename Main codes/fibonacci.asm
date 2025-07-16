.text
.globl main

main:
    li $t0, 10                  # Load 10 into $t0 (n)
    li $t1, 0                   # Initialize $t1 to 0 (fib(n-1))
    li $t2, 1                   # Initialize $t2 to 1 (fib(n))
    beq $t0,$zero,print
    
loop:
    # Calculate fib(n)
    add $t3, $t1, $t2           # $t3 = fib(n-1) + fib(n)
    move $t1, $t2               # fib(n-1) = fib(n)
    move $t2, $t3               # fib(n) = $t3
    addi $t0, $t0, -1           # Decrement n
    bgtz $t0, loop              # Branch back to loop if n > 0

print:
    # Print result
    li $v0, 1                   # System call for print integer
    move $a0, $t1               # Load the Fibonacci value into $a0
    syscall
    
    li $v0, 11      # System call for print character
    li $a0, '\n'    # Load newline character into $a0
    syscall

    # Exit
    li $v0, 10                  # System call for exit
    syscall
