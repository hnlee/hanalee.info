Title: Testing and data analysis in Python
Date: 2016-12-21
Category: blog
Tags: python, apprenticeship, 8th light, tdd, data science
Author: Hana Lee
Summary: Incorporating testing into my data analysis workflow 

Something that occurred to me more frequently than I would like to admit while I
was writing code to analyze data back in graduate school was that I would start a
computationally intensive process, only to find that it would terminate at the
penultimate step due to a simple bug in my code. At the time, I knew nothing
about testing frameworks or test-driven development. I had a variety of
approaches of dealing with this problem:

* Go through statements one by one in the REPL (the ones that I could run
  quickly, anyway)
* Make sure I could check on interim progress through standard output or output files
* Split up my scripts into smaller units

None of these really substitute for the confidence you have with test coverage,
however. Since I've returned to wrangling with data on my current client
project, I've sought to incorporate testing into my workflow.

Most data scientists endorse the use of [notebooks](http://jupyter.org/) as a form of reproducible
research. Indeed, it's a good way to explore a data set and share your analysis.
I've been treating what I do in notebooks as a spike; it's a good place for one-off
code and getting familiar with new APIs or libraries.

But when I find myself repeating a block of code over and over again, I move to the text editor and start writing tests for a reusable
function. These functions then assemble into modules that I can import as necessary to carry out any lengthy processes or computations. I'm not quite at the stage when the final script I run only makes calls to test-covered functions, but I'm getting there. And certainly, the bugs I'm experiencing now tend to happen in the parts of the script that use untested functions.

I use [pytest](http://doc.pytest.org/en/latest/) to run my tests. I find the
output easier to read and interpret than the built-in
[unittest](https://docs.python.org/3/library/unittest.html). Other people
recommend [nose2](https://nose2.readthedocs.io/en/latest/index.html), which I
haven't tried yet.

At the current stage of my project, I've been using the APIs from various social
media platforms to collect data. While testing the functions I use to call these
APIs and parse the JSON responses, I try to avoid directly interacting with
those APIs (especially because they might have rate limits!) and create small
mock APIs to pass to my functions instead. I found one library that was
particularly good for mocking out HTTP requests and JSON responses, called
appropriately enough [responses](https://github.com/getsentry/responses). Note
that if you're having trouble with the mocks, make sure you have the
`match_querystring` boolean set to `True`. Otherwise, any query parameters you add to
the URI of your request won't be matched. (That's not within the documentation
anywhere, and I had to go into the source code to figure out that parameter
existed.)

I haven't heard much about testing frameworks or TDD in data science circles. People do
talk a lot about validation, but that's not of the code itself but of its
output. I think it's
because data science doesn't focus so much on building software; most of the
code we write is procedural and not necessarily extensively reused. Since we
may work primarily or only with third-party libraries (which hopefully _are_
already
well-tested before release), the need for testing the code ourselves we write probably does not seem as
urgent. Nonetheless, taking the time to write tests, even for a simple series of statements that you
don't plan to use again, can help you be confident that the scripts you're
running won't fail on some easily preventable bug. 
