Title: First day at 8th Light
Date: 2016-07-18
Category: blog
Tags: 8th light, apprenticeship, java
Author: Hana Lee
Summary: My first day as a resident apprentice at 8th Light.

It's been a while since I last updated this blog. Last time I wrote, I was
starting to apply for jobs outside academia. I was primarily focusing
on data scientist positions, due to my experience with statistical
analysis, but I was also interested in the possiblity of a more generalist
software engineering role. The latter would require an expanded skill set
and knowledge of software development, since as a researcher, I
usually only wrote code for a single user: myself.

Enter 8th Light, a software consulting company that has pioneered the
apprenticeship model for training software engineers. I'd heard about
8th Light while attending tech Meetups in Chicago and their reputation for
excellent coding practices and mentorship. So one day, I submitted an
application, figuring it couldn't hurt.

To my surprise, I was invited to do a code submission, involving
refactoring and extending the code for a tic-tac-toe game. I can't emphasize
enough how much I was able to learn from this experience alone; I think it
was the first time I really got to experience a code review with detailed
feedback on my code. Then I visited 8th Light's Chicago office for an
interview, and to make a long story short, I signed a contract to start as
a resident apprentice in July, with [Eric Smith](http://paytonrules.com) as
my mentor.

Today was my first day, and I spent the first part of it dealing with
administrivia, like handing in paperwork, setting up my laptop, getting my
company email and Slack accounts, etc. I got to briefly meet some of the
other apprentices during a weekly talk; the topic this time was on leadership,
particularly on different [leadership
styles](http://www.fastcompany.com/1838481/6-leadership-styles-and-when-you-should-use-them), 
when to use them, and how to improve one's leadership skills. (I think that
alone illustrates a lot about 8th Light's company culture: the emphasis on
self-cultivation, the attention paid to organizational and interpersonal
dynamics, and the conscientious approach to the work being done.) Then I met up
with Eric, who wrote the email introducing me to the company and filled
me in on how the apprenticeship would proceed on a day-to-day basis.

I spent the afternoon working through [Test Driven Development by
Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530).
The book demonstrates the process of test driven development by
walking you through step by step two example cases. The first builds a
multicurrency calculator, and the second creates a framework for
automated testing. I'd read through the book before and tried to follow the
first example by translating the Java code into Python. But now that I had spent some time
absorbing the basics of Java (as preparation for the apprenticeship),
Eric suggested that I go through the book with code written in Java. That became
my first topic of study.

First I spent some time setting up JUnit, the Java package for unit testing,
and figuring out how to use it. Then I opened the book to chapter 1 and began
putting together the multicurrency calculator. It definitely helps to
be reading this book again with more knowledge of Java; the logic behind the
steps taken is much clearer now that I have a better understanding of how
Java classes are structured and how they work. I worked to the end of chapter
12, which begins implementing an addition method.

What troubles me is that while I think I mostly comprehend the sequence of
thoughts behind each step, I don't yet have a grasp of the more general
principles that should guide decisions during the development process. E.g. there
are some instances when one has to "go backwards" (revert to previous code) in
order to have a test pass. While I understood why that was necessary at that
particular stage of developing the multicurrency calculator, I don't
know how I would recognize another situation that would call for the same
tactic. Kent Beck, the author, says the intuition will develop with
practice, so hopefully it will become more apparent with time.

Two points I have taken away from this afternoon's work:

* Don't be afraid to write ugly code. Write something that will make the test
pass first, _then_ refactor it to be good code.
* There's not a set "size" to the steps taken; you can modulate according
to the situation. But if you're running into problems, the immediate response
should be to make the steps smaller. A possible rule of thumb may be that
the steps should be small enough to make you feel slightly impatient.

