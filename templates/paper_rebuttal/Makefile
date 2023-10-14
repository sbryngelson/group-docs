# execute this makefile via `$ make`, 
# it will create a diff between your original and revised paper,
# named main.tex and main_rev.tex, respectively. also compmiles 
# your response with filename response.tex

# put the name of your main .tex file
paper = main
# put the name of your revised file
rev_paper = main_rev

# the name of your response.tex file
response = response

# the name of your bibliography file
ref = ref

all: $(paper).pdf $(rev_paper).pdf $(response).pdf diff.pdf

$(paper).pdf: $(paper).bbl $(paper).tex 
	pdflatex $(paper)
	pdflatex $(paper)

$(response).pdf: $(response).tex
	pdflatex $(response)

$(paper).bbl: $(ref).bib
	pdflatex $(paper) 
	bibtex $(paper)

$(rev_paper).pdf: $(rev_paper).bbl $(rev_paper).tex 
	pdflatex $(rev_paper)
	pdflatex $(rev_paper)

$(rev_paper).bbl: $(ref).bib
	pdflatex $(rev_paper) 
	bibtex $(rev_paper)

diff.pdf: $(rev_paper).tex 
	latexdiff $(paper).tex $(rev_paper).tex > diff.tex
	pdflatex diff
	bibtex diff
	pdflatex diff
	pdflatex diff

clean:
	rm -f *converted*pdf external*/*converted*pdf *.bbl *.log *.dvi *.blg *~  *.aux *Notes.bib *.gz

realclean: clean
	rm -f $(paper).pdf $(rev_paper).pdf diff.pdf diff.tex
