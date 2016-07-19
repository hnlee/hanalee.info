Title: ChiPy Mentorship: Finishing Up
Date: 2016-01-14
Category: blog
Tags: chipy, python, data science
Author: Hana Lee
Summary: Finishing up the Fall 2015 ChiPy Mentorship Program

Since my last [update](http://hanalee.info/blog/chipy-mentorship-progress.html), I've made considerable improvements to my classifier for the SF crimes Kaggle competition. Delving into the other variables and engineering new features, such as time of day, helped improve the performance of my logistic regression model considerably. I even got to experiment a bit with _k_-means clustering, which is an unsupervised learning method, in order to define "neighborhoods" from the longitude and latitude data. I jumped up about 306 positions and had a log-loss score of 2.54026 when used to make predictions on the external test data set provided by Kaggle.

I also experimented with combining multiple models and averaging their predictions to improve performance. Random forests on the same feature set gives a cross-validation score of 2.74832, but when combined with the better performing logistic regression model, it helps improve the overall performance of my classifier and gives a log-loss score of 2.49766 on the Kaggle test data.

As the final part of the mentorship program, the mentees will be presenting five-minute "lightning talks" at the ChiPy monthly meeting tonight. Preparing this presentation has been an extensive learning experience in and of itself: it's my first time using the Jupyter notebook system to make `reveal.js` slides. I especially like the "subslide" feature that scrolls vertically instead of horizontally, which gives additional structure to the presentation. I've hosted the slides for the talk on Github: [Predicting type of urban crime: Python, Kaggle, and SF OpenData](http://hnlee.github.io/sfcrimes/#/).

Looking back on the goals I've set, I realize that while I haven't quite fulfilled all of them, I've managed to accomplish a fair amount.

1. I've made multiple submissions to the Kaggle competition, and my highest-scoring submission places in the top 25%.
2. I've learned so much more about machine learning by reading books and watching videos that my mentors recommended to me.
3. I haven't submitted any job applications yet...but I have a [resume](http://hanalee.info/static/pdfs/resume.pdf) instead of the old academic-style CV and am writing cover letters for several job listings.

I plan on tinkering a little bit more with the SF crimes data over the next few days, as I have hopes of further improving my model. I'm currently running gradient boosting on the training data, and I would like to do some more parameter tuning.

The mentorship program was a rewarding experience outside of simply working on my project and meeting with my mentors. Going to the coding dojos exposed me to paired/group programming, and the ChiPy mailing list has also pointed me to a lot of resources on software development, not all specific to Python either. It's made me realize that I really enjoy the problem solving and abstract thinking involved in programming, which gives me added confidence that making this career shift is the right decision. 
