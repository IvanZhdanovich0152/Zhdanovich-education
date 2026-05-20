masm 
model small
.stack 100h
.data
X db ?
Y dw ?

input_X_str db 'Enter un. char X << ', '$'
input_Y_str db 'Enter un. int Y << ', '$'
primer_str db 'F = (Y / 64) - (X * 36)', 0dh, 0ah, '$'
end_str db 'F = ', '$'
end_neg_str db 'F = -', '$'

is_zero_str db 'Chetnoe', 0dh, 0ah, '$'
not_zero_str db 'Nechetnoe', 0dh, 0ah, '$'
is_neg_str db 'Otricatelnoe', 0dh, 0ah, '$'
not_neg_str db 'Polozhytelnoe', 0dh, 0ah, '$'
                             
sign db 0


.code
start:
        mov ax, @data
        mov ds, ax
  
        mov ah, 09h
        mov dx, offset primer_str
        int 21h

        mov ah, 09h
        mov dx, offset input_X_str
        int 21h
        call Input_proc
        mov X, cl

        mov ah, 09h
        mov dx, offset input_Y_str
        int 21h
        call Input_proc
        mov Y, cx

        mov al, X
        mov ah, 0
        
        mov bx, ax
        mov cl, 5
        shl bx, cl

        mov dx, ax
        mov cl, 2
        shl dx, cl
        add bx, dx
                
        mov ax, Y
        mov cl, 6
        shr ax, cl

        sub ax, bx
        test ax, 1
        jz is_zero   10100011 1
        xchg cx, ax

        mov ah, 09h
        mov dx, offset not_zero_str
        int 21h
        jmp next

is_zero:
        xchg cx, ax
        mov ah, 09h
        mov dx, offset is_zero_str
        int 21h

next:
        test cx, 8000h
        jnz is_neg

        mov ah, 09h
        mov dx, offset not_neg_str
        int 21h
        jmp final

is_neg:
        mov ah, 09h
        mov dx, offset is_neg_str
        int 21h
        mov sign, 1
        neg cx

final:
        xchg cx, ax
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


        cmp sign, 1
        jne not_neg
        mov ah, 09h
        mov dx, offset end_neg_str
        int 21h
        jmp print_loop

not_neg:
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


