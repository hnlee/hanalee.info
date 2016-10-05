Title: TDD metaphors
Date: 2016-08-16
Category: blog
Tags: 8thlight, apprenticeship, tdd
Author: Hana Lee
Summary: 
Status: draft

Earlier this year, I started watching [lecture
videos](https://archive.org/details/SICP_4_ipod) for the MIT course that
formed the basis for the famous textbook, [_Structure and Interpretation of
Computer Programs_](https://mitpress.mit.edu/sicp/full-text/book/book.html). I
still have yet to watch the bulk of the lectures, but the very first one
presented a view of programming that became a personal light bulb moment:
computer science is not so much about computers themselves but about the
science of processes and procedures for problem solving. One could even consider
it the modern counterpart to epistemology. So it is appropriate that
software engineers and developers spend so much time talking not just about the
processes they implement in their code but about the process of writing code
itself. From the details of one's _tmux_ setup to the principles of
agile, quite a lot of thought is put into identifying the specific and
general ways in which to make software development more efficient and
better quality. So we can look at TDD as a sort of meta-process of creating
processes.

It should then follow that there would be parallels for TDD in other domains,
and indeed, there are three obvious analogies that come to mind. The
usefulness of a metaphor lies in how much it sheds light on the object of
comparison; I can't claim that any of these analogies actually give added
insight into TDD itself, but I think it's interesting to think about.

### Scientific method

The scientific method, stated simply, involves posing a question, developing a hypothesis, testing
it with controlled experiments, and rejecting or adjusting the hypothesis if the data does
not support it. Of course, in reality, there's a feedback loop between
hypothesis generation and experimentation, which seems similar to the feedback
loop that drives TDD. In TDD, the tests themselves pose a question: What is the
behavior that we would like to see from the software we are building? Then we
come up with a hypothesis: an implementation that should produce that behavior. 
The controlled experiment is of course running our test suite, upon which we
fix and sometimes delete code until the tests pass.

A controlled experiment requires you to change one variable at a time so you can
pinpoint causality (or, well, develop a
matrix multifactorial design, but that is getting beyond the scope of this
metaphor). TDD also requires you to change your code in small increments so that
you always know what is responsible for a failing test.

There are similar aesthetic preferences too. Scientists prefer the simplest
hypothesis that will fit the data; programmers prefer the simplest code that
will meet the use cases.

### Mathematical proof

While I was going through the Prime Factors code kata, building up the algorithm
for prime factorization step by step seemed rather similar to arriving a
definition of prime factors for a mathematical proof. The assert statements
function like lemmas, which you "prove" in succession by implementing code until
you arrive at the full theorem (or, in the case of TDD, the full algorithm). 

Or another parallel: my mentor drew an explicit connection between TDD and proof by induction when he
explained the ["zero, one, many"
principle](http://agileinaflash.blogspot.com/2012/06/simplify-design-with-zero-one-many.html).
If you can demonstrate your code works for zero objects, one object, and more than one
object, it can probably handle anything you throw at it.

I know from vague osmosis that theoretical computer science deals with proofs
and provability, but I do think there is something really interesting in the way
TDD tries to break down software development into a series of steps that
(ideally, anyway) should follow logically from the previous ones.

### Biological evolution

Of course, the parallel that occurred to me first was natural selection.
(Probably not surprising that I tend to look for biology metaphors to understand
other subjects!) Natural selection is the basic mechanism underlying evolution,
wherein the genetic variation among individuals in a population
leads to differences in fitness or the ability to survive and reproduce in their
environment. The more successful individuals have more offspring, thus resulting
in a larger proportion of the population possessing the genetic variants
responsible for the increase in fitness.

Of course, we should be clear: the source of variation in nature is randomly
occurring mutations that are not directed in any way: they are no more likely to
increase an organism's fitness as decrease it, and in fact, in most cases,
result in no change to fitness at all. (See neutral theory.) In software, the
variation is not random; a programmer is making the changes in a definite
direction. 
 
Still, the tests in TDD function like the environment to which the software
organism must adapt via a series of small changes that are really just guided by
the single constraint of needing to pass all the tests. Interestingly, this
constraint ends up manifesting in surprisingly complex ways, in which certain
patterns and designs lead to better testability and better quality. In a similar
fashion, in nature, the constraints that emerge from the seemingly simple
requirement of "survival and reproduction" mean that the fitness landscape only
holds a few "optimums" to which evolutionary trajectories will converge.

A less vague and more specific parallel: when migrating code around, what TDD
encourages is that you first duplicate your code at its destination and only
after the tests pass do you delete it from its original location. That's rather
like paralogs and pseudogenes: a gene will duplicate, and the second copy will develop
some new function, while the original copy ends up becoming nonfunctional and
may undergo partial or full deletion. (Though evolution being less clean than a
text editor means that you can still see the traces of the old gene in DNA
sequence.)

Also, sometimes TDD necessitates stepping backwards in your code in order to
make a leap forward later. Experimental evolution studies in the laboratory
have revealed similar sequences where a deleterious mutation must be acquired
first in order for a successive mutation to end up being favorable to the
organism.

Finally, what TDD encourages the development of reusable, extendable software that can be easily
modified to meet future, unknown use cases. Similarly, selection in changing,
turbulent environmental conditions will encourage adaptability.
 
