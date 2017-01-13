Title: Feedback from my mini review board 
Date: 2016-12-20 
Category: blog
Tags: 8th light, apprenticeship, object-oriented programming, ruby, rails, javascript
Author: Hana Lee
Summary: Current status and areas for improvement

A few weeks ago, I had a mini review board to look over the code I contributed
to the pair project that I worked on with a fellow apprentice. After
she rolled off the project, I spent an additional two
weeks working on it solo, finishing up some stories in the backlog and adding
some minor features. Then a group of six crafters, including my two mentors, as
well as the two mentors of the apprentice with whom I paired, reviewed my
code and gave me feedback on the project as well as on the status of my
apprenticeship overall. It's called a "mini" review board because it's a much
smaller preview of the review board that will ultimately review the work I
do during the last two weeks of my apprenticeship to decide whether I will move
on to be a software crafter.

Most of the feedback focused around object-oriented design. The app we built
more or less followed the architecture of a traditional Rails app, with the
accompanying weaknesses. In particular, there was a lot of refactoring that I
could do on the controllers, extracting out the logic into [interactors or
service objects](http://multithreaded.stitchfix.com/blog/2015/06/02/anatomy-of-service-objects-in-rails/) that could then be tested in isolation. Some of the logic in the
views could be put in interactors as well, which sounded like a good move
since there's a fair bit of functionality there that is currently only really being
covered in acceptance tests, rather than in unit tests.

My mentor paired with me later to show me how to safely refactor and
extract interactors from my controllers. Another advantage of this approach is
that it also allows me to do a bit of dependency inversion and not require
manipulation of ActiveRecord models in my unit tests. It's not quite the same
as the [Repository pattern](http://martinfowler.com/eaaCatalog/repository.html), but it achieves a similar goal.

On similar lines, the Javascript in our app currently barely qualifies as
"object-oriented". There are constructors and objects are initialized, but in
reality, the classes are really just namespaces for related functions. One of
the key suggestions I received was to refactor the Javascript to use
encapsulation and implement some of the object-oriented design principles
that I've spent the past several months reading about.

To be honest, we hadn't spent much time discussing the app's architecture while
building the project. We made decisions about the database schema and briefly
discussed whether to implement the Repository pattern (which we attempted then
abandoned because we ran out of time), but otherwise, we unquestioningly
followed the architecture that Rails sets out by default. But of course, when one is a professional consultant, one doesn't want to simply demonstrate the
ability to follow Rails tutorials to the letter. As one of the crafters on my
review board put it, this app doesn't really show anything of my personality
as a developer. So my task is to work on refactoring the code, focusing
particularly on one of the controllers and the Javascript, to get practice in
making those design decisions about the architecture of the app. I've found this
blog post, which my mentor sent to me, particularly useful for thinking about
the bigger picture: [Clean
Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html).

I would like to say that I've made a lot of progress on this task in the weeks
since my mini review board was held, but alas, I've had my time taken up with
a client project instead. I'm quite excited about this project actually,
which involves data science and machine learning, but it's left me with no
opportunities to wrap up loose ends. But I'm going to try to set aside a little time
every day to work on implementing the suggestions I received.

The pair project was my introduction to Ruby and Rails. I have to admit that
I'm not particularly thrilled by Ruby, and Rails is such a behemoth of a
framework that it makes Django look quite small by comparison. Ruby
looks deceptively similar to Python at first, but its underlying
philosophy is almost the antithetical to the Pythonic style of coding.
Nonetheless, so many modern web applications are built in Ruby and Rails that
I appreciate the chance to gain experience with these tools, even if they
wouldn't be my first choice on a personal project. I think it would be
worthwhile to fiddle around with Ruby outside the Rails context. I mean,
Ruby will still be Ruby, with its apparent belief that having multiple
ways of saying the same thing actually makes developers "happy", but at
least it might give me a chance to see the charms of the language beyond the
limited scope of a Rails project.

This pair project also introduced me to Javascript and all the pains of trying
to test user interactions. I can't say that I _enjoyed_ writing Javascript,
but I did find it interesting to try to get it under test. One of the stories
that I worked on solo after my fellow apprentice left the project was to do a timeboxed spike to see if I could get an estimate on how much work it would be to build an [Ionic](https://ionicframework.com/) hybrid mobile app to work with the Rails backend. 
Building an API for the app in Rails didn't seem too difficult actually, but Ionic is built on top of Angular, which in turn uses Typescript, which posed quite a learning curve. (It didn't help that there was a major breaking change between Ionic 1 and 2, to match the difference between Angular 1 and 2!) I barely managed to get a Google login screen working before I ran out of time on my spike.
Nonetheless, that's definitely an area that I would like to explore further in
the future. I haven't built a single mobile app yet, and that's something I
would like to learn how to do.
