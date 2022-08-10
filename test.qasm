# rev_tof_1 for two 3 qudit registers
# developed by Amit Saha
.qudit 9


qudit x0 (2)
qudit x1 (2)
qudit x2 (3)
qudit x3 (3)
qudit x4 (2)
qudit x5 (2)
qudit x6 (2)
qudit x7 (2)
qudit x8 (2)


.begin
X x0
X x1
X x3
CX x0 x2
CX x2 x4
CX x0 x2 2
CX x1 x2
CX x2 x5
CX x1 x2 2
CX x0 x3
CX x3 x6
CX x0 x3 2
CX x1 x3
CX x3 x7
CX x1 x3 2
CX x5 x8
CX x6 x8
.end
