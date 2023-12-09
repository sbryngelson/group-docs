## Making figures

See [here](../templates/paper/figures) for examples.

### What tool to use to make figures?

TikZ and PGFplots are TeX packages that provide a natural way to achieve this consistency.
There is a steep learning curve, though the trade-off is worth it compared to their competitors. 
The TeX stack exchange website regularly answers questions about these packages. 
A web search of almost any basic TikZ/PGF question will quickly flag an answer.
I can provide example `.tex` files for many things (like [here](../templates/paper/figures)), and you can gather examples from your colleagues as well as online (like [here](https://github.com/comp-physics/tikz-examples) and [here](https://github.com/comp-physics/TikZ-examples-2)).

**Rule 1:** Use a tool and workflow that allows you to remake a figure very quickly (e.g., change a line of text in a program and recompile) 

**Rule 2:** Use a tool that allows you to use LaTeX fonts for text and equations.

### What if you have flow visualizations?

Images of complex simulations _require careful attention_!
In some cases one will need to annotate them with axes labels, tick marks and labels, legends, and so on.
All of this text/equations should __not be rasterized__; if it is rasterized, I will send it back to you to fix.

__Paraview:__
I believe Paraview has some functionality for this. Here is [a reference](https://www.paraview.org/Wiki/ParaView/Vector_Graphics_Export) and here is [another](https://scicomp.stackexchange.com/questions/36122/vector-format-export-for-screenshots) and [another](https://www.paraview.org/pipermail/paraview/2017-April/039969.html).
Perhaps it exports a separate vector image for the text and/or legends?
I am not entirely sure how it works.
I welcome recommendations on how to best do this, but I do know it is possible.

Other rules:
* __Background color:__ Do not use background colors in your visualizations, e.g., the dark blue used in Paraview.
Instead, use a white background! So it blends into the document nicely.
* __File size:__ Do not use images that are very large. Images bigger than roughly 10MB are too large.


### How to label sub-figures

Label your sub-figures using font face and size consistent with the figure caption font face and size.
Place your sub-figure labels (e.g., (a) and (b)) in a place that is not too obtrusive.

* If you do not need sub-captions, you can place in the labels in the top left or bottom left of each sub-figure.
* If you need sub-captions, then you should put the sub-figure labels below the center of the figure.

Do not put the sub-figure captions directly below the sub-figures if you have no "real" caption (e.g., you are just labeling them (a) or (b), etc.); in this case, instead put them in one of the corners per above.
See the examples [here](../templates/paper/figures) for reference.

### Title

Your figures should not have titles.

### Color bars

If your data involves a color bar, use one that makes sense for the data you are plotting.
You can read more about this online, like [here](https://chartio.com/learn/charts/how-to-choose-colors-data-visualization/) or [here](https://academy.datawrapper.de/article/140-what-to-consider-when-choosing-colors-for-data-visualization).
Common guidelines are 
* Don't use the rainbow/jet color scheme (read more about the problem with this [here](https://stats.stackexchange.com/questions/223315/why-use-colormap-viridis-over-jet))
* Don't use a tri-color scheme (e.g., Paraview's default blue-white-red) for data that is not centered at a unique/special value like 0
  * A violation would be using such a color scheme for data that varies from 0 to 1
* Using a monochromatic color scheme (e.g., from white to black) for data that vary uniformly as above, say from 0 to 1.
* Use a tri-color scheme that centers the color at black or white, e.g., the Paraview default red-white-blue for data that are nominally centered at a special or reference value, like 0 or 1.

### Information quantity

Your figures should only consist of the information required to tell the story or show the results that you want to show.

Examples of having too much information are, well, numerous. Some examples:
* You have too many tick marks
* You include too many lines of data on your plot.

To be quite specific: If you have two simulation results that are very close to each other, you may or may not want to show both on your figure.
You should show both if your intention _is to show_ that they are close together.
If your message is the result, then you can just show one simulation result and mention in the caption that the results for the other case look the same.

Essentially, you want to show the reader as close to a 'cartoon' of your work as possible.
Showing frivolous information distracts from your message.

### Consistency 

Figures should also be consistent between each other and the surrounding text. 
If you use a solid black line to denote the "exact solution" in one figure, do not switch to a dashed red line for a different exact solution in a later figure. 
The fonts used in the figures should match the face and size of the surrounding text. 
LaTeX uses Computer Modern and Latin Modern font faces and 11pt sizes by default, though journal templates and class files may change this. 

The font size of the captions below your figures should be one step smaller than that of your document (so 10pt if the document is nominally 11pt).
The tick labels and axis labels should also be smaller than the nominal font size of your document; 9pt is usual here, and it should be consistently this size in your whole document.

**Rule:** Do _not_ scale your figures via the command
```tex
\includegraphics[width=0.3\textwidth]{figure.pdf}
```
Doing so leads to inconsistent font sizes between the document and the software that generated the figure. 
__An exception__ to the above is if the figure contains no text or equations, like a simulation visualization.

**Rule:** Use vector graphic formats (PDF, please) for all plots that involve text or equations.

**Rule:** Use the same color palette for all of your figures (not including flow visualizations) and your main text (see [formatting](formatting.md)]).

### Useful references

* [Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)
