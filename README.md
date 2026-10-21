# Quantum Algorithms versus Classical Algorithms

Comparative review with a reproducible ideal Grover-search case study.

**Authors:** SETTI APPALANAIDU and Mohitrajsinh Jadeja  
**Affiliation:** Department of CSE (AI & ML), Marwadi University, Rajkot, Gujarat, India  
**Corresponding author:** SETTI APPALANAIDU — setti.139984@marwadiuniversity.ac.in

[Read the IEEE-style paper](paper.pdf) · [LaTeX source](main.tex) · [Simulation code](reproduce.py) · [All numerical results](grover_results.csv) · [Reference links](reference_links.csv)

## What this project shows

The review compares search, integer factorization, linear systems, quantum simulation, and variational optimization using 20 scholarly references. The numerical study reproduces the established Grover success-probability formula for 13 search sizes, from 16 to 65,536 candidates.

This is a review and ideal numerical demonstration. It does not introduce a new algorithm, demonstrate quantum-hardware speedup, or constitute peer-reviewed publication. The simulation executes on a classical computer.

## Reproduce the results

Use Python 3.12 (the supplied run used Python 3.12.14).

```bash
git clone https://github.com/HariSetti9/quantum-vs-classical-algorithms.git
cd quantum-vs-classical-algorithms
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python reproduce.py
```

The script regenerates `grover_results.csv`, `environment.json`, and both figure PDFs. It independently checks state-vector probabilities against the analytical formula and checks normalization with an absolute tolerance of 1e-10. Maximum probability disagreement in the supplied run was approximately 1.78e-14. The calculation is deterministic and does not require a random seed.

## Selected results

| Candidates N | Grover iterations | Ideal success probability | Expected classical checks |
|---:|---:|---:|---:|
| 16 | 3 | 0.961319 | 8.5 |
| 256 | 12 | 0.999947 | 128.5 |
| 4,096 | 50 | 0.999945 | 2,048.5 |
| 65,536 | 201 | 0.999988 | 32,768.5 |

Classical expectations assume a uniformly located single target and a sequential scan without replacement. Quantum iteration counts describe one ideal attempt; verification and failed attempts are discussed separately in the paper. These counts must not be described as a measured 163-times runtime speedup.

For one marked target, theta = asin(1/sqrt(N)) and P(k) = sin²((2k+1)theta). The script implements phase marking followed by inversion about the mean. It does not decompose a circuit into physical gates or model noise.

## Figures

- [Query-count scaling](query_scaling.pdf)
- [Success probability versus iteration count](success_probability.pdf)

## Build the paper

The complete bibliography is embedded in `main.tex`; BibTeX is not required. Use pdfLaTeX with standard LaTeX packages:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

For Overleaf, upload the project files, choose `main.tex`, and use pdfLaTeX. IEEEtran V1.8b is included with its original license notices. IEEE formatting does not imply IEEE publication or endorsement.

## Research provenance and limitations

Foundational theoretical claims belong to the cited researchers. The repository provides an educational synthesis, reproducible numerical confirmation, and an illustrative cost-sensitivity calculation. No runtime, energy, financial-cost, or quantum-device measurements were collected. Literature selection is a focused narrative review with cited works through 2021, not an exhaustive or current systematic survey.

Generative AI assistance was used for literature discovery, manuscript drafting, LaTeX preparation, and simulation-code development. The named authors must independently review and approve the content before academic or external submission. See [author review notes](AUTHOR_REVIEW_NOTES.md).

GitHub provides access to the artifacts and commit history. It does not itself establish novelty, peer review, arXiv acceptance, or independent authorship of every component.
