Title: Sub- and superclasses
Date: 2016-10-06
Category: blog
Tags: 8th light, software design, apprenticeship
Author: Hana Lee
Summary: Objects are not nouns but collections of verbs 

We just listened to a zagaku talk on "moving on from inheritance", which in a
lot of ways boiled down to the [SOLID
principles](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) and
["composition over
inheritance"](https://en.wikipedia.org/wiki/Composition_over_inheritance).

(8th Light dictionary: zagaku is a quick talk given by one of the crafters to
the apprentices. In Japanese, it means "seated learning" (座学); the Korean reading of those characters
would be 좌학. We have one everyday from Mondays through Thursdays, on all sorts
of topics, usually but not always related to software or consulting.)

Anyway, I realized during the talk, when a diagram was put up to
illustrate how inheritance is used to extend classes, that we say subclass and
superclass and expect these terms in some sense to operate like subsets and
supersets. (Well, maybe you don't if you are an experienced programmer, but I
initially did when first encountering the concept of object-oriented
programming.) 

But when you use inheritance to extend a class, the resulting visual
representation becomes counterintuitive. The subclass has added functionality
that does not belong to the superclass. So instead of drawing the subclass
enclosed within the superclass, the subclass contains the superclass instead.  That's also essentially what the Liskov substitution principle (LSP), which states that a subclass must be
able to function in whatever context its superclass is called, describes. 

I think there's an additional misleading layer where introductory books use the
heuristic "IS-A" to teach how inheritance works. "Dog IS-A
Canine and Wolf IS-A canine" so both Dog and Wolf should be subclasses of
Canines. But ["Circle IS-A(N)
Ellipse"](https://en.wikipedia.org/wiki/Circle-ellipse_problem), and that's one of the classic examples of
LSP violation. The inheritance relationships between objects should not be
determined by categories but by functionality.

So sets are not really a good metaphor for objects at all. Objects are not
really nouns; they are collections of verbs.
