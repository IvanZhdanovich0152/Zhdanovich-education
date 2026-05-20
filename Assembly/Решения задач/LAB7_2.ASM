masm
model small
.stack 100h

.data
    len equ 10
    array db 1, -3, 59, 2, 87, 8, -9, 4, 100, -10
    sum dw 0
    filename db 'output.txt', 0
    msg db 'Summa polozhitelnyh elementov: $'
    buffer db 7 dup('$')         
    handle dw ?

.code
start:
    mov ax, @data
    mov ds, ax

    mov cx, len
    xor si, si
    mov sum, 0

sum_loop:
    mov al, array[si]
    cmp al, 0
    jle next
    cbw
    add sum, ax
next:
    inc si
    loop sum_loop

    mov ah, 3Ch
    mov cx, 0
    lea dx, filename
    int 21h
    mov handle, ax
    jc exit

    mov ah, 40h
    mov bx, handle
    lea dx, msg
    mov cx, 31
    int 21h

    lea di, buffer
    mov cx, 6
clear_buffer:
    mov byte ptr [di], '$'
    inc di
    loop clear_buffer

    mov ax, sum
    lea si, buffer
    add si, 5                 
    mov byte ptr [si], '$'    
    dec si

    cmp ax, 0
    jne convert_number
    mov byte ptr [si], '0'
    dec si
    jmp write_number

convert_number:
    mov bx, 10

convert_loop:
    xor dx, dx
    div bx
    add dl, '0'
    mov [si], dl
    dec si
    cmp ax, 0
    jne convert_loop

write_number:
    inc si

    mov di, si
    mov cx, 0
count_len:
    cmp byte ptr [di], '$'
    je write_num
    inc di
    inc cx
    jmp count_len

write_num:
    mov ah, 40h
    mov bx, handle
    mov dx, si
    int 21h

    mov ah, 3Eh
    mov bx, handle
    int 21h

exit:
    mov ah, 4Ch
    int 21h
end start
