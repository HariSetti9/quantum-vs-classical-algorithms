# Quantum Algorithms versus Classical Algorithms

IEEE-style conference manuscript, first full draft. Authors: SETTI APPALANAIDU and Mohitrajsinh Jadeja, Department of CSE (AI & ML), Marwadi University, Rajkot, Gujarat, India. Corresponding author: SETTI APPALANAIDU (setti.139984@marwadiuniversity.ac.in).

## Contents
- main.tex: complete editable manuscript with 20 numbered bibliography entries. References are embedded using thebibliography; BibTeX is not required.
- IEEEtran.cls: unmodified IEEEtran V1.8b class, including its license notices.
- query_scaling.pdf and success_probability.pdf: vector figures.
- reproduce.py: deterministic NumPy state-vector study and figure generation.
- grover_results.csv: all 13 simulated sizes, probabilities, and sensitivity values.
- environment.json and requirements.txt: generation environment and numerical dependencies.
- reference_links.csv: references and verification links for author review.

## Compile in Overleaf
Create a New Project -> Upload Project, upload this ZIP, select main.tex as the main document, and use pdfLaTeX. Compile twice so citations and cross-references resolve. The included figures allow compilation without running Python.

## Compile locally
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex

## Reproduce the numerical study
Install the versions in requirements.txt, then run:
python3 reproduce.py
This regenerates both plots, grover_results.csv, and environment.json in the script directory. Maximum probability disagreement in the supplied run is approximately 1.78e-14. Checks reject errors above 1e-10. No random seed is required because no random sampling is used.

## Interpretation
The Python program runs on a classical computer. It represents an ideal Grover state, not a gate-level or noisy hardware simulation. Query counts are not execution-time measurements. The sensitivity model is an illustrative assumed-cost calculation, not a fitted hardware prediction. Verification and failed attempts are explicitly accounted for in that model. No new algorithm, complexity separation, or physical quantum advantage is established.

## Before external submission
This is a focused narrative review and educational numerical case study. It is suitable for author/lecturer review; publication acceptance is not assured. The literature set is foundational and deliberately bounded, with cited works through 2021, and does not constitute a current systematic survey. For a competitive external submission, expand recent related work, identify a substantive contribution beyond reproducing a known formula, and request subject-expert review. Do not describe the paper as peer reviewed or IEEE published merely because it uses the template.

Both named authors should read the cited papers, verify every claim and bibliographic record, understand and rerun the code, and approve the manuscript and author order. Setti is designated to handle correspondence; no unverified contribution statement has been invented. Confirm any university submission requirements. Follow the selected venue's current generative-AI disclosure policy: AI assistance was used for literature discovery, drafting, LaTeX preparation, and code generation in this version. Do not claim that author verification or independent experimental work has occurred until the authors have done it.

For arXiv, check the appropriate category, endorsement, moderation, licensing, and TeX-source requirements at https://info.arxiv.org/help/submit/index.html before uploading. arXiv is a moderated preprint repository and does not confer peer review. This package has not been submitted anywhere. If a target venue requires anonymous review, remove author details only for that anonymous version.

IEEEtran.cls source: https://raw.githubusercontent.com/cslaviero/ieee_paper_markdown_pandoc/master/IEEEtran.cls (V1.8b, 2015/08/26); its embedded license is retained.
