Title: Prime Factors coding kata 
Date: 2016-07-26
Category: blog
Tags: 8thlight, apprenticeship, java, codingkata 
Author: Hana Lee
Summary: Thoughts on practicing the Prime Factors coding kata

The concept of a coding kata originates with [Dave
Thomas](http://codekata.com/kata/codekata-how-it-started/) who based it on his
practice of karate. When I started looking around for potential katas, I found a
lot of blog posts that argued over what the purpose of kata was and whether they
were useful. In particular, there seems to be conflict over whether you are
supposed to perform kata the same way every time or use it as an opportunity to
explore the solution space to an interesting problem.

My prior experience with kata up until now have been via a different Japanese
martial art, kendo. I imagine kata function more or less similarly there as they
do in karate: a series of choreographed movements that are supposed to
demonstrate important principles and ideal form. What becomes clear as a
beginner is that you may be doing the same sequence of moves each time but you
never really do manage to move in the exact same way. One time, you may hold
your bokuto (the wooden blade that you use for kata) a centimeter higher; the
next time, the third step you take might land you slightly closer or further
from your opponent. (Kendo kata are always done in pairs, simulating an exchange
of strikes between two swordsmen.)  When performed mindfully, kata should help
the practitioner achieve new insight into their art.

The other important aspect of kata is that there is usually a Platonic ideal
form to which one can aspire to approach asymptotically but probably not
actually achieve. (Unless you are a short old hachidan with a pot belly that
nevertheless moves like lightning.)

Anyway, practicing coding kata has some similarities and some differences. I
haven't repeated my chosen kata all that many times yet, but I definitely do it
slightly differently each time I tackle it from memory. On the other hand, I
don't think one can claim there is one perfect sequence of keystrokes for a
given coding problem.

I've been practicing the Prime Factors kata, which was
originally characterized by [Uncle
Bob](http://butunclebob.com/ArticleS.UncleBob.ThePrimeFactorsKata). It's a
fairly simple algorithm used to generate prime factors of any natural number.
The first time, I followed Uncle Bob's walkthrough step for step; since then,
I've been going through the kata, TDD-style, on my own. What I've been wondering
how to handle is the fact that I remember the end solution and start to skip
steps in the process of getting there.

For example, after writing the test to factor 2, the walkthrough implements the
following to make it pass:

```{java}

if (number > 1) {
    primes.add(2);
}

```

But what I habitually come up with is:

```{java}

if (number > 1) {
    primes.add(number); 
}

```

Which also means that I never write a test for factoring 3 because then it seems
like a trivial case.

Another example is after writing the test to factor 4, the walkthrough uses the
following code to make it pass:

```{java}

if (number > 1) {
    if (number % 2 == 0) {
        primes.add(2);
        number /= 2;
    }
    if (number > 1)
        primes.add(number);
}

```

Whereas I again end up jumping ahead of myself to:

```{java}

int factor = 2;
while (number > 1) {
    primes.add(factor);
    number /= factor;
}

```

Now that I lay out them out side by side like that, it seems apparent that I am
always choosing to go one or two levels of abstraction beyond what the unit test
immediately requires. Hmmm.

It also seems that one can use coding kata to explore multiple routes to the
same destination: i.e. that in some senses, one can and should use the
opportunity to do the kata differently each time.  Some kata seem more suited
for this approach than others. So far, the only thing that I have tried is to
test the performance of the algorithm on large primes. (It will work for any
number up to the memory limit on Java's `int` type.) Some ideas that I would
like to play around with once I am reliably able to reproduce the steps in the
walkthrough from memory:
 
* Handling negative numbers (should the code return an error or the prime
  factors of the absolute value?)
* Handling numbers that have to be stored in `long` because they are too
  big for `int`
* Deriving one of the well-known factorization algorithms (e.g. [Fermat's
  method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) or
  [Euler's
  method](https://en.wikipedia.org/wiki/Euler%27s_factorization_method)) via
  TDD (is that possible?!)

