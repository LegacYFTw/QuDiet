from qudiet.circuit_library.standard_gates.cx import CXGate
from qudiet.circuit_library.standard_gates.h import HGate
from qudiet.circuit_library.standard_gates.i import IGate
from qudiet.circuit_library.standard_gates.measurement import Measurement
from qudiet.circuit_library.standard_gates.x import XGate
from qudiet.circuit_library.standard_gates.z import ZGate
from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate
from qudiet.circuit_library import ArbitaryGate
from qudiet.circuit_library.standard_gates.toffoli_utility import Toffoli

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import math as m

def _draw_cgate(name,crtl,trgt,plus,dim,i,ax,dpi):

        s=dpi/6
        x= i
        txt=r"$"+name+"^{+"+str(plus)+"}_{"+str(dim)+"}$"
        t=ax.text(x,trgt+1,txt,size=s,
            bbox=dict(boxstyle="square",
                    facecolor='white'
                    )
            )
    
    
        width=t.get_window_extent()
        width=width.get_points()[1][0]-width.get_points()[0][0]
        width=width/dpi
        left=width/2
    
        mn=min(crtl)
        mx=max(crtl)
        if trgt<mn:
            mn=trgt
        if trgt>mx:
            mx=trgt
        
        y1 = [y+1 for y in range(mn,mx+1)]
        x1 = [x+left for i in range(len(y1))]
        marker = [False for i in range(len(y1))]
        for i in range(len(y1)):
            if y1[i]-1 in crtl:
                marker[i]=True
        
        ax.plot(x1, y1, marker = 'o',markevery=marker,color='black')
    
        return width
        
def _draw_qubit_cnot_gate(crtl,trgt,i,ax,dpi):
    s=dpi/6

    x=i

    x1=[x,x]
    y1=[crtl+1,trgt+1]
    marker=[True,False]
    ax.plot(x1, y1, marker = 'o',markevery=marker,color='black')
    ax.plot(x1[1], y1[1], marker = 'o',markevery=[True],color='none',markeredgecolor='black',markersize=s)
    ax.plot(x1[1], y1[1], marker = '+',markevery=[True],color='black',markersize=s)

    return s/dpi
    
def _draw_single_qudit_gate(*args):
    dpi=args[len(args)-1]
    ax=args[len(args)-2]
    x= args[len(args)-3]
    s=dpi/6
    if len(args) == 7:
        name=args[0]
        trgt=args[1]
        plus=args[2]
        dim=args[3]
        txt=r"$"+name+"^{+"+str(plus)+"}_{"+str(dim)+"}$"

    elif len(args) == 5:
    
        name=args[0]
        trgt=args[1]
        txt=r"$"+name+"$"
    
    
    t=ax.text(x,trgt+1, txt ,size=s,
        bbox=dict(boxstyle="square",
                facecolor='white'
                )
        )
    width=t.get_window_extent()
    width=width.get_points()[1][0]-width.get_points()[0][0]
    width=width/dpi
    return width
    
def _draw_custom_gate(name,trgt,x,ax,dpi):
    s=dpi/6

    txt=r"$"+name+"$"

    ymax=max(trgt)
    ymin=min(trgt)
    
    rec=patches.Rectangle((x,ymin+1-0.1),1,ymax-ymin+0.2,facecolor='white',edgecolor='black',zorder=2)
    ax.add_patch(rec)
    ax.annotate("G",(x+0.5,(ymin+ymax+2)/2),ha='center', va='center',fontsize=s)

    mark=[]
    x1=[]
    y1=[]
    for i in range(len(trgt)):
        y1.append(trgt[i]+1)
        x1.append(x)
        mark.append(True)
    ax.plot(x1,y1,linewidth=0,markevery=mark,marker=9,markersize=s/2,color='black')
    return 1
    
def _draw_qudit(n,k,ax):
    y=1
    fig = ax.figure
    size = fig.get_size_inches()
    x1, y1 = [k, size[0]-1], [y, y]
    for i in range(n):
        ax.plot(x1, y1, marker = 'o',markevery=[False,False],color='black')
        y+=1
        x1, y1 = [k, size[0]-1], [y, y]
def _draw_states(st,dims,x,ax,dpi):
    s=dpi/6
    width=[0]

    t=ax.text(0.1,0.1, "MSB" ,size=s,
            bbox=dict(boxstyle="square",
                    facecolor='None',
                    pad=0,
                    edgecolor='None'
                    )
            )

    w=t.get_window_extent()
    w=w.get_points()[1][0]-w.get_points()[0][0]
    w=w/dpi
    width.append(w)

    for i in range(len(st)):
        txt=r"$Q^{"+str(dims[i])+"D}_{"+str(i)+"}|"+str(st[i])+">$"
        t=ax.text(x,0.9+i, txt ,size=s,
            bbox=dict(boxstyle="square",
                    facecolor='None',
                    pad=0,
                    edgecolor='None'
                    )
            )

        w=t.get_window_extent()
        w=w.get_points()[1][0]-w.get_points()[0][0]
        w=w/dpi
        width.append(w)


    t=ax.text(0.1,len(st)+0.6, "LSB" ,size=s,
            bbox=dict(boxstyle="square",
                    facecolor='None',
                    pad=0,
                    edgecolor='None'
                    )
            )

    w=t.get_window_extent()
    w=w.get_points()[1][0]-w.get_points()[0][0]
    w=w/dpi
    width.append(w)

    return max(width)
def _draw_toffoli_gate(gate_,i,ax,dpi):
    crtl_,trgt=gate_.acting_on
    crtl=list(crtl_)
    plus=gate_._plus
    dim=gate_.dims[trgt]
    return _draw_cgate('X',crtl,trgt,plus,dim,i,ax,dpi)

def _draw_cnot_gate(gate,i,ax,dpi):
    crtl,trgt=gate.acting_on
    crtl=[crtl]
    plus=gate._plus
    dim=gate._qreg[trgt]
    if gate._qreg[crtl[0]]==2 and gate._qreg[trgt]==2:
        return _draw_qubit_cnot_gate(crtl[0],trgt,i,ax,dpi)
    return _draw_cgate('X',crtl,trgt,plus,dim,i,ax,dpi)
def _draw_x_gate(gate_,i,ax,dpi):
    trgt,plus,dim=gate_.acting_on,gate_.plus,gate_.dims
    return _draw_single_qudit_gate("X",trgt,plus,dim,i,ax,dpi)
       
def _draw_h_gate(gate_,i,ax,dpi):
    trgt=gate_.acting_on
    return _draw_single_qudit_gate('H',trgt,i,ax,dpi)
def _draw_z_gate(gate_,i,ax,dpi):
    trgt=gate_.acting_on
    return _draw_single_qudit_gate("Z",trgt,i,ax,dpi)
def _draw_arbitary_gate(gate_,i,ax,dpi):
    trgt=gate_.acting_on
    if isinstance(trgt,int):
        return _draw_single_qudit_gate("G",trgt,i,ax,dpi)
    elif len(trgt)==1:
        return _draw_single_qudit_gate("G",trgt[0],i,ax,dpi)
    else:
        trgt=list(trgt)
        return _draw_custom_gate("G",trgt,i,ax,dpi)
def _draw_measure_gate(gate_,i,ax,dpi):
    trgt=gate_.acting_on
    return _draw_single_qudit_gate("M",trgt,i,ax,dpi)

def _draw_layer(gates,i,ax,dpi):
    width=[0]

    for gate in gates:
        if isinstance(gate,XGate):
            width.append(_draw_x_gate(gate,i,ax,dpi))
        elif isinstance(gate,HGate):
            width.append(_draw_h_gate(gate,i,ax,dpi))
        elif isinstance(gate,ZGate):
            width.append(_draw_z_gate(gate,i,ax,dpi))
        elif isinstance(gate,CXGate):
            width.append(_draw_cnot_gate(gate,i,ax,dpi))
        elif isinstance(gate,Toffoli):
            width.append(_draw_toffoli_gate(gate,i,ax,dpi))
        elif isinstance(gate,ArbitaryGate):
            width.append(_draw_arbitary_gate(gate,i,ax,dpi))
        elif isinstance(gate,Measurement):
            width.append(_draw_measure_gate(gate,i,ax,dpi))
    
    return max(width) 

def draw_circuit_mpl(cir,compress=1):

    bit=len(cir.qregs)
    
    moments=cir.op_flow.peek()
    moment=moments[1]
    gates=moment.peek_list()
    
    fig=1
    dpi=plt.rcParams['figure.dpi']
    x=15+bit*compress
    y=bit+1
    
    f,ax=plt.subplots(figsize=(x, y))
    ax.set_xlim(xmax=x)
    ax.set_ylim(ymax=y)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_title("Fig:- "+str(fig),loc='left',fontdict=dict(fontsize=dpi/6))
    
    fig+=1
    l0=moments[0].peek_list()
    sts=[]
    dims=[]
    for st in l0:
        sts.append(st.state)
        dims.append(st.dim)

    width=_draw_states(sts,dims,0.5,ax,dpi)
    _draw_qudit(bit,m.ceil(width+1),ax)

    i=m.ceil(width+1)
    gap=1

    for moment in moments:
        gates=moment.peek_list()
        width=_draw_layer(gates,i,ax,dpi)
        i=(i+width+gap)
        if m.ceil(i) >= x-1:
            f,ax=plt.subplots(figsize=(x, y))
            ax.set_xlim(xmax=x)
            ax.set_ylim(ymax=y)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.set_title("Fig:- "+str(fig),loc='left',fontdict=dict(fontsize=dpi/6))
            fig+=1
            _draw_qudit(bit,1,ax)
            i=2

    plt.show()
    plt.close()