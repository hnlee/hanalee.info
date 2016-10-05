Title: Notes on Refactoring 
Date: 2016-10-05
Category: blog
Tags: 8th light, apprenticeship, refactoring, books
Author: Hana Lee
Summary: Notes on _Refactoring_ by Martin Fowler

I had another reading assignment before this one, but there was so much material
that I have three(!) unfinished blog drafts on it. _Refactoring_ is an even
longer book, but most of the material in it is intended as reference, so it's
quicker to write up my notes.

### Defining refactoring

> the process of changing a software system in such a way that it does not alter
> the external behavior of the code yet improves its internal structure

- Also can be thought of as software decay in reverse.

- Make code easier to understand.

- Make code easier to modify.

- Allows you to develop faster because it becomes easier to add new features.

- Reduces the penalty of making changes to the overall design, which in turn
  means less time needed for upfront design. Also encourages simpler design even
  if it is less flexible, since it means design can always be changed. 

### General recommendations 

- Refactor before you add a new feature. Adding a new feature should not involve
  changing existing code (if you have correctly implemented open-closed
  principle or OCP).

- Have self-checking automated tests so you can refactor safely.
  - Run tests frequently after each step in a refactoring. If you forget, go
    back and redo the refactoring with testing.
  - Test boundary conditions and expected exceptions.

- Some design principles to keep in mind:

  - A method belongs with the object whose data it uses.
  - Minimize use of temporary variables and complex conditional logic.
  - Eliminate duplicate code since more lines of code are more difficult to
    maintain.
  - Clean code should not require you to remember anything about it to be
    readable and comprehensible.

- Refactoring can be used to understand unfamiliar code or conduct a code
  review or understand a bug.

- Don't set aside time to refactor. Refactoring should be done all throughout
  the development process in frequent, short bursts.

- Sometimes refactoring can be as simple as renaming variables. Don't hesitate
  to rename.

- __Rule of Three__: Refactor the third time you write code that duplicates
  similar behavior.

### Indirection

- Software design concept that boils down to having many small modular
  components.

- While it creates more pieces of code to manage, the benefits outweigh the
  drawbacks:
  - Easy to share logic between different parts of your code.
  - Allows (through good naming practices) explanation of the intent behind
    each step in your code.
  - When making modifications, keeps change isolated to one part of the system.
  - Simplify conditional logic (e.g. in object-oriented paradigm, you can use
    the identity of the object rather than branching to specify different
    behaviors)

### Limitations of refactoring

- Hard to refactor applications with tight coupling to databases

- May involve changing published interfaces, which requires maintaining old and
  new versions

- Sometimes it is better to rewrite from scratch.

- When _not_ to refactor:
  - Too many failing tests! Only refactor code that works.
  - Close to deadline

### Performance optimization

- Optimization often makes code harder to read and understand. But refactoring
  can make it easier to tune the performance.

- Most of the time, there is a rate-limiting step that is responsible for
  slowing down the program. Don't optimize all parts of the code equally;
  identify where this step is (e.g. big-O analysis). 

### Code smells

(There are probably dozens of blog posts that have already regurgitated this
material partially or in full, so I'm just going to include some mnemonics to
help myself remember what each one is about.)

__Duplicated code__: Self-explanatory

__Long method__: Some heuristics for identification
    - "When we feel a need to comment something, we write a method instead."
    - A lot of parameters or temporary variables
    - Conditional logic
    - Loops

__Large class__: One sign is too many instance variables

__Long parameter list__: Note that this "smell" may end up being necessary in
some cases to avoid unwanted dependencies.

__Divergent change__: Basically a single-responsibility principle (SRP)
violation.

__Shotgun surgery__: The inverse of divergent change. Could be sort of seen as
a dependency-inversion principle (DIP) violation in some cases?

__Feature envy__: Method shouldn't use data that doesn't belong to its object!
(Except for some design patterns like Strategy or Visitor. So think about
trade-offs.)

__Data clumps__: Data that tends to be used together need to be in their own
object.

__Primitive obsession__: Use objects rather than primitives (e.g. Java's
String).

__Switch statements__: Use polymorphism rather than switch-case branching.

__Parallel inheritance__: Duplication of class hierarchies.

__Lazy class__: Is this class doing anything?

__Speculative generality__: Functionality that isn't being used yet.

__Temporary field__: Instance variable that isn't being used.

__Message chains__: Chains of calls between objects.

__Middleman__: Heuristic is that if an object is delegating half its methods to
the same object, those two objects should communicate directly.

__Inappropriate intimacy__: Boils down to lack of encapsulation and tightly
coupled classes.

__Alternative classes with different interfaces__: Self-explanatory

__Incomplete library class__: Situation where you need to make a slight
modification to a library.

__Data class__: Classes that do nothing but hold data that is being called by
other classes.

__Refused bequest__: Not always a problem. But one example of when it is: a
subclass that doesn't support the interface of its superclass.

__Comments__: Not inherently bad but usually pop up to mask the lack of
readability or comprehensibility. Address the underlying problem directly and
need for comment usually disappears.

### Refactoring tools

I wonder if a refactoring tool rather resembles a compiler, since it needs to
understand code syntax in much the same way.

- Help integrate refactoring into regular development process by reducing the
  cost of refactoring.

- Allows for safe refactoring without needing to rerun tests.

- Uses parse trees to represent the internal structure of a method.

- Needs to be safe and accurate.
