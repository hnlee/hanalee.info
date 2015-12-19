Title: Notes on "Lessons from 2MM machine learning models"
Date: 2015-11-03
Modified:
Category: blog
Tags: data science, kaggle, talks
Author: Hana Lee
Summary: My notes on a talk given by Kaggle's founder, Anthony Goldbloom, on 2 Nov 2015 at the Blue 1647 Innovation Center.

Not a comprehensive outline of the talk, just a list of points that I found interesting.

- During the timeline of a competition, scores reach a plateau or floor where subsequent increases in accuracy are minimal
    - The "four-minute mile" phenomenon: when someone makes a breakthrough that dramatically pushes past a plateau, it is immediately replicated by others
    - Otherwise the floor represents the limits of the signal in the dataset
    - Usually the floor is reached unless there is too much noise or not enough signal in the dataset
- Neural networks are dominating in any competition involving images, speech, or text
- Two approaches to winning
    - Creative feature engineering: make plots, test many different combinations of features, use version control to keep track
        - E.g. used car competition, where winning model depended on the crucial feature of unusual car colors vs. standard car colors
    - Parameter tuning: usually only gets incremental improvements in score
- [XGBoost](https://github.com/dmlc/xgboost) (variant on gradient boosting) also dominating in competitions
- To guard against overfitting, final scoring of submissions uses completely new test data
    - Overfitting is the most common issue in supervised learning problems
    - Phenomenon where someone high up on leaderboard drops a hundred places after final scoring
    - Can guard against overfitting by ignoring feedback from parameter tuning unless score improves above standard error
- How are test sets generated?
    - Out-of-time sampling
    - Out-of-sample sampling
    - Stratified sampling (if one of the classes being predicted is very rare in the dataset)
- Boundaries between different types of problems: which ones suited for neural network approachvs XGBoost/random forests/etc. approach?
    - Unstructured data for former, very structured data for latter
    - What about in-between cases? e.g. EEG data for grasping vs lifting: time series data where neural networks won
- Any way to automate feature engineering? - a hard problem...
- Optimizing behavior in response to machine learning results? - also a hard problem...
- [Kaggle Scripts](https://www.kaggle.com/scripts) as a learning resource, "Github for data science"
- Properties of Kaggle winners: good coders, careful use of version control, coding best practices, tenacity 
