masm 
model small
.stack 100h
.data
        my_str db 'qqqqqqwertyuiopasdfghjklqwertyuiop', '$'
        lenght equ $ - my_str - 1
        res dw 0

.code
        include macro.inc
start:
        init_data

        xor bx, bx 
        count_char my_str, lenght, 'q', bx
        mov res, bx
        print_num res

        close_program
end start


