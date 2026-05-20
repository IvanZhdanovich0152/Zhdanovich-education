masm
model small
.stack 100h
.data
    Temp dw ?
    input_Temp_str db 0dh, 0ah, 'Enter Temperature << ', '$'
    output_good_str db 0dh, 0ah, 'Temperature is good', '$'
    output_bad_str db 0dh, 0ah, 'ATTENTION! Temperature is not good', '$'
    incorrect_input_str db 0dh, 0ah, 'Incorrect input! Only digits!', 0dh, 0ah, '$'
    sign db 0

.code
start:
    mov ax, @data
    mov ds, ax

main:
    mov ah, 09h
    mov dx, offset input_Temp_str
    int 21h
    
    call Input_proc
    mov Temp, ax

    
    mov ax, 45
    cmp Temp, ax
    jg opastnost    

    mov ah, 09h
    mov dx, offset output_good_str
    int 21h
    jmp main

opastnost:
    mov ah, 09h
    mov dx, offset output_bad_str
    int 21h

    mov ah, 4ch
    int 21h


Input_proc PROC
    push bx
    push dx

start_input:
    xor bx, bx       
    mov sign, 0      

    mov ah, 01h      
    int 21h

    cmp al, 0dh      
    je error_input
    
    cmp al, '-'      
    jne validate_digit
    mov sign, 1
    jmp next_digit

validate_digit:
    cmp al, '0'
    jb error_input
    cmp al, '9'
    ja error_input
    
    sub al, '0'
    mov ah, 0
    mov bx, ax

next_digit:
    mov ah, 01h
    int 21h
    
    cmp al, 0dh      
    je finish_input

    cmp al, '0'
    jb error_input
    cmp al, '9'
    ja error_input

    sub al, '0'
    cbw
    mov dx, ax       
    
    mov ax, bx
    mov si, 10
    imul si          
    add ax, dx       
    mov bx, ax
    jmp next_digit

error_input:
    mov ah, 09h
    mov dx, offset incorrect_input_str
    int 21h
    
    mov ah, 09h
    mov dx, offset input_Temp_str
    int 21h
    jmp start_input

finish_input:
    mov ax, bx
    cmp sign, 1
    jne exit_label
    neg ax

exit_label:
    pop dx
    pop bx
    ret
Input_proc ENDP

end start
