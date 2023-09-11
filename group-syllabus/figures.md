# How to make figures

See [here](../templates/figures) for examples.

## What tool to use to make figures?

TikZ and PGFplots are TeX packages that provide a natural way to achieve this consistency.
There is a somewhat steep learning curve, though compared to their competitors I think the trade-off is worth well worth it. 
The TeX stack exchange website regularly answers questions about these packages. 
A web search of most any basic TikZ/PGF question will quickly flag an answer.
I can provide example `.tex` files for many things, and you can gather examples from your colleagues as well.

**Rule 1:** Use a tool and workflow that allows you to remake a figure very quickly (e.g., change a line of text in a program and recompile) 

**Rule 2:** Use a tool that allows you to use LaTeX fonts for text and equations.

## Consistency 

Figures should also be consistent, both between each other and with the surrounding text. 
If you use a solid black line to denote the "exact solution" in one figure, do not switch to a dashed red line for a different exact solution in a later figure. 
The fonts used in the figures should match the face and size of the surrounding text. 
Latex uses Computer Modern and Latin Modern font faces and 11pt sizes by default, though journal templates and class files may change this. 

The font size of the captions below your figures should be one step smaller than that of your document (so 10pt if the document is nominally 11pt).
The tick labels and axis labels should also be smaller than the nominal font size of your document, perhaps 9pt is usual here, and it should be consistently this size in your whole document.

**Rule:** Do _not_ scale your figures via the command
```tex
\includegraphics[width=0.3\textwidth]{figure.pdf}
```

**Rule:** Use the same color palette for all of your figures and your main text (see [formatting](formatting.md]).

## Vector graphics

An exception to the above is if the figure does not contain any text or equations.
Doing so leads to inconsistent font sizes between the document and the software that generated the figure. 

**Rule:** Use vector graphic formats (PDF, please) for all plots that involve text or equations.
