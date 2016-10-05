Title: Links, the network analysis edition 
Date: 2016-08-08
Category: blog
Tags: 8th light, apprenticeship, linkspam, network analysis 
Author: Hana Lee
Summary: Useful links from the mastery cohort with Bobby Norton. 

One of the many skill development opportunities available at 8th Light is
a "mastery cohort", where an acknowledged "master" with years of experience in
the software industry is invited to come give a day-long workshop for 8th Light
crafters. Last Friday, [Bobby Norton](http://www.bobbynorton.com) came to give a
mastery cohort on data science and network analysis, and apprentices were
invited to participate. I was pretty enthusiastic to sign up because I've done a
lot of dabbling while studying genomics and systems biology; a lot of my
research interests as a scientist revolved around the emergent properties of
complex systems and understanding the behavior of gene regulation and metabolic
networks. I haven't studied graph theory at a rigorous level, other than reading
some papers by Barab&aacute;si and doing a course project on "subgraph" patterns
(incidentally, also the project where I took the opportunity to first teach
myself Python!) way back in second year of graduate school, but the subject
continues to fascinate me.

The Big Idea of the cohort was to apply the ideas from network analysis and
graph theory to software, which is in and of itself a complex system, and to see
if the insights that emerge could be used to identify the characteristics of
well-designed software and (conversely) diagnose problems in code more quickly.
It's one of those ideas that as soon as you hear it, you wonder why it hasn't
been done already! We looked at some tools for representing and visualizing
graphs and networks as well as Bobby Norton's own library written in Clojure for
analyzing dependencies and functions in Clojure codebases.

[vis.js](http://visjs.org/): Javascript-based visualization library that can be
used to draw graphs and network diagrams

[Gephi](https://gephi.org/features/): A visualization GUI tool that is fairly
popular and can be used for exploring network data.

[yEd](https://www.yworks.com/products/yed): Similar to Gephi, with a slicker
interface. Main disadvantage is that there is no support for weighted edges.

[GraphML](http://graphml.graphdrawing.org/index.html): XML-based standard for
representing graph data. File format should be supported by most GUIs.

[Polinode](https://www.polinode.com/): Cloud-based platform for network
analysis.

[iGraph](http://igraph.org/): Package for network analysis. Available for
[R](http://igraph.org/r/) and [Python](http://igraph.org/python/).

[edgewise](https://github.com/testedminds/edgewise): Clojure library for network
analysis.

[lein-topology](https://github.com/bobbyno/lein-topology): Generates graph data
for a given Clojure library, can be used in conjunction with `edgewise` above to
analyze the software network structure.

Also, I don't know any Clojure yet, but since so much of the day was spent
with Clojure-based tools, I did collect a few links for learning Clojure:

[4Clojure](http://www.4clojure.com/problems): A koan/kata-like site for learning
Clojure through exercises.

[Gorilla](https://github.com/JonyEpsilon/gorilla-repl): A notebook-type REPL for
Clojure, kind of like Jupyter and apparently better than the actual Clojure
kernel for Jupyter ([CloJupyter](https://github.com/roryk/clojupyter)), which
has a few bugs.

Some ideas I had for studies that could be done investigating the network analysis
of software:

* Get network representations of many software libraries in a given language,
  and have some independent metric(s) for either performance or design quality.
  Show statistically significant correlations between network properties and
  such metrics.

* Time series showing how the network architecture of software evolves while
  moving from a "small-scale" to "large-scale" project.

* Do different types of languages lend themselves to different types of network
  topologies? (E.g. functional vs object-oriented vs procedural.)

* Do different "subgraphs" correlate with well-known "design patterns" outlined
  in best practices for software design?

I wonder if any of these have already been done in the theoretical computer
science field. Worth searching on arXiv, one of these days.
