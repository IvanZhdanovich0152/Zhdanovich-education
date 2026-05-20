save_regs macro
        push es
        push ds
        push ax
        push bx
        push cx
        push dx
        push si
        push di
endm

restore_regs macro
        pop di
        pop si
        pop dx
        pop cx
        pop bx
        pop ax
        pop ds
        pop es
endm

write_str macro handle, str_addr
        local str_len_loop, str_end_write
        
        save_regs

        lea si, str_addr
        mov cx, 0
        
str_len_loop:
        mov al, [si]
        cmp al, '$'
        je str_end_write
        cmp al, 0
        je str_end_write
        inc cx
        inc si
        jmp str_len_loop
        
str_end_write:
        mov ah, 40h
        mov bx, handle
        lea dx, str_addr
        int 21h

        restore_regs
endm

print_num macro num
        local positive_num, print_digits

        push ax
        push bx
        push cx
        push dx

        mov ax, num
        mov cx, 0
        mov bx, 10
        
        test ax, 8000h
        jz positive_num
        
        push ax
        mov ah, 02h
        mov dl, '-'
        int 21h
        pop ax
        neg ax

positive_num:
        xor dx, dx
        div bx
        push dx
        inc cx
        test ax, ax
        jnz positive_num

print_digits:
        pop dx
        add dl, '0'
        mov ah, 02h
        int 21h
        loop print_digits

        pop dx
        pop cx
        pop bx
        pop ax
endm


;====10lab====
init_data macro
        mov ax, @data
        mov ds, ax
endm

close_program macro
        mov ah, 4ch
        int 21h
endm        

print_str macro str_addr
        push ax
        push dx
        lea dx, str_addr
        mov ah, 09h
        int 21h
        pop dx
        pop ax
endm

count_char macro str_addr, len, char, count_reg
        local next_char, end_search

        xor count_reg, count_reg
        mov al, char
        mov cx, len
        lea di, str_addr

        push ds
        pop es
        cld

next_char:
        jcxz end_search
        repne scasb
        jne end_search

        inc count_reg
        jmp next_char

end_search:
endm









