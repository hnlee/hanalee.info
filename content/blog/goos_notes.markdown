Title: Growing Object-Oriented Software, Guided by Tests 
Date: 2016-08-11
Category: blog
Tags: 8th light, apprenticeship, java, tdd, books
Author: Hana Lee
Summary: Notes on _Growing Object-Oriented Software, Guided by Tests_ by Steve Freeman and Nat Pryce

This book focuses on how to do test-driven development with object-oriented
software, but it also ended up introducing to me several general principles
about software design and defining vocabulary that are routinely referenced in
articles and blog posts about software. In other words, it is dense and provides
a lot to digest.

The first third of the book lays out the concepts and then most of the last
two-thirds work through an example of building an auction sniper application.

### Definitions

* __acceptance test__: tests the functionality of a feature and how the whole
  system operates

* __integration test__: tests how code interacts with external/invariant code

* __unit test__: tests the functionality of a single object

* __end to end test__: tests the system as if it were a black box and only
  interacts with it through the UI

* __edge to edge test__: tests every step from build to deployment to release

* __coupling__: change in one component forces change in another (i.e. the
  modularity, or lack thereof, of the system)

* __cohesion__: responsibilities form a meaningful unit

* __role__: related group of responsibilities

* __responsibility__: obligation to either perform a task or know information

* __collaboration__: interaction between objects or roles

* __mockery__: jMock term that refers to the context of the object being tested

* __mock object__: a test object that substitutes for objects that interact with
  the object under test

* __expectations__: rules that define how mock objects should be invoked

* __"walking skeleton"__: most minimal implementation necessary to have an
  end-to-end test

* __encapsulation__: behavior of an object can only be affected through
  methods for interaction with other objects

* __information hiding__: how object functions remains internal and invisible to
  other objects

* __aliasing__: sharing references to mutable objects, breaks encapsulation

* __peers__: objects with which a given object communicates 

* __dependencies__: services from peers without which the object cannot
  function

* __notifications__: peers that need to be updated with the object's
  behavior or status

* __adjustments__: peers that adjust the object's behavior to work with
  the rest of the system

* __context independence__: object has no internal knowledge about its
  environment

* __interface__: "whether two components will fit together"

* __protocol__: "whether two components will work together"

* __spike__: initial code written to figure out what to do, later rolled back
  and rewritten more cleanly

* __implementation layer__: describes how the code will do something

* __declarative layer__: describes what the code will do

### Key Ideas

* In general, we want _low_ coupling and _high_ cohesion.

* Object-oriented design can be thought of as the network of communications
  among the objects in your software system.

* Objects are mutable; values are immutable. 

* Interfaces help define an object's roles.

* "Tell, Don't Ask" or ["Law of
  Demeter"](https://en.wikipedia.org/wiki/Law_of_Demeter)

* Mock objects are used to test interactions between objects.

* Begin with a "walking skeleton".

* Start each new feature with an acceptance test to determine how the new feature
  will function.

* Separate acceptance tests for completed features to catch bugs vs acceptance
  tests for new features in progress.

* Write unit tests for object behavior rather than the object's methods.

* Unit tests check the internal quality of the code; acceptance tests check the
  external quality.

* Something that is difficult to test is probably badly designed.

* [Single Responsibility
   Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle):

> Our heuristic is that we should be able to describe what an object does
> without using any conjunctions ("and," "or").

* Interacting with the composite object should be simpler than interacting with
  the components that compose it.

* "Mock an object's peers [...] but not its internals."

* Techniques for introducing new objects:

    * "Breaking out": when code for an object becomes too complex, separate it into smaller
      units 
    * "Budding off": placeholder for a new object, to be filled in with more
      implementation details later
    * "Bundling up": creating a new object for a group of objects that are always
      used together

* When to break out:

> Break up an object if it becomes too large to test easily, or if its test
> failures become difficult to interpre. Then unit-test the new parts
> separately.

* When to bud off:

> When writing a test, we ask ourselves, "If this worked, who would know?" If
> the right answer to that question is not in the target object, it's probably
> time to introduce a new collaborator.

* When to bundle up:

> When the test for an object becomes too complicated to set up [...] consider
> bundling up some of the collaborating objects.

* Use interfaces to name roles played by objects. Keep interfaces narrow in
  scope.

* Goal is to move to "higher-order" programming: "composing programs from
  smaller programs".

* Don't use mocks for third-party code, since it is usually not changeable.
  Use an adapter layer to implement interactions with third-party code.

