byte_to_str PROC
        push bx
        xor ah, ah
        mov bl, 10
        div bl
        add al, '0'
        add ah, '0'
        pop bx
        ret
byte_to_str ENDP

WriteNumToFile PROC
        save_regs

        mov si, 0
        mov bx, 10
        
        test ax, 8000h
        jz convert_num
        
        neg ax
        push ax
        
        mov ah, 40h
        mov bx, out_handle
        mov cx, 1
        lea dx, minus
        int 21h
        
        pop ax

convert_num:
        xor dx, dx
        div bx
        add dl, '0'
        push dx
        inc si
        test ax, ax
        jnz convert_num

write_digits:
        pop dx
        mov temp_char, dl
        
        push si
        mov ah, 40h
        mov bx, out_handle
        mov cx, 1
        lea dx, temp_char
        int 21h
        pop si
        
        dec si
        jnz write_digits

        restore_regs
        ret

WriteNumToFile ENDP

GetDateTime PROC
        save_regs

        mov ah, 2ah
        int 21h
        
        lea si, date_buffer
        
        mov al, dl
        call byte_to_str
        mov [si], al
        mov [si+1], ah
        mov byte ptr [si+2], '-'
        
        mov al, dh
        call byte_to_str
        mov [si+3], al
        mov [si+4], ah
        mov byte ptr [si+5], '-'
        
        mov ax, cx
        mov bl, 100
        div bl
        mov al, ah
        call byte_to_str
        mov [si+6], al
        mov [si+7], ah
        mov byte ptr [si+8], '$'
        
        mov ah, 2ch
        int 21h
        
        lea si, time_buffer
        
        mov al, ch
        call byte_to_str
        mov [si], al
        mov [si+1], ah
        mov byte ptr [si+2], ':'
        
        mov al, cl
        call byte_to_str
        mov [si+3], al
        mov [si+4], ah
        mov byte ptr [si+5], ':'
        
        mov al, dh
        call byte_to_str
        mov [si+6], al
        mov [si+7], ah
        mov byte ptr [si+8], '$'

        restore_regs
        
        ret
GetDateTime ENDP

OpenFileIN PROC
        push ax
        push dx
        lea dx, input_file
        mov ax, 3d00h
        int 21h
        mov in_handle, ax
        pop dx
        pop ax
        ret
OpenFileIN ENDP

CloseFileIN PROC
        push ax
        push bx
        mov ah, 3eh
        mov bx, in_handle
        int 21h
        pop bx
        pop ax
        ret
CloseFileIN ENDP

CreateFileOUT PROC
        push ax
        push cx
        push dx
        mov ah, 3ch
        mov cx, 0
        lea dx, output_file
        int 21h
        mov out_handle, ax
        pop dx
        pop cx
        pop ax
        ret
CreateFileOUT ENDP

CloseFileOUT PROC
        push ax
        push bx
        mov ah, 3eh
        mov bx, out_handle
        int 21h
        pop bx
        pop ax
        ret
CloseFileOUT ENDP

ReadFileToBuffer PROC
        push ax
        push bx
        push cx
        push dx
        mov ah, 3fh
        mov bx, in_handle
        mov cx, 512
        lea dx, buffer
        int 21h
        mov bx, ax
        mov buffer[bx], 0
        pop dx
        pop cx
        pop bx
        pop ax
        ret
ReadFileToBuffer ENDP

WriteMatrixToFile PROC
        save_regs

        lea si, matrix
        mov cx, N
        
matrix_row_file:
        push cx
        mov cx, M

matrix_col_file:
        mov ax, [si]
        push si
        call WriteNumToFile
        pop si
        
        write_str out_handle, space
        
        add si, 2
        loop matrix_col_file
        
        write_str out_handle, new_line
        
        pop cx
        loop matrix_row_file

        restore_regs
        ret
WriteMatrixToFile ENDP

WriteResultToFile PROC
        save_regs

        mov cx, N
        lea si, matrix

result_row_file:
        push cx
        mov cx, M
        xor dx, dx

result_col_file:
        mov ax, [si]
        cmp ax, 0
        jne not_zero_f
        inc dx

not_zero_f:
        add si, 2
        loop result_col_file
        
        mov ax, dx
        call WriteNumToFile
        write_str out_handle, space
        
        pop cx
        loop result_row_file
        
        write_str out_handle, new_line

        restore_regs
        ret
WriteResultToFile ENDP

WriteOutputFile PROC
        save_regs

        call GetDateTime
        
        write_str out_handle, datetime_str
        write_str out_handle, date_buffer
        write_str out_handle, space
        write_str out_handle, time_buffer
        write_str out_handle, new_line
        
        write_str out_handle, file_info_str
        write_str out_handle, output_file
        write_str out_handle, new_line
        write_str out_handle, new_line
        
        write_str out_handle, matrix_str
        call WriteMatrixToFile
        write_str out_handle, new_line
       
        write_str out_handle, result_str
        call WriteResultToFile

        restore_regs
        ret
WriteOutputFile ENDP
