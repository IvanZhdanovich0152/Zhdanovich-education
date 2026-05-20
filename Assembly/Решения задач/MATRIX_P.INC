skip_spaces PROC
skip_loop_local:
        mov al, [si]
        cmp al, ' '
        je skip_char_local
        cmp al, 13
        je skip_char_local
        cmp al, 10
        je skip_char_local
        cmp al, 0
        je end_skip_local
        ret

skip_char_local:
        inc si
        jmp skip_loop_local

end_skip_local:
        ret
skip_spaces ENDP

read_number PROC
        push bx
        push cx
        push dx

        call skip_spaces

        xor ax, ax
        xor bx, bx
        xor cx, cx

        mov bl, [si]
        cmp bl, '-'
        jne read_digit_loop_local
        mov bh, 1
        inc si

read_digit_loop_local:
        mov dl, [si]
        cmp dl, '0'
        jb done_local
        cmp dl, '9'
        ja done_local

        sub dl, '0'
        mov cl, dl

        mov dx, 10
        mul dx
        add ax, cx

        inc si
        jmp read_digit_loop_local

done_local:
        cmp bh, 1
        jne positive_local
        neg ax

positive_local:
        pop bx
        pop cx
        pop dx
        ret
read_number ENDP

ParseMatrix PROC
        save_regs

        lea si, buffer
        call read_number
        mov N, ax
        
        call read_number
        mov M, ax

        lea di, matrix
        mov ax, N
        mov cx, M
        mul cx
        mov cx, ax
        jcxz parse_done

fill_matrix_local:
        push cx
        call read_number
        mov [di], ax
        add di, 2
        pop cx
        dec cx
        jnz fill_matrix_local

parse_done:
        restore_regs
        ret
ParseMatrix ENDP

print_matrix PROC
        save_regs

        lea si, matrix
        mov cx, N

print_row_loop:
        push cx
        mov cx, M

print_col_loop:
        print_num [si]
        print_str space

        add si, 2
        loop print_col_loop

        print_str new_line

        pop cx
        loop print_row_loop

        restore_regs
        ret
print_matrix ENDP

PrintResult PROC
        save_regs

        print_str result_str

        mov cx, N
        lea si, matrix

result_loop_print:
        push cx
        mov cx, M
        xor dx, dx

count_zeros_print:
        mov ax, [si]
        cmp ax, 0
        jne next_num_print
        inc dx

next_num_print:
        add si, 2
        loop count_zeros_print

        print_num dx
        print_str space

        pop cx
        loop result_loop_print
        
        print_str new_line

        restore_regs
        ret
PrintResult ENDP
