Title: Notes on data visualization and graphics in Python
Date: 2016-08-18
Category: blog
Author: Hana Lee
Tags: chipy, data science, python
Summary: Or, where is my `ggplot2`?!

Yesterday, I gave a talk at ChiPy's Scientific SIG meeting, providing an
overview of the data visualization packages in Python, from the perspective of
a former scientist who switched from using R to Python for large-scale data
analysis. My talk was framed around the current limitations in Python's data
visualization packages and what improvements I would like to see. Here is a written, and considerably more polished, version of what I spoke
about.

### What we talk about when we talk about data visualization

It's hard to talk about "Big Data" because it is
complicated. What does that mean? There are many variables, both continuous and
discrete, exhibiting patterns and trends that cannot be easily modeled
linearly and frequently riddled with a lot of noise. The data does not yield
easy takeaways that can be summarized in a single phrase. Thus, it becomes
more important than ever that we have tools to not only analyze our data
correctly but also to communicate our findings to others.

That's the importance of data visualization. Edward Tufte, who is one of the
pioneers in this field, sums up the criteria for an
effective graphic in this quote from his classic, _Visual Display of
Quantitative Information_: 

> Graphical excellence is that which gives to the viewer the greatest number of
> ideas in the shortest time with the least ink in the smallest space.

It's important that we convey the overall message as well as key details in a
format that is clear, simple, and easy to interpret.

We can start to develop some guidelines for creating such "excellent" data
graphics by looking at how humans process visual information. How do
we distinguish between different quantities? There's a maxim that pie charts are
much worse than bar charts for displaying categories with similar amounts
because our eye is better able to notice small differences in length than area
or angle. Another question to ask is how we notice relationships among
individual data points. Graphical elements that are located close
together or share similar properties, like color or shape, or even directly
creating connections or boundaries help the viewer
draw connections between data components.

Broader considerations include thinking about directing the viewer's attention:
where does their eye fall and are there indicators that show where to look next?
Possibly most important of all, every data graphic has a story to tell, and
the success of any data visualization depends on having a coherent narrative. "A picture is worth a thousand words," but we need to know
what those words are in the first place.

### ggplot2 and a grammar of graphics

Another pioneer in the field, Leland Wilkinson, tried to
systematize how we go about creating data
visualizations through what he called a "grammar of graphics".It breaks
down the components of a plot into the following abstract elements:

* Aesthetics, which visually represent data variables
* Geometric objects, which depict data points
* Scales and coordinates, which communicate information about quantities
* Statistics, which are transformations applied to the data to illustrate analysis
* Facets, which are how multiple related plots can be tied together in a graphic
* Annotations, which are text labels applied to a plot

These elements form the foundation for the R library, `ggplot2`,
which has set a high standard for data visualization packages and is
widely used in the R community. Its particular strengths are a clear and
consistent syntax, based on the grammar of graphics; a layering system,
which allows you to quickly add new elements to a plot; and a faceting system,
which makes it easy to generate data graphics with multiple related plots, when
dealing with complicated data.

Of particular note is how simple it is to apply statistical functions, like
calculating the mean and standard error to summarize a lot of data points, and
useful, attractive plotting methods, like `geom_smooth()`, which automatically
applies a smoothing loess function to your data and draws a line on top of a
translucent ribbon that represents the 95% confidence interval.

It also makes it easy to go from a single plot to multiple plots split across
an additional variable. In my code examples, I show how I go from a single plot
depicting mean car mileages measured during city and highway driving over time to multiple plots depicting how this
relationship changes with engine displacement.[^1] The final version 
illustrates the trend among four different variables (miles per gallon, year,
type of mileage measured, and engine displacement), in an uncluttered
two-dimensional graphic that is easy to interpret.  

So if this R library is so awesome, why would we ever want to use Python
instead? Well, Python has quite a few advantages over R for data science,
particularly when we are dealing with large amounts of data. It is overall
faster and more efficient than R, and because it is a general purpose
programming language, it is easier to integrate into applications that
may want to use the results of your data analysis. It has highly readable
syntax and testing frameworks that make it easier to write robust code. In an
industry setting, Python is much better suited to deploying and releasing
data-based products, which is why it is more widely used.

### What's available in Python

When it comes to data visualization packages for Python, options:
`matplotlib`, `seaborn` and `ggplot`. All of these fall short of R's
`ggplot2` and have certain limitations that stop them from being useful for
generating excellent data graphics. I'll start with `matplotlib`, which
is probably the most widely used library.

`matplotlib` is a port of the Matlab library. I often joke that I haven't met
a single person who enjoys coding in Matlab. Unfortunately, that also applies
to `matplotlib`. A lot of people coming to Python are already familiar
with this library from Matlab, and it does have powerful methods for
rendering 3D or interactive plots. But `matplotlib` has several pitfalls.
Its syntax does not take any advantage of Python's clarity and is difficult to
read. Without customization, it generates some truly ugly plots...and it
doesn't make that customization easy to do either. (The plots shown in the
slides are actually much better than what the default `matplotlib` style
looks like, because Jupyter notebooks automatically apply a style that is meant
to resemble the default theme for `ggplot2`.) It's certainly possible to
"prettify" `matplotlib` if you dig down into its functions to control the
appearance of your plots, but it doesn't make it easy.  Finally, `matplotlib`
doesn't have any functions that actually deal with subsetting or
transforming your data. For example, you have to manually write code to
filter your data by categories if you want to show data points in multiple
colors on a single plot. The lack of such higher-level functions make
using `matplotlib` unsatisfactory for data visualization despite all its
power as a graphics package.  

`seaborn` is a wrapper for `matplotlib` that simplifies its syntax and
generates much more attractive looking graphs. It also has some data handling
functions similar to `ggplot2` that facilitate the process of making more
complex plots. However, there are some obvious gaps in its functionality,
which seems to be reflected in how it also seems to have incomplete
documentation. In particular, what I've noticed is that it has a limited range
of plot types, each of which is fairly inflexible in how it will handle data.
In my code examples, I show how the `stripplot()` and `factorplot()`
functions treat the variable for year as discrete rather than continuous
data, which means that labels along the x-axis end up unreadable as
every value for year is treated as a separate category. There's also no
support for more specialized plots, like contour plots. The methods available
for customizing text labels and annotations are limited and have inconsistent
syntax from plot type to plot type. In some cases, it requires drilling
down into the underlying `matplotlib` code to get the effect you want. So while
there are many promising aspects to `seaborn`, it seems that it needs further
development to be truly mature as a data visualization tool.

The last option, which may be the least known or used out of the three, is
`ggplot`, a Python port of `ggplot2` that is being developed by &Ycirc;hat. Now
at first, this package sounds like the answer we've been wanting: a way to
use `ggplot2`'s powerful approach to data visualization in a Python environment.
However, it is also an incomplete package still under development, which
becomes clear when you look at its
[documentation](http://ggplot.yhathq.com/docs/index.html), where many pages
are completely empty. What's great is that it emulates `ggplot2`'s syntax,
breaking down a plot into abstract elements that helps you think about how to
visually represent your data in an effective way. What's not so great is that
it's missing a lot of key functions for statistical transformations and
plot types. In the code examples, when I attempt to use the `geom_jitter()`
method to prevent overplotting, there is no actual jittering on the points. The
implementation of `geom_smooth()` also seems to have bugs in how it calculates
the 95% confidence interval and how it applies loess smoothing to the
data. And faceting just creates a visually unappealing, proportionally
unbalanced set of plots. In short, there needs to be more development of this package
in order for it to be fully usable.

### Where do we go from here?

When compared to the kind of data graphics we can produce in R with `ggplot2`,
the status quo in Python is far from satisfactory...but we don't have to be demoralized.
I think we can look at the situation as an opportunity: to create a Python
data visualization package that can rival `ggplot2` in its power and ease of
use. [`matplotlib`](https://github.com/matplotlib/matplotlib),
[`seaborn`](https://github.com/mwaskom/seaborn) and
[`ggplot`](https://github.com/yhat/ggplot) are all open-source projects to
which Python programmers and data scientists can contribute. Or perhaps the
Python community can build a new package from the ground up that has
`ggplot2`'s functionality.

I would like to see a data visualization tool that implements what is
key to `ggplot2`'s success in the R community. People tend to try to imitate
the look and style of `ggplot2` graphics and stop there. But the core innovation of
`ggplot2` is how it utilizes the "grammar of graphic" concepts to
organize how we construct plots. There's no reason that we can't create that
in Python.

In the meantime, we also have the option of using R and Python together,
which is particularly easy to do in a Jupyter notebook environment with
the `rpy2` package. (Or if you want to run Python from R, there is the
`rPython` library on CRAN.)

As a footnote, while I've focused on static data graphics here, there are
also tools available for constructing interactive plots in both languages,
`ggvis` for R and `bokeh` for Python, which I encourage people to check out
as well. 
 
For code examples and pretty plots, please look at my [Jupyter
notebook](https://github.com/hnlee/talks/blob/master/pyviz/pyviz.ipynb) or my
[slides](http://hnlee.github.io/talks/pyviz/).

[^1]: The data for all the plots shown in my slides comes from an
open-source data set provided by
the [EPA](http://fueleconomy.gov), processed and made available as an R
package, [`fueleconomy`](https://github.com/hadley/fueleconomy).
