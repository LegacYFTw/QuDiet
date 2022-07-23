# rev_tof_1 for two 3 qudit registers
# developed by Amit Saha
.qudit 3 


qudit x0 (2)
qudit x1 (3)
qudit x2 (2)


.begin
X x0
CX x0 x1
CX x1 x2
CX x0 x1
.end
