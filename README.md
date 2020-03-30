SP_project
The project is a simulation to the assembler of the SIC hypothetical machine.
Students should implement both Pass1 and Pass2 of the SIC assembler language.
Your assembler should consider all the issues:
1-  Directives: START, END, BYTE, WORD, RESB, RESW, LTORG
2-  Comments: If a source line contains a period (.) in the first byte, the entire line is treated as a comment.
- Addressing modes: Simple, Indirect
- Instruction Set: Specified in Appendix A
- Literals: literals are supported in your source code
- Errors: Your Assembler should designate the errors
You should include test files. Assume a fixed format source code with all text written in uppercase.


 The output of Pass 1 is:
1. Symbol Table SYBTAB: should be displayed on the screen.
2. LOCCTR, PRGLTH, PRGNAME, ...
3. Intermediate file (.mdt): Stored on the secondary storage.
