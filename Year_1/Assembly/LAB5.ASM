masm
model small
.stack 100h
.data
Temp dw ?

; 0dh, 0ah, '$'
input_Temp_str db 'Enter Temperature << ', '$'
output_good_str db 'Temperature is good', 0dh, 0ah, '$'
output_bad_str db 'ATTENTION! Temperature is not good', 0dh, 0ah, '$'
incorrect_input_str db 'Incorrect input! Only digits!', 0dh, 0ah, '$'
sign db 0

.code
start:
; if temp > 45: Opastnost

        mov ax, @data
        mov ds, ax


main:
        mov ah, 09h
        mov dx, offset input_Temp_str
        int 21h
        call Input_proc
        mov Temp, cx

        mov ax, 45
        mov bx, Temp
        cmp bx, ax
        jge opastnost

        mov ah, 09h
        mov dx, offset output_good_str
        int 21h

        jmp main

opastnost:
        mov ah, 09h
        mov dx, offset output_bad_str
        int 21h

        mov ah,4ch
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



