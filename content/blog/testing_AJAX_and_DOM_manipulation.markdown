Title: Testing AJAX calls and DOM manipulation
Date: 2016-11-03
Category: blog
Tags: javascript, 8th light, apprenticeship, tdd, rails
Author: Hana Lee
Summary: Challenges encountered while testing Javascript in a Rails application and how we solved them 

I'm currently working on a pairing project with <a
href="http://github.com/NicoleCarpenter">Nicole</a>, a fellow <a
href="http://8thlight.com">8th Light</a> apprentice, where we are developing an
internal tool intended for rating how well people review projects on three
criteria: whether they are kind, specific, and actionable. (While the obvious
use case is for evaluating the helpfulness of code reviews, it could conceivably
be used for any endeavor where feedback is solicited, including blog posts or
event planning.) We are building the application in Ruby and Rails, but there
are several features that require Javascript to mediate user interactions. Most
of these are fairly simple uses of jQuery and AJAX to display a form or error
message dynamically on the same page without redirection or reloading. But
testing our Javascript turned out to be more difficult than we anticipated.

We used <a href="http://jasmine.github.io/">Jasmine</a> as our testing framework, but Jasmine by itself is not
sufficient to cover asynchronous AJAX requests and DOM manipulation. We spent quite
a lot of time navigating Stack Overflow responses and asking for help from
coworkers, which led us to wrestle with <a
href="https://github.com/jasmine/jasmine-ajax">jasmine-ajax</a> and <a
href="https://github.com/velesin/jasmine-jquery">jasmine-jquery</a>. Both of
these plug-ins were significantly overpowered for what we were trying to test,
and we got nowhere while trying to figure out how to use them correctly.

Luckily, <a href="http://paytonrules.com">my mentor</a> got back from vacation, and I was able to pick his brain for
assistance. He suggested using <a href="http://sinonjs.org/">sinon</a> and <a
href="https://github.com/searls/jasmine-fixture">jasmine-fixture</a>, which were
both fairly simple libraries with documentation that was easy to decipher.

The first step was to separate the AJAX calls themselves from the DOM
manipulation. I set up my tests using `sinon`'s handy `fakeServer` and `spy`
classes. I told the fake server to give a 200 status response to the type of 
AJAX request I was testing and a spy to watch that the AJAX call was made and 
successfully completed.

Now to test the DOM manipulation. I had tried to set up HTML fixture files while
experimenting with `jasmine-jquery`, but that seemed like a lot of redundant code
for testing functions that were pretty much just displaying or hiding elements
on a page. The `affix()` function from `jasmine-fixture` was much simpler,
allowing you to quickly set up the elements you needed to test, while also
taking care of cleaning them up after the test was run. I could create an
element, call my DOM manipulation function, then check to see that necessary
change had happened to the element.

These two steps allowed me to create a toolkit of reusable functions for making AJAX GET and
POST requests and for displaying, hiding, and replacing parts of the DOM. Then I
could easily write unit tests for the specific user interactions that combined those
functions.

We are using <a
href="https://github.com/jnicklas/capybara">Capybara</a> to handle our
acceptance tests. While Capybara is very powerful, you do need to be thoughtful
about how you write any tests that cover functionality involving asynchronoous
requests. One <a
href="https://robots.thoughtbot.com/write-reliable-asynchronous-integration-tests-with-capybara">blog
post</a> provides a good summary of the points to keep in mind. However,
something very simple that no blog post or Stack Overflow answer seemed to
explicitly cover is that you need to include `:js => true` in your test blocks
for Rspec to realize it needs to use the Javascript driver.

Speaking of which, it probably helps to use a headless browser instead of the
Capybara default for the Javascript driver. I ended up going with PhantomJS
through the <a
href="https://github.com/teampoltergeist/poltergeist">Poltergeist</a>, since we
are using <a href="https://travis-ci.org/">Travis CI</a> for continuous
integration, and it has PhantomJS already installed.

Finally, note that if your acceptance test involves any interaction with hidden elements
on your page, Capybara may require you to explicitly set
`Capybara.ignore_hidden_elements = false` (depending on your version).

The source code for our project, still in progress, is available on
[Github](https://github.com/hnlee/reviewr), and a demo is deployed on
[Heroku](http://reviewr-app.herokuapp.com/).
