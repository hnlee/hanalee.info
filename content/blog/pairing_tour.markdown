Title: Pairing tour
Date: 2017-01-12 
Category: blog
Tags: 8th light, apprenticeship
Author: Hana Lee
Summary: Summary of my apprenticeship pairing tour

The penultimate stage of the resident apprenticeship at 8th Light is a pairing
tour, where I got to spend time pairing with the crafters who will sit on my
Review Board (i.e. the people who decide whether I get to "graduate" from my
apprenticeship). I spent a day with each crafter and got exposed to a variety of
different clients, languages and frameworks, project management tools, and work
styles, all in under two weeks. Here are some notes and thoughts on how it went.

**Eric M.**: The day was spent updating the front-end Javascript library used for
UI elements to use ES6, with Webpack and Karma to run builds and tests, rather than 
Coffeescript with Grunt. Since my previous experience with Javascript had been
with ES5, I got a taste of how ES6 and Coffeescript syntax differed. It also
showed me what a well-constructed Javascript library should look
like, with good unit test coverage and a modular architecture that lends itself
to reuse.

**Kristin**: I had another day spent with Javascript, hunting down a bug that turned out
to be especially difficult to trace because of duplication that existed due to
the feature being in a transition phase. We kept inserting `console.log()`
statements and seeing nothing in the inspector until we finally realized that
the code being called existed in a completely different portion of the file
tree! Once we figured out what going on, we could then fix the bug, then fix
another bug that we discovered while testing the functionality in the browser,
and finally make a pull request with the changes. It also sparked some good
software design discussions about why the duplication existed and what the best way would be to
resolve the confusion it created.

**Doug**: Pairing with Doug was a bit unusual, since he is one of the two Managing
Directors of the Chicago office. But it was rather fascinating to shadow him
during his day and find out what his many responsibilities look like.
Some meetings were with other management making high-level strategic
or staffing decisions, and other meetings were with the teams that
reported to Doug. Up until now, I haven't had many opportunities to see a really
good manager in action, so I was really struck by the fact that the crafters
that spoke with Doug all had a great deal of trust in him and were comfortable
being honest about the problems they were facing in their work. I think this
trust is able to exist when the manager shows trust in the team first. 

**Vincent**: Vincent is one of my mentors, so I already knew him quite well, but I
had never seen any of his client work before. We spent the day trying to lay the
groundwork for "A/B testing" (quotation marks because the test group would be
selected nonrandomly and their identities known) by exposing endpoints that
would be necessary for identifying whether a user belonged to the test or
control group. Due to the existing infrastructure, the service that would have
the test feature could not talk directly to the database containing the user
information, so we had to figure out how to communicate that data via an
intermediary service that connected to a Grape API that connected to the database.
(If that sounded complicated, it definitely was.)

**Eric S.**: Eric is my other mentor, and since his usual client has a lot of
security procedures, I paired with him on a day when he didn't have to be on
site. Since he's the Director of Training, I ended up sitting in on a few
meetings that related to the various training services that 8th Light provides
to businesses and even got to provide some feedback on a curriculum being
developed. Towards the end of the day, he walked me through one of his side projects,
implementing a browser version of Space Invaders in F# and discussed how to
test a game loop in a functional paradigm. I didn't know any F#, so it was an
interesting chance to look at an explicitly typed functional language, as well
as a good demonstration of how to make things that are difficult to test more
testable.

**Nicole**: I was supposed to pair with Zack originally, but because he is in
between clients, he decided that it would be more productive for me to pair with Nicole, his former
apprentice. I had paired with Nicole before, when she was still an apprentice,
on our feedback rating app, so it was good to be working with her again. We
worked on an internal 8th Light application that was written in Clojure; it was
also good to be working in Clojure again. We wrote a validator for a new
field added to a form and spent quite a lot of time hunting down every test that
used that form in some way to make sure that those tests now worked with the new
validation requirement. The test suite all passed but then the feature didn't
work in the browser; the bug required some outside assistance to track down
and turned out to be due to a parameter not being passed to a third-party
library.

**Rob**: The first story of the day was adding a logger to an API managing
document uploads. The code was all in C# and had to be edited in Visual Studio
through a VM, which was a first for me. We used a third-party library to do the
logging, but it took a lot of reading and experimenting to get it installed and
then figure out where it needed to be injected. But we got it to log all API
requests and responses and finished the story pretty quickly. Then we waded
through the details of a few other stories and realized that they either had
already been addressed or needed further consultation with business
stakeholders. The last story we worked on was finishing the setup of a Flask API
that would eventually hold endpoints for a new service. That was getting close
to the end of the day, but I did get to write some Python and put in a passing
test for the root path route.

**Lisa**: I paired with Lisa today, as the last stop on my pairing tour. She is
working on a greenfield app, which has a React front-end and a Rails backend.
The morning was spent on doing a code review of a pull request and addressing
comments on a pull request she had made before, and then the afternoon was spent
pairing with Jerome, another 8th Light crafter on the same project. I found React to be really
interesting, since it makes some aspects of DOM manipulation seem a lot easier
than just with plain Javascript and JQuery, so now I'm trying to think of ways
that I can learn more about the framework in a future side project. Lisa also
had a whole host of useful tips---from making more informative pull requests to using
`git checkout -` to switch to the last branch---that she imparted during the
day, which I plan to put into use.

Overall, the pairing tour was a great experience, allowing me to see what a
crafter actually does on a day-to-day basis. Getting to see so many new code
bases, all with different languages and frameworks, was also really
illuminating; it shed new light on how a lot of decisions (good and bad) about
software architecture get made as well as the challenges of working with legacy
code. I'm in the middle of reading _Working Effective With Legacy Code_, and I
think some of the content will make more sense to me now that I've actually
experienced trying to modify a truly large existing code base. Everything that
I've worked on up until now has been quite small and manageable,
with not more than three contributors at most; it really is worlds apart from
a piece of software that multiple teams have worked on, often for several years.

I also got to see more than just code. It was really educational to see how
different developer teams work together: how they conduct their standups and
IPMs, what their development workflows are, how they divvy up story cards and
tasks, and even just how they consult one another individually when they have
questions. Reading about agile processes in a book is not really the same as
seeing how they are conducted in real life. Each organization, as well as each
individual, ends up making compromises, and it's interesting to see how the same
tradeoffs recur over and over again, although they are solved in different ways.

Tomorrow begins the final stage: challenges! I have no idea what these will be
like since they generally keep them a secret from apprentices. What I do know is
that the next two weeks will probably be intense. Wish me luck!
