masm
.model small
.stack 100h

.data
        matrix dw 100 dup(?)
        N dw ?
        M dw ?

        input_file db 'matrix.txt', 0
        output_file db 'result.txt', 0
        in_handle dw ?
        out_handle dw ?

        temp_char db ?

        buffer db 512 dup(?)
        date_buffer db 11 dup(?)
        time_buffer db 9 dup(?)

        matrix_str db 'Matrix:', 13, 10, '$'
        result_str db 13, 10, 'Zeros in each row: ', 13, 10, '$'
        file_info_str db 'File: ', '$'
        datetime_str db 'Created: ', '$'
        new_line db 13, 10, '$'
        space db ' $'
        minus db  '-'

.code
        include macro.inc
        include file_proc.inc
        include matrix_proc.inc
        
start:
        init_data

        call OpenFileIN
        jnc file_opened
        jmp exit

file_opened:
        call ReadFileToBuffer
        call CloseFileIN
        call ParseMatrix

        print_str matrix_str
        call print_matrix

        call CreateFileOUT
        call WriteOutputFile
        call CloseFileOUT

        call PrintResult

exit:
        close_program
        
end start
