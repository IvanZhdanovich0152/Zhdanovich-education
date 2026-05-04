masm
model small
.stack 100h
.data
X dw ?
Y dw ?
input_X_str db 'Enter X << ', '$'
input_Y_str db 'Enter Y << ', '$'


.code
start:
; F = (12 * 1369) / X + (Y + 3699)

        mov ax, @data
        mov ds, ax

        mov ah, 09h
        mov dx, offset input_X_str
        int 21h
        
        mov ah, 01h
        int 21h
        sub al, 30h
        mov ah, 0
        mov bx, 10
        mov cx, ax

X_input_loop:
        mov ah, 01h
        int 21h
        cmp al, 0dh
        je End_X

        sub al, 30h
        cbw
        xchg ax, cx
        mul bx
        add cx, ax
        jmp X_input_loop

End_X:
        mov X, cx

        mov ah, 09h
        mov dx, offset input_Y_str
        int 21h

        mov ah, 01h
        int 21h
        sub al, 30h
        mov ah, 0
        mov bx, 10
        mov cx, ax
        
Y_input_loop:
        mov ah, 01h
        int 21h
        cmp al, 0dh
        je End_Y

        sub al, 30h
        cbw
        xchg ax, cx
        mul bx
        add cx, ax
        jmp Y_input_loop

End_Y:
        mov Y, cx


        mov ax, 0ch
        mov bx, 559h
        mul bx
        mov cx, ax

        mov ax, X
        xchg ax, cx

        div cx
        mov dx, 0

        mov bx, Y
        add bx, 0e73h

        add ax, bx
        adc dx, 0

        mov cx, 0

convert:
        mov dx, 0
        mov bx, 10
        div bx
        add dl, 30h
        push dx
        inc cx
        test ax, ax
        jnz convert

print_loop:
        pop dx
        mov ah, 02h
        int 21h
        loop print_loop

        mov ah, 4ch
        int 21h

end start



