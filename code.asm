; Sample code for alarm triggering based on RTC input
CheckAlarm:
MOV AX, 0402; Function to read RTC time
MOV CX, 00; Address of hours in RTC
INT 1AH ; Call interrupt for RTC input
CMP AL, [AlarmHour] ; Compare current hour with set alarm hour JNE SkipAlarm ; Jump if not equal
CMP AH, [AlarmMinute] ; Compare current minute with set alarm minute JNE SkipAlarm ; Jump if not equal
; Alarm time matched, trigger the buzzer
MOV CX, 02 ; Port number for the buzzer
MOV DX, 01 ; Command to activate the buzzer
OUT CX, DX ; Send command to the buzzer port
SkipAlarm:
; Continue with the main loop
