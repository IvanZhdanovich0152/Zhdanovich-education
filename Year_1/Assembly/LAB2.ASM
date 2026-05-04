masm 
model small
.stack 100h
.data


; F = 12 - (1369 + X + Y) + Z + 3699
x db 0ah
y dw 0fh
z dd 12345678h


.code
start:

  mov ax, @data
  mov ds, ax
  
  mov al, x
  cbw
  add ax, 1369
  add ax, y

  mov bx, 12
  sub bx, ax   

  mov ax, bx
  cwd

  add ax, word ptr z
  adc dx, word ptr z+2

  add ax, 3699
  adc dx, 0
 
  mov [ds:1000h], ax
  mov [ds:1002h], dx

  mov ah, 4Ch
  int 21h

end start


