
HW1	START   1000
FIRST	LDA     TWO
	MUL     TWO
	MUL     TWO                 .2*2*2
	STA     ALPHA
	LDA     FTHREE
	MUL     FTHREE              .(-3)*(-3)            
	STA     BETA
	LDA     ALPHA
	SUB     BETA                 .A-B
.
GO	MUL     FONE   
	COMP    ZERO
	JLT     GO                   .較小就*(-1)
	STA     C
	.                                     交換A,B
	LDA     ALPHA              
	STA     TEMP                 .把ALPHA存入TEMP
	LDA     BETA 
	STA     ALPHA                .把BETA存入ALPHA
	LDA     TEMP
	STA     BETA                 .把TEMP(原ALPHA)存入BETA
	.         
	LDA     ALPHA
	SUB     BETA
	STA     D                    D=A-B
	.	
	LDA     C                    
	SUB     D
WEE	MUL     FONE   
	COMP    ZERO
	JLT     WEE                  .絕對值
	STA     C
	.        
	DIV     TWO                  .得到商
	MUL     TWO
	STA     MATH
	LDA     C                    .C-D減求出來的MATH
	SUB     MATH                 .終於求得餘數
	.         
	COMP    ZERO
	JEQ     EVN                  .偶數
	LDA     G0                   .奇數
	J       JUMP
EVN	LDA     G1                   .印EVN  
JUMP	STA     G
.
TWO	WORD    2
ALPHA	RESW    1
BETA	RESW    1
C	RESW    1
D	RESW    1
MATH	RESW    1
TEMP	RESW    1
FONE	WORD    -1                  
FTHREE	WORD    -3                  
ZERO	WORD    0
G	RESB    3
G0	BYTE    C'ODD'
G1	BYTE    C'EVN'
