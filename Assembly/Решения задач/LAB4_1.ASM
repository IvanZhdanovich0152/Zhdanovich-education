masm
model small
.stack 100h
.data
X dw ?
Y dw ?
input_X_str db 'Enter X << ', '$'
input_Y_str db 'Enter Y << ', '$'
primer_str db 'F = (12 * 1369) / X + (Y + 3699)', 0dh, 0ah, '$'
end_str db 'F = ', '$'
sign db 0

.code
start:
; F = (12 * 1369) / X + (Y + 3699)

        mov ax, @data
        mov ds, ax

        mov ah, 09h
        mov dx, offset primer_str
        int 21h

        mov ah, 09h
        mov dx, offset input_X_str
        int 21h
        call Input_proc
        mov X, cx

        mov ah, 09h
        mov dx, offset input_Y_str
        int 21h
        call Input_proc
        mov Y, cx

        mov ax, 0ch
        mov bx, 559h
        mul bx
        mov cx, X
        cwd
        idiv cx
        mov dx, 0

        mov bx, Y

        add bx, 0e73h
        adc dx, 0

        add ax, bx
        adc dx, 0

        mov cx, 0

convert:
        mov bx, 10
        div bx
        add dl, 30h
        push dx
        inc cx

        xor dx, dx
        test ax, ax
        jnz convert

        mov ah, 09h
        mov dx, offset end_str
        int 21h

print_loop:
        pop dx
        mov ah, 02h
        int 21h
        loop print_loop

        mov ah, 4ch
        int 21h


Input_proc PROC
        mov sign, 0

        mov ah, 01h
        int 21h

        cmp al, 2dh
        jne check_digit
        mov sign, 1
        jmp input_loop

check_digit: 
        sub al, 30h
        mov ah, 0
        mov bx, 10
        mov cx, ax

input_loop:
        mov ah, 01h
        int 21h
        cmp al, 0dh
        je Finish_input

        sub al, 30h
        cbw

        xchg ax, cx
        mul bx
        add cx, ax
        jmp input_loop

Finish_input:
        cmp sign, 1
        jne Exit_label
        neg cx

Exit_label:
        RET
Input_proc ENDP

end start



