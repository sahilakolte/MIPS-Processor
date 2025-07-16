.text
.globl main

main:
    li $t0, 6                   # Load 6 into $t0 (n)
    li $t1, 1                   # Initialize $t1 to 1 (factorial)
    beq $t0,$zero,print                  
    
loop:
    mul $t1, $t1, $t0           # $t1 = $t1 * $t0
    addi $t0, $t0, -1           # Decrement n
    
    bgtz $t0, loop              # Branch back to loop if n > 0
 
print:   
    # Print result
    li $v0, 1                   # System call for print integer
    move $a0, $t1               # Load the factorial value into $a0
    syscall

    # Print newline
    li $v0, 11      # System call for print character
    li $a0, '\n'    # Load newline character into $a0
    syscall

    # Exit
    li $v0, 10                  # System call for exit
    syscall
