#12 Sept 2024. Not the complete version.

optimize:

LDR R3, [R0] @a is in R3
LDR R4, [R0, #4]! @b is in R4
NEG R2, R2
MOV R8, #0 @counter
MOV R6, #10
Mov R7, #100

LOOP:
ADD R8, #1 @counter

MUL R5, R1, R3 @ax in R5
LSL R5, #1 @ax times 2

@ADD R5, R4 @fp is in R5
MLA R5, R4, R6, R5 @fp is in R5
MUL R5, R2, R5
SDIV R5, R7 @change is in R5
ADD R5, R1 @new x is in R5

CMP R1, R5
MOV R1, R5
BNE LOOP

MOV R0, R5
