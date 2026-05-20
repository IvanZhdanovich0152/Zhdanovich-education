masm
.model small
.stack 100h
.data
        old_x dw 0
        old_y dw 0
        trail_color db 15
        bg_color db 0
 
        idle_counter dw 0
        idle_threshold dw 200
        delay_flag db 0
        screen_cleared db 0
      
.code
        include macro.inc
start:
        init_data

        mov ax, 0013h
        int 10h

        mov ax, 0000h
        int 33h
        cmp ax, 0
        jne have_mouse
        jmp no_mouse

have_mouse:
        mov ax, 0001h
        int 33h

main:
        mov ax, 0003h
        int 33h
        shr cx, 1

        test bx, 3
        jz dont_pressed
        jmp exit_program

dont_pressed:
        cmp cx, old_x
        jne mouse_moved
        cmp dx, old_y
        jne mouse_moved
    
        cmp screen_cleared, 1
        je skip_clear_screen

        inc idle_counter
        mov ax, idle_counter
        cmp ax, idle_threshold
        jl skip_clear_screen

        push es
        mov ax, 0a000h
        mov es, ax
        xor di, di
        mov cx, 64000  
        mov al, bg_color
        cld
        rep stosb
        pop es
        
        mov screen_cleared, 1
        mov old_x, 0
        mov old_y, 0

skip_clear_screen:
        jmp skip_draw

mouse_moved:
        mov screen_cleared, 0
        mov idle_counter, 0

        mov ax, 0002h
        int 33h

        call draw_pixel

        mov ax, 0001h
        int 33h

        mov old_x, cx
        mov old_y, dx

skip_draw:
        mov cx, 0
        mov dx, 1500h
        mov ah, 86h
        int 15h

        jmp main

draw_pixel PROC
        push ax
        push di
        push es

        push cx
        mov ax, dx
        mov di, ax
        mov cl, 8
        shl ax, cl
        mov cl, 6
        shl di, cl
        pop cx

        add di, ax
        add di, cx

        mov ax, 0a000h
        mov es, ax

        mov al, trail_color
        mov es:[di], al

        pop es
        pop di
        pop ax
        ret
draw_pixel ENDP


exit_program:
        mov ax, 0003h
        int 10h

no_mouse:
        close_program

end start      
