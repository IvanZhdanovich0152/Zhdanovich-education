masm
model small
.stack 100h
.data
X db 0fh
Y dw 0f18ch

.code
start:
;F = (12 * 1369) / X + (Y + 3699)

        mov ax, @data
        mov ds, ax

        mov ax, 0ch
        mov bx, 559h
        mul bx            ; result in DX:AX
        mov cx, ax        ; tk resultat 402ch on vlazit v odno slovo 

        mov al, X         
        cbw               ;razshuryem x do slova i vernym cx v ax, a X v bx
        mov bx, ax
        mov ax, cx

        div bx            ;(12 * 3699) / X chastnoe v AX, ostatok v DX
        mov dx, 0

        mov bx, Y
        add bx, 0e73h 
        add ax, bx
        adc dx, 0
        ;/12

        mov [ds:0010h], ax
        mov [ds:0012h], dx

        mov bx, 12
        div bx

        mov ah, 4ch
        int 21h

end start
















