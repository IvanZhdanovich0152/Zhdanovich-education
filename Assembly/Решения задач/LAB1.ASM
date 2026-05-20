masm
.model small
.stack 100h
.data
stroka db 'Nachalo segmenta data','$'
var1 db 10
var2 db 100
var3 dw 1000
var4 dw 10000
adrvar3 dw var3
perem1 db 0ffh
perem2 dw 3a7fh
perem3 dd 0f54d567ah
mas db 10 dup (' ')
pole db 5 dup (?)
adr dw perem3
adr_full dd perem3
fin db 0dh, 0ah, 'Konec segmenta data $'
.code
start:
        mov ax, @data
        mov ds, ax

        mov ah, 09h
        mov dx, offset stroka
        int 21h

        mov ah, 09h
        mov dx, offset fin
        int 21h

        mov ax, 4c00h
        int 21h

end start




