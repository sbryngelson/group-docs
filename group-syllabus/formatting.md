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

Always use consistent formatting.
This might mean more than it seems at first.

Some examples and common errors:
* Choose to either abbreviate journal names (using the __correct__ abbreviation, Google it!) or use the full journal name, then stick with it
    * Like this (full names): 
        * Firouznia, M., Bryngelson, S. H., Saintillan, D. (2023). A spectral boundary integral method for simulating electrohydrodynamic flows in viscous drops. Journal of Computational Physics, 489, 112248.
        * Spratt, J.-S., Rodriguez, M., Schmidmayer, K., Bryngelson, S. H., Yang, J., Franck, C., and Colonius, T. (2021). Characterizing viscoelastic materials via ensemble-based data assimilation of bubble collapse observations. Journal of the Mechanics and Physics of Solids, 152, 104455.
    * Or like this (abbreviations)
        * Firouznia, M., Bryngelson, S. H., Saintillan, D. (2023). A spectral boundary integral method for simulating electrohydrodynamic flows in viscous drops. J. Comp. Phys., 489, 112248.
        * Spratt, J.-S., Rodriguez, M., Schmidmayer, K., Bryngelson, S. H., Yang, J., Franck, C., and Colonius, T. (2021). Characterizing viscoelastic materials via ensemble-based data assimilation of bubble collapse observations. J. Mech. Phys. Solids, 152, 104455.
    * But not like this (mixed)
        * Firouznia, M., Bryngelson, S. H., Saintillan, D. (2023). A spectral boundary integral method for simulating electrohydrodynamic flows in viscous drops. Journal of Computational Physics, 489, 112248.
        * Spratt, J.-S., Rodriguez, M., Schmidmayer, K., Bryngelson, S. H., Yang, J., Franck, C., and Colonius, T. (2021). Characterizing viscoelastic materials via ensemble-based data assimilation of bubble collapse observations. J. Mech. Phys. Solids, 152, 104455.

* In an article title, only capitalize the first letter, proper nouns, abbreviations, and the first letter after a colon
    * Like this: _A Gaussian moment method and its augmentation via LSTM recurrent neural networks for the statistics of cavitating bubble populations_
    * Not like this: _A Gaussian Moment Method and its Augmentation via LSTM Recurrent Neural Networks for the Statistics of Cavitating Bubble Populations_
    * And definitely not like this: _A gaussian moment method and its augmentation via lstm recurrent neural networks for the statistics of cavitating bubble populations_
    * Accomplish this via the `.bib` entry, like this
```tex
  title = {A {G}aussian moment method and its augmentation via {LSTM} recurrent neural networks for the statistics of cavitating bubble populations},
```

* Book titles will usually be capitalized as you enter them verbatim (capitalization and all) in the `.bib` file. So, be consistent when citing book titles!
    * Like this:
        * M. A. Nielsen and I. L. Chuang, _Quantum Computation and Quantum Information_ (Cambridge University Press, 2000)
        * T. Kruger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, and E. Viggen, _The Lattice Boltzmann Method: Principles and Practice_ (Springer International Publishing, 2016)
    * Or like this:
        * M. A. Nielsen and I. L. Chuang, _Quantum computation and quantum information_ (Cambridge University Press, 2000)
        * T. Kruger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, and E. Viggen, _The lattice Boltzmann method: Principles and practice_ (Springer International Publishing, 2016)
    * But not like this:
        * M. A. Nielsen and I. L. Chuang, _Quantum Computation and Quantum Information_ (Cambridge University Press, 2000)
        * T. Kruger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, and E. Viggen, _The lattice Boltzmann method: Principles and practice_ (Springer International Publishing, 2016)

### Referencing your bibliography

Use `natbib` via `\usepackage{natbib}` (it is automatically loaded when one uses the `elsarticle` class).
I recommend the bibliography style file in the template at `templates/paper/model1-num-names.bst`.
This way, you will have access to text and parenthetical citations, which render as:
> One can partially address this problem by working in Fourier space [1] or fitting a parametric model to approximate the eddy diffusivity operator [21, 23]. However, the former requires spatial homogeneity, and the latter’s accuracy depends on the parametric model’s quality. Liu et al. [17] introduces an improved model that uses the nonlocal eddy diffusivity operator's moments to approximate the operator. 
via the code
```tex
One can partially address this problem by working in Fourier space or fitting a parametric model to approximate the eddy diffusivity operator~\citep{hamba04,park21}. 
However, the former requires spatial homogeneity, and the latter's accuracy depends on the parametric model's quality. 
\citet{liu21} introduces an improved model that uses the nonlocal eddy diffusivity operator's moments to approximate the operator.
```
__Note__ the use of `\citep{ref}` and `\citet{ref}` here.
Text `\citet{ref}` instances can be used as nouns but parenthetical references _cannot_.
* This is OK (via `\citet{ref}`):
> So and so [1] did this awesome thing.
* This is not (via `\citep{ref}`):
> [1] did this awesome thing.

Always prevent line-breaks via tides `~` between a parenthetical reference and the text before it.
For example:
* This is correct: `The algorithm is fast, but not as fast as possible~\citep{ref}.`
* This is not: `The algorithm is fast, but not as fast as possible \citep{ref}.`

We generally want our references at the end of sentences unless they are part of a long list.
* Incorrect:
> The LBM method [1] is not as accurate as the finite volume method [2].
* Correct:
> The LBM method is described in So and So [1]. However, is not as accurate as the finite volume method [2].
* And this is also acceptable
> Cavitation is seen in many engineering applications, including submarines [1], pumps [2], and medical devices [3].

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

### References to equations, figures, tables, and sections.

#### Figures, tables, sections

To keep things consistent, I recommend using the `cleveref` package
```tex
\usepackage{cleveref}
```
which is invoked for figures, tables, and sections via the commands `\Cref{}` and `\cref{}`, using the former if the reference is at the beginning of a sentence.
Figures, tables, and sections are always treated as nouns.

#### Equations

First labeling them appropriately as
```tex
\begin{gather}
    Ax=b
    \label{e:lineareqn}
\end{gather}
```
and then reference then via the command `\eqref{e:lineareqn}`.

Treat your equations as nouns and never use the abbreviation "eqn." before it.
* Like this: `The algorithm follows from reducing \eqref{e:someqn} to a first-order system.`
    * Which renders as: 
    > The algorithm follows from reducing (1) to a first-order system.
* Not like this: `The algorithm follows from reducing equation \eqref{e:someqn} to a first-order system.`
* Nor like this: `The algorithm follows from reducing eqn. \eqref{e:someqn} to a first-order system.`
