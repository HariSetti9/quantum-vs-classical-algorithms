from pathlib import Path
import math, csv, json, platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
ROOT.mkdir(parents=True,exist_ok=True)
rows=[]
for n in range(4,17):
    N=2**n
    theta=math.asin(1/math.sqrt(N))
    k=math.floor(math.pi/(4*theta))
    state=np.full(N,1/math.sqrt(N),dtype=np.float64)
    for _ in range(k):
        state[0]*=-1
        state=2*state.mean()-state
    p=float(state[0]**2)
    exact=math.sin((2*k+1)*theta)**2
    assert abs(p-exact)<1e-10
    assert abs(float(state@state)-1)<1e-10
    c=(N+1)/2
    rows.append(dict(n=n,N=N,iterations=k,success_probability=p,analytic_probability=exact,absolute_error=abs(p-exact),classical_expected_checks=c,query_ratio=c/k,expected_verified_quantum_queries=(k+1)/p,break_even_r=c*p/(k+1)))
with (ROOT/'grover_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
plt.rcParams.update({'font.family':'serif','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(3.45,2.25),layout='constrained')
ax.plot([r['N'] for r in rows],[r['classical_expected_checks'] for r in rows],'-o',ms=3,color='#111111',label='Classical expected checks')
ax.plot([r['N'] for r in rows],[r['iterations'] for r in rows],'-s',ms=3,color='#245b91',label='Grover iterations')
ax.set(xscale='log',yscale='log',xlabel='Search-space size N',ylabel='Ideal query count')
ax.grid(alpha=.22);ax.legend(frameon=False,fontsize=7,loc='upper left')
fig.savefig(ROOT/'query_scaling.pdf');plt.close(fig)
N=256;theta=math.asin(1/math.sqrt(N));ks=np.arange(0,41)
state=np.full(N,1/math.sqrt(N));ps=[]
for k in ks:
    ps.append(float(state[0]**2));state[0]*=-1;state=2*state.mean()-state
fig,ax=plt.subplots(figsize=(3.45,2.35),layout='constrained')
ax.plot(ks,np.sin((2*ks+1)*theta)**2,color='#111111',lw=1,label='Analytical probability')
ax.scatter(ks[::2],np.array(ps)[::2],s=13,facecolors='none',edgecolors='#245b91',label='State-vector simulation')
ax.set(xlabel='Grover iterations k',ylabel='Success probability',ylim=(-.03,1.05))
ax.grid(alpha=.22);ax.legend(frameon=False,fontsize=7,loc='lower center',bbox_to_anchor=(0.5,1.02))
fig.savefig(ROOT/'success_probability.pdf');plt.close(fig)
(ROOT/'environment.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__,'max_probability_error':max(r['absolute_error'] for r in rows),'scope':'Ideal real-valued state-vector simulation; not quantum hardware or a runtime benchmark.'},indent=2))
print(json.dumps(rows[::4],indent=2))
