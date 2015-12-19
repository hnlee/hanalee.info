Title: ChiPy Mentorship: Progress
Date: 2015-12-07
Modified:
Category: blog
Tags: chipy, python, data science, kaggle
Author: Hana Lee
Summary: What I've accomplished so far.

To recap, my main objective for the ChiPy mentorship program is to work on the [San Francisco crime classification](https://www.kaggle.com/c/sf-crime) Kaggle competition. I've made the Jupyter/iPython notebook I am using for analysis available [on Github](https://github.com/hnlee/sfcrimes/blob/master/sfcrimes.ipynb).

This particular data set is very simple, consisting only of eight features aside from the target, which corresponds to the category of crime. I began with some exploratory data analysis, looking at the frequency of crimes across different categories, police districts, and days of the week. I also took a look at the distribution of crimes across longitude and latitude, which revealed some extreme outliers, likely to be the result of mistakes in data entry.

Kaggle evaluates submissions based on the [log-loss metric](https://en.wikipedia.org/wiki/Loss_functions_for_classification#Logistic_loss) and require you to predict probabilities for each class of crime category on every row in the test set. Thus, the very simplest model would simply be the average frequency of each crime category. I split the training data into internal training and test sets for quick cross-validation and fit the model by calculating the means on the internal training set. The performance of this model is actually not too shabby, with a log-loss score of 5.46035 on the internal test set.

The next simplest model was to use a single categorical variable, that of police district, as a predictor. After transforming this column into dummy variables, I fitted a logistic regression model to the internal training set. This model performed even better, with a log-loss score of 2.61714 on the internal test set. I then used this model to generate predictions on the test data from Kaggle and made a submission, just as a practice run. My initial position on the leaderboards at the time of submission was at a pretty abysmal 476th place. (I've slipped even further in the standings since then!) But my score on Kaggle's test set was 2.61626, which is not very far off from the current top score on the leaderboard at 2.06702. That implies that I'm already very close to the limits of the signal in the dataset...assuming of course that there isn't some undiscovered breakthrough that hasn't occurred to anyone in the Kaggle community yet.

Still, I suspected that more sophisticated machine learning methods could perform better, however incrementally, than my univariate logistic regression. As a next step, I incorporated the day of the week as another categorical variable into the logistic regression model. However, this feature did not appear to contribute very much, as my log-loss score from the internal test set was only 2.61416.

I turned to random forests, a popular ensemble learning method that is based on decision trees. I also set up five-fold cross-validation (more robust than a single split into training and test). Using police districts and the day of the week again, random forests did not seem to perform any better than logistic regression, with a mean log-loss score of 2.61821 across the five folds.

I spent last Sunday discussing what to do next with my mentor, and I plan to work on the following over the next couple of weeks:

1. __"Hacking" the score:__ Since performance is measured via log-loss, there's an extreme penalty for predicting any crime category probability as zero. Adding a minimal constant and renormalizing before submitting the probabilities matrix should help avoid this situation.
2. __Feature engineering:__ Try to harness what signal is remaining in the other variables, such as extracting the month or time of day from the date column. (Time of day could be even be binned into categories like morning, afternoon, and night.) Given the usefulness of the police district column, the higher-resolution geographic data in the latitude and longitude columns may prove to perform even better, although it would require some initial cleaning and may need to be processed via clustering first.
3. __Gradient boosting:__ Random forests is basically a [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating) method. Another major category of ensemble learning algorithms is [boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)), which in the form of `XGBoost` ([eXtreme Gradient Boosting](https://github.com/dmlc/xgboost)) has been one of the most successful methods on Kaggle. Since it is fundamentally a different approach to combining multiple machine learning models, it should be worth trying.
4. __"Meta-learning":__ Going one step up from ensemble learning by running multiple methods and averaging their results. (The results can also be combined in more sophisticated ways, obviously, e.g. weighting the methods based on their respective performance.)

As a side note, going from R to Python with `numpy` and `pandas` has made me think that there really ought to be a website that allows you to search an R function and find the equivalent in Python. I've spent a lot of time muttering to myself things like, "How do I `cbind()`? How do I `colSums()`? What's `table()` in `pandas`?"  (If there is such a website, let me know!)
