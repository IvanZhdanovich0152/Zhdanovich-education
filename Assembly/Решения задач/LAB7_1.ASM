masm
model small
.stack 100h

.data
    len equ 10
    array db 1, -3, 5, 20, -7, 8, -9, 4, 0, 200
    sum dw 0
    filename db 'output.txt', 0
    msg db 'Summa polozhitelnyh elementov: $'
    num_str db '     $'           
    handle dw ?

.code
start:
    mov ax, @data
    mov ds, ax

    mov cx, len
    xor si, si
    mov sum, 0

calc:
    mov al, array[si]
    cmp al, 0
    jle skip
    cbw
    add sum, ax
skip:
    inc si
    loop calc

    mov ah, 3Ch
    mov cx, 0
    lea dx, filename
    int 21h
    mov handle, ax

    mov ah, 40h
    mov bx, handle
    lea dx, msg
    mov cx, 31
    int 21h

    mov ax, sum
    mov bx, 10
    lea si, num_str
    add si, 5 

    cmp ax, 0
    jne convert
    mov byte ptr [si], '0'
    jmp write_file

convert:
    xor dx, dx
    div bx
    add dl, '0'
    mov [si], dl
    dec si
    cmp ax, 0
    jne convert
    inc si

write_file:
    mov di, si
    mov cx, 0
len_loop:
    cmp byte ptr [di], ' '
    je write_it
    cmp byte ptr [di], '$'
    je write_it
    inc di
    inc cx
    jmp len_loop

write_it:
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
