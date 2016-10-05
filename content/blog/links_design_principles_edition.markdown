Title: Links, the design principles edition
Date: 2016-09-15
Category: blog
Tags: 8th light, apprenticeship, linkspam, tdd, software design
Author: Hana Lee
Summary: Useful links related to software design principles 

I was gently reminded today that I haven't kept up with writing blog posts,
despite the original goal of posting three times a week. Oops! Currently,
I'm reading _Agile Software Development: Principles, Patterns, and
Practices_, which has been rather like drinking from a firehose of
concepts and code examples. I've moved on from working on a Java implementation
of tic-tac-toe to building an HTTP server in Clojure, which has propelled me to
finally figuring out what GET and POST requests are all about.

I tend to collect links in my private DM channel on the [8th Light](http://8thlight.com) Slack, so I'll start off this
return to (hopefully regular) blogging with another list of useful reading:

[Simplify Design with Zero, One, Many](http://agileinaflash.blogspot.com/2012/06/simplify-design-with-zero-one-many.html): I've found "zero, one, many" to be a really useful guideline to turn to when I'm trying to figure out which unit test to write next or when I'm checking for test coverage. Any loop in your code should be covered by a test for the zero case, the singleton case, and the "many" case (usually suffices to do two).

[Good naming is a process, not a single
step](http://arlobelshee.com/good-naming-is-a-process-not-a-single-step/):
A good series of posts on naming variables in your code. I find that as I
improve my sense of design, finding names that fully and accurately describe
a component's "single responsibility" is crucial to helping me refactor my code
and make it more comprehensible.

[The Three Rules of
TDD](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd):
A classic Uncle Bob post. A slightly different formulation of the TDD cycle
that I find helpful because of two points in particular.

1. Treating compiler failures as failing tests, since I frequently get compiler failures.

2. Only writing enough production code to make a test pass, since one of the
recurring themes in code reviews from my mentors is that I tend to come up
with something more complicated than what the test (and the actual problem
being solved) calls for.

[Beck Design
Rules](http://martinfowler.com/bliki/BeckDesignRules.html): Another take on
how to avoid complicated code: a list of priorities that fit in very well with
the TDD cycle. First, you write code that meets the first priority, passing
the tests. Then, you refactor to remove duplication and express the intent
of your code. (The post talks very usefully about how sometimes there
might be tension between those two priorities and how to find the right
balance.) Finally, the last priority, fewest elements, forces you to
remove anything redundant or not being used (another "code smell" that is
prone to popping up in my code).

[Code for the auction sniper application in
GOOS](https://github.com/sf105/goos-code): [_Growing
Object-Oriented Software_](goos_notes.html) spends the bulk of its volume on an example of an auction sniper software, which is worked through in
detail to illustrate the design decisions and processes that the authors have
laid out. This Github repository contains all the code, and I rather wish I had
known about it when reading the book! A lot of the ideas that the book talks
about only really became clear to me after I had mostly finished my
tic-tac-toe in Java, to the effect that I would probably go about designing a
tic-tac-toe very differently if I had to start over from scratch now. I'm
trying to keep them in mind as I write my Clojure server, though
there is a bit of a translation process 
due to Clojure being a functional language rather than an object-oriented one.

