# Making a nice looking article

## Why should I read this?

For better or worse, the quality of your figures correlates with the perceived quality of your work.
Just like the grammatical correctness of your writing, one might wonder if someone is sufficiently careful with their scientific work if they aren't very careful with their figures and their presentation.
I am putting some "rules" below for how to format your documents and figures.

## Consistency

One should keep styles consistent within a manuscript.
You might be forgiven for even obviously poor style choices if you are consistent with them throughout.

### Colors

I like to use the following color palette, in your TeX preamble as:
```tex
\usepackage{xcolor}
\definecolor{lightblue}{rgb}{0.63, 0.74, 0.78}
\definecolor{seagreen}{rgb}{0.18, 0.42, 0.41}
\definecolor{orange}{rgb}{0.85, 0.55, 0.13}
\definecolor{silver}{rgb}{0.69, 0.67, 0.66}
\definecolor{rust}{rgb}{0.72, 0.26, 0.06}
\definecolor{purp}{RGB}{68, 14, 156}
\definecolor{joshua}{RGB}{251,220,127}

\colorlet{lightsilver}{silver!30!white}
\colorlet{darkorange}{orange!75!black}
\colorlet{darksilver}{silver!65!black}
\colorlet{darklightblue}{lightblue!70!black}
\colorlet{darkrust}{rust!85!black}
\colorlet{darkseagreen}{seagreen!85!black}
```
In particular, I use `darkrust` and `seagreen` quite a bit, as I find them complementary and easy on the eyes.

Setup your hyperrefs this way, so that have attractive notation of your crossrefs in your document:
```tex
\usepackage[colorlinks=true,linkcolor=darkrust,citecolor=darklightblue,urlcolor=darksilver]{hyperref}
```

To keep things consistent, I recommend using the `cleveref` package
```tex
\usepackage{cleveref}
```
which is invoked for figures, tables, and sections via the commands `\Cref{}` and `\cref{}`, using the former if the reference is at the beginning of a sentence.


## Figures

### Consistency 

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

### Vector graphics

An exception to the above is if the figure does not contain any text or equations.
Doing so leads to inconsistent font sizes between the document and the software that generated the figure. 

**Rule:** Use vector graphs, preferably PDF, for all plots that involve text or equations.

### How to actually make your figures

TikZ and PGFplots are TeX packages that provide a natural way to achieve this consistency.
There is a somewhat steep learning curve, though compared to their competitors I think the trade-off is worth well worth it. 
The TeX stack exchange website regularly answers questions about these packages. 
A web search of most any basic TikZ/PGF question will quickly flag an answer.

