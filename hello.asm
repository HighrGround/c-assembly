section .data

msg: dq "hello world\n"
len: $ - msg



section .text 
	global _start;


_start;



movq rax, 0x2000004         ; write system call
movq rdi, 1                  ; file descriptor (stdout)
movq rsi, msg                ; message address
movq rdx, len                ; message length
syscall                      ; invoke kernel

movq rax, 0x2000001         ; exit system call
movq rdi, 0                  ; exit code
syscall                      ; invoke kernel
