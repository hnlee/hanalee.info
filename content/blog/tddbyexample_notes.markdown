Title: Test-Driven Development by Example 
Date: 2016-07-23
Category: blog
Tags: 8th light, apprenticeship, java, tdd, books
Author: Hana Lee
Summary: Notes on _Test-Driven Development by Example_ by Kent Beck

I finished working through the two examples in this book as well as reading
through the last part on common "patterns" or principles to help generalize the
process of test-driven development. For the first part, building a multicurrency
calculator, I directly followed the book. The second part, which builds the core
automated testing functions of xUnit, was demonstrated in Python, so I used the
opportunity to practice and followed along in Java. My code is up at
[Github](http://github.com/hnlee/tddbyexample) and undergoing review by my
mentor and co-mentor.

I jotted down a lot of notes while reading through the book, particularly the
last section, which I suspect I will end up revisiting as I gain more experience
with test-driven development. I'll try to present them here in a semi-organized
fashion.

### Tips for writing tests

* I found the following quote worth keeping in mind: 

> You will likely end up with about the same number of lines of test code as
> model code when implementing TDD (p. 78)

As a note, this principle does not mean you end up writing more total lines of code,
since the TDD process also encourages you to keep your model code simple.

* Overall, the number of test classes should equal the number of model classes
(although you don't necessarily need an exact one-to-one correspondence).

* Tests should be independent of one another. They should be able to run in any
order.

* Differences in test data should represent meaningful, different use cases.

* When writing a test, try writing the assert statements first.

* Another quote worth keeping in mind:

> You are writing tests for a reader, not just the computer.

Tests can function as a sort of documentation by demonstrating the behavior of
the software under different use cases. Similarly, writing tests for packages
created by other people can be a good way of learning how to use them.

* However, in your own work, you usually do not test the parts where you use
code written by others.

* When you don't know what test to write next:
    * Write a test for functionality that seems doable but not obvious how to
    implement.
    * Use a to-do list to guide your test-writing.

* Log strings can make testing easier.

* Treat the objects like black boxes in your tests. This strategy ensures that
the objects stay modular and do not get too coupled. Tests should leave the
objects in the same state they were in prior to testing. 

### Tips for getting tests to pass

* If a test case seems too big, write a smaller test focusing on the broken part
of the bigger one. In this way, you can isolate the bug by finding the smallest
test that fails.

* Start with a "fake" implementation -- a trivial or non-meaningful solution --
to get the test to pass, then refactor with the right implementation.

* If you need to handle collections of objects, implement it for a single object
first, then generalize to collections.

* In general, think first about the code's behavior, _then_ think about its
design.

### Tips for refactoring

* Beck frequently uses the concept of "triangulation", where you only implement
abstraction after you have two or more examples with duplicated behavior. On a
similar note, only unify code when it has become identical in both examples. 

* There are certain design patterns worth keeping in mind for refactoring: null
objects, template methods, pluggable objects and selectors, factory methods,
impostor objects, composite objects, and collector parameters.

* Refactor long methods by taking out one part and putting it in a smaller
separate method.

* Temporarily duplicating code or data is a good way to ensure robustness while
moving things around. It means your tests will keep passing during refactoring.

* The tests themselves can indicate design problems that need to be addressed.
E.g. if the tests require a lot of setup code, if the tests take a long time to
run, and if tests that were passing start breaking unexpectedly. 

### Miscellany

* The Expression object that is created to handle sums of mixed currencies in
the first part can be thought of as analogous to a mathematical vector, in which
each dimension represents a currency. Or another way of putting it would be
multivariate linear systems of equations.

* Beck describes the number of changes per refactoring as a bell curve with a
fat tail. The pedant in me has to note that the graph he shows is a Poisson
distribution (commonly used to model count data, which "number of changes" would
fall under), not Gaussian. It is however leptokurtic as he describes. (Word of
the day: the antonym of leptokurtic is platykurtic.)

* The book mentions the existence of tools used to evaluate test coverage (e.g. JProbe),
which is an interestingly meta concept. Software that analyzes software!

* Another fun math metaphor at the end likens software created through TDD as
converging on steady state attractors, where your final destination is
error-free code.
