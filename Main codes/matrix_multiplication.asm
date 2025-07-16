.text
.globl main

main:
    # Initialize matrices
    # Matrix A
    li $s0, 1       # A[0][0]
    li $s1, 2       # A[0][1]
    li $s2, 3       # A[1][0]
    li $s3, 4       # A[1][1]

    # Matrix B
    li $s4, 5       # B[0][0]
    li $s5, 6       # B[0][1]
    li $s6, 7       # B[1][0]
    li $s7, 8       # B[1][1]

    # Matrix C (Result)
    li $t2, 0       # C[0][0]
    li $t3, 0       # C[0][1]
    li $t4, 0      # C[1][0]
    li $t5, 0      # C[1][1]

    # Multiply matrices
    # C[0][0]
    mul $t0, $s0, $s4
    mul $t1, $s1, $s6
    add $t2, $t0, $t1

    # C[0][1]
    mul $t0, $s0, $s5
    mul $t1, $s1, $s7
    add $t3, $t0, $t1

    # C[1][0]
    mul $t0, $s2, $s4
    mul $t1, $s3, $s6
    add $t4, $t0, $t1

    # C[1][1]
    mul $t0, $s2, $s5
    mul $t1, $s3, $s7
    add $t5, $t0, $t1

    # Print result (matrix C)
    # Row 1
    li $v0, 1       # System call for print integer
    move $a0, $t2   # Load C[0][0] into $a0
    syscall

    li $v0, 11      # System call for print character
    li $a0, ' '     # Load space character into $a0
    syscall

    li $v0, 1       # System call for print integer
    move $a0, $t3   # Load C[0][1] into $a0
    syscall

    li $v0, 11      # System call for print character
    li $a0, '\n'    # Load newline character into $a0
    syscall

    # Row 2
    li $v0, 1       # System call for print integer
    move $a0, $t4  # Load C[1][0] into $a0
    syscall

    li $v0, 11      # System call for print character
    li $a0, ' '     # Load space character into $a0
    syscall

    li $v0, 1       # System call for print integer
    move $a0, $t5  # Load C[1][1] into $a0
    syscall
    
    li $v0, 11      # System call for print character
    li $a0, '\n'    # Load newline character into $a0
    syscall

    # Exit
    li $v0, 10      # System call for exit
    syscall
