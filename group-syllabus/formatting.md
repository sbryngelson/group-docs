## Making to format an article or conference paper

### Why should I read this?

For better or worse, the quality of your figures correlates with the perceived quality of your work.
Just like the grammatical correctness of your writing, one might wonder if someone is sufficiently careful with their scientific work if they aren't very careful with their figures and presentation.
I am putting some "rules" below for how to format your documents and figures.

### Consistency

One should keep styles consistent within a manuscript.
You might be forgiven for esoteric style choices if they are employed consistently.

### Math symbols

Always use consistent math symbols.
I usually put all of these in a single file that in invoked in the TeX preamble via
```tex
\input{mathsymbols.tex}
```
and an example such file is in `templates/paper/mathsymbols.tex` in this repository.

Some notation rules you should follow
* Bold lowercase for vectors
* Bold uppercase for matrices and tensors
* Non-bold lowercase for scalars/constants

Common errors
* Dimensionless symbols like the Reynolds number __should not__ be italic, but upright.
    * Like this $\mathrm{Re}$
    * Not like this $Re$
* Super and subscripts that denote text should not be in math/italic symbols, but rather upright normal text. 
    * Like this: $c_{\mathrm{Temp.}}$ or $\mathbf{A}_{\mathrm{Fast}}$
    * This is also OK: $c^{\mathrm{(Temp.)}}$ or $\mathbf{A}^{\mathrm{(Fast)}}$
    * But not like this: $c_{Temp}$ or $\mathbf{A}_{Fast}$
* Do not use asterisks or $\times$ for multiplication
    * Like this: $ab$
    * Never like this: $a\times b$ or $a \ast b$
* Do not use inline math with full fractions that make your text too small to read!
    * Don't do this (inline): $\frac{a}{b}$
    * Do this: $a/b$

### Bibliography

### Colors

I like to use the following color palette in your TeX preamble:
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

Setup your hyperrefs this way so that you have an attractive notation of your crossrefs in your document:
```tex
\usepackage[colorlinks=true,linkcolor=darkrust,citecolor=darklightblue,urlcolor=darksilver]{hyperref}
```

To keep things consistent, I recommend using the `cleveref` package
```tex
\usepackage{cleveref}
```
which is invoked for figures, tables, and sections via the commands `\Cref{}` and `\cref{}`, using the former if the reference is at the beginning of a sentence.


