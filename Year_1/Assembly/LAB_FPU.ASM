.MODEL small
.386
.stack 100h

.data
        X       dq      0.987654321
        Y       dq      3.1415926535
        Z       dq      9.87654321
        RESULT  dq      ?

.code
start:
        mov ax, @data
        mov ds, ax
        finit
        ;F = cos(X) - (sin(X) + X + Y) + Z + tg(X)

        fld X
        fsin    ;  0.8347366295 (1F18AB397h)     
        fld X
        faddp st(1), st(0)   ; 1.8223909505 (43E3ACA81h)
        fld Y
        faddp  ;st0 = sinx + x + y     ; 4.963983640 (B8EC3C988h)

        fld X
        fcos          ; 0.5506493978 (148366E1Ah)
        fsubrp st(1), st   ;st0 = cosx - scobki ; -4.4133342061 (FFFFFFF5B972A493h)

        fld Z
        faddp   ;st0 = cosx - scobki + Z  ; 5.4632090038 (CB85389B6h)

        fld X
        fptan    ; 1.5159130886 (3878DFB06h)
        fstp st(0)
        faddp    ;6.9791220925 (103FE184BDh)

        fstp RESULT

        mov ah, 4Ch
        int 21h
end start


