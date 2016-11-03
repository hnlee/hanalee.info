Title: Links, the Clojure edition
Date: 2016-10-12  
Category: blog
Tags: linkspam, apprenticeship, clojure
Author: Hana Lee
Summary: Useful links related to Clojure 

I'm wrapping up my current apprenticeship project, a simple HTTP server, which
has exposed me to Clojure so that I have a functional programming language in my
toolkit alongside an object-oriented one. I do find functional programming far
more intuitive than object-oriented programming: a lot of the concepts have close parallels in mathematics, and
at least on a naive level, it's much more similar to writing
scripts in an imperative paradigm, which is where most of my experience with
programming lies.

In addition to being an example of a functional programming language, Clojure
also belongs to the Lisp family. So yes, it has a lot of nested parentheses, as
well as as reverse Polish notation. I thought the latter would be hard to get used to, 
but once I started thinking of it as being similar to
mathematical functional notation, it actually made a lot of sense and led to a
very satisfying degree of consistency in syntax that is one of Clojure's (and
Lisp's) main
attractions. 

Here are some interesting Clojure-related links:

[Clojure Cheatsheet](http://clojure.org/api/cheatsheet): Quickest way to
navigate Clojure documentation and look up any function in the core.

[clojure-bowling](https://github.com/stuarthalloway/clojure-bowling):
Implementation of the bowling game kata in Clojure, using lazy sequences. Very
slick and very true to Clojure idiom.

[Clojure Style Guide](https://github.com/bbatsov/clojure-style-guide): Style
guide for Clojure code, which I still haven't fully digested...

[How to ns](https://stuartsierra.com/2016/clojure-how-to-ns.html): A whole
article on specifically how to style namespace declarations, by Stuart Sierra,
the same author for the above.

[TDD in
ClojureScript](https://8thlight.com/blog/eric-smith/2016/10/05/a-testable-clojurescript-setup.html):
I haven't really done anything in ClojureScript yet, but my mentor wrote this
blog post about how to set up a good TDD environment for a ClojureScript
project.

[Tetris in ClojureScript](http://shaunlebron.github.io/t3tr0s-slides/): Speaking
of ClojureScript, a really cool implementation of a browser-based Tetris game.
The slides include the link to the Github repo with all the code.

[SICP lecture videos](https://archive.org/details/SICP_4_ipod): Not
strictly Clojure, but since you can't
mention Lisp without thinking of _Structure and Interpretation of
Computer Programs_...As an alternative or supplementation to working your way
through the text, here are uploaded lecture videos of the MIT course on which
the book was based. Hat tip to the ChiPy mailing list, where I originally got
the link.

...And not really to do with Clojure at all, but:

[Vim anti-patterns](https://sanctum.geek.nz/arabesque/vim-anti-patterns/): I've
taken the tips in this article to heart as I continue in my quest to improve my
Vim usage.[^1]

[Modern pandas](http://tomaugspurger.github.io/modern-1.html): Better ways
to use `pandas`. I have yet to fully delve into this post, but I listened to a
talk last month on `pandas` best practices that was really mindblowing, and the
speaker attributed most of his insights to this blog post by one of the main
contributors to the package.

[^1]: Permit me to take a moment here to rant about the term "anti-pattern". It
is really popular in tech/software circles, to the point where it's been
applied to other contexts. E.g. "meeting anti-patterns" or "office layout
anti-patterns". Let me just point out that when first faced with the term, a
reasonably educated layperson would conclude that it referred to the
_opposite_ of a pattern: something that is disorganized or random. But the
actual meaning is a _negative_ pattern that impedes functionality or
productivity. There's really no good way to arrive at this definition unless
you have the assumption that patterns are inherently positive, which I
guess makes sense to programmers who usually associate the word "pattern" with
"design pattern". But to
the rest of the world, patterns are value-neutral. So it makes very little
sense to apply the term to anything that isn't related to software design.
Arguably, if the reasonably educated layperson can't deduce the correct
meaning from breaking down the word, it qualifies as jargon and doesn't belong
in effective technical writing. (Latter rule courtesy of a professor in grad
school, who memorably told us to stop using "Western blotting" and say
"immunoblotting" instead.) I doubt anyone will agree with me or care,
but what other purpose do blogs serve than to provide an outlet for one's
pedantic pet peeves... 

