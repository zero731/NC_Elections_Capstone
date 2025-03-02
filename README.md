# Registered Voter Participation in Union County, North Carolina
### Author: Max Steele
##### Project Dashboard: <a href="https://share.streamlit.io/zero731/nc_elections_capstone/main/UC_elec_app.py"> Union County Registered Voter Data</a>
---

## Abstract
The 2020 general election saw many key battleground states with extremely close margins for races at virtually every level of the ballot. Several battleground states flipped from red in 2016 to blue in 2020. However, North Carolina was one battleground state that remained red in the 2020 general election, awarding its electoral votes to the Republican candidate, despite re-electing a Democratic governor. Increased turnout of early voters and mail-in ballots in 2020 seemed promising for Democratic candidates, but in many cases they fell short of victory. With political races being decided by a slim margin, it is important to understand who is voting, and who is failing to turnout. Equipped with this information, local Democratic leaders can begin the targeted work of increasing turnout for their candidates in future elections. 
 
To address this problem, I built a dashboard for exploring trends in registered voter participation in Union County, NC in the 2012, 2016, and 2020 general elections. I also built classification models for each year to investigate which demographic features from voter registration data were most predictive of whether an individual voted in Union County. The best models for 2012, 2016, and 2020 achieved an accuracy of 66%, 69%, and 66%, respectively. Across all three election years, age group, birth region, political party, and possession of a driver's license emerged as top predictors of registered voter participation.
 
Overall, it was relatively difficult to predict whether a registered voter would cast a ballot based on information in their voter registration record. Model performance may be improved if voter registration records could be supplemented with information such as education and income level. However, model performance was better than guessing, and training models on voter registration and history data that is freely available highlighted important trends within and between elections.<br>
 

---

## Introduction
The 2020 general election saw many key <a href="https://www.cnn.com/election/2020/results/president"> battleground states</a> with extremely close margins for not only the presidential race, but for races at virtually every level of the ballot. This resulted in recounts in several states and Senate runoff elections in Georgia. We also witnessed the <a href="https://www.washingtonpost.com/graphics/2020/elections/voter-turnout/">highest voter turnout in over a century</a>, with 2/3 of every American elligible to vote casting a ballot.

Many of the battleground states flipped from red to blue during the 2020 election in the midst of this massive voter turnout. However, my home state of North Carolina was not one of them, even though enough voters split their ticket to re-elect a Democratic governor. The 2020 election saw above average <a href="https://www.statista.com/statistics/1184621/presidential-election-voter-turnout-rate-state/"> voter turnout in NC</a> as compared to the country as a whole, with 71.5% of eligible North Carolinians showing up at the polls. In the last 3 presidential elections, North Carolina has made the list of <a href="https://www.cnn.com/2020/11/09/politics/2020-election-trump-biden-closest-states/index.html"> top 10 states</a> with the closest margin. This was also reflected at the state level in 2020, with one <a href="https://ballotpedia.org/North_Carolina_Supreme_Court_elections,_2020"> NC Supreme Court race</a> being decided by a margin of just 412 votes after a recount. When political races are as close as we saw in the 2020 general election, absolutely every vote counts. Thus, it is important to understand who is voting, and who is failing to turnout to the polls.

This project focuses on examining trends in voter turnout in the 2012, 2016, and 2020 elections in Union County, NC. As part of this project, I created a Streamlit dashboard that allows for interactive exploration of these trends and comparison across elections. The dashboard can be found <a href="https://share.streamlit.io/zero731/nc_elections_capstone/main/UC_elec_app.py"> here</a>.

I combined information from NC voter registration records with records of each registered individual's voting history, and built models to predict whether or not an individual participated (Vote vs. No Vote) and what voting method they used (Early, Election Day, or No Vote), with separate models for each year. I intend to scale up to examining statewide trends once finalized voter history records have been released for the 2020 general election for every county in North Carolina.<br><br>


---

## Data
The data used for this project were obtained from the North Carolina State Board of Elections (NCSBE). Both <a href="https://www.ncsbe.gov/results-data/voter-registration-data"> voter registration records</a> and <a href="https://www.ncsbe.gov/results-data/voter-history-data"> voter history records</a> are made available and updated weekly. Voter history records do not contain demographic information, but the two files can be merged according to a unique ID (`ncid`) assigned to each registered voter in the state of North Carolina.<br><br>


---

## Methods
### Preparing Data for Modeling
In the <a href="https://github.com/zero731/NC_Elections_Capstone/blob/main/Final_Part_I_Merge_Scrub_UC_Data.ipynb"> Part I</a> notebook of my project, I merged the two files (the data used for the current version of this project obtained from the NCSBE site on January 4, 2021) to obtain a single dataframe containing both demographic and vote history information for each registered voter in Union County.

The major steps I took in cleaning and preparing the data for modelling and visualization were as follows:
1. **Drop duplicate records from voter history records.** This included identical duplicates and records/ rows that were not completely identical, but shared the same combination of `ncid` (unique voter ID) and `election_desc` (the specific election for which the voter cast a ballot). Each `ncid` should only show up in a given election once, since each voter gets a single vote.<br>

2. **Drop voter registration records for individuals with "Removed" or "Denied" status.** These individuals are currently (as of January 4) ineligible to vote within Union County. Because the records do not indicate when their status was changed, I could not account for the fact that they may have been elligible to vote in either the 2012 or 2016 election. Thus the dataframes for those elections may be missing individuals who were elligible to vote then, but not in 2020.<br>

3. **Merge cleaned voter history data onto cleaned voter registration data on `ncid`.**<br>

4. **Create a separate dataframe for each election (general 2012, 2016, and 2020).** Individuals were excluded from an election dataframe for a given year if they were not registered in time to vote in that election, or if they were too young to vote that year. This left one record per elligible, registered individual in each dataset, even if they did not cast a vote in that particular year.<br><br>


After creating a separate dataframe for each election, I explored the data and ultimately prepared each dataset for modeling in a consistent manner to enable direct comparisons. This was done in the <a href="https://github.com/zero731/NC_Elections_Capstone/blob/main/Final_Part_II_Clean_Explore_UC_Elecs.ipynb"> Part II</a> notebook.


Since most of the demographic information is required for voter registration records, there were not many null values to deal with. For variables that were used as model predictors, missing information became its own category.
Several features included rare labels (categories that made up less than 5% of the total population). Rare labels were combined into a single 'Other' category. This was distinct from the 'Missing' category.


<br>

### Modeling
All models were built using the following predictive features:
 - **Generation** (`gen_grp`) - Based on birth year: Gen Z, Millennial, Generation X, Baby Boomer, Greatest-Silent (combined the two oldest generations together) <br>

 - **Political Party** (`party_grp`) - Democrat, Republican, or Other (includes voters registered as unaffiliated, Libertarian, Green, or Constitution) <br>

 - **Race** (`race_grp`) - Black, White, Undesignated, or Other (includes voters that identify with 2 or more racial groups, Asian, Native American, Pacific Islander, or other groups) <br>

 - **Gender** (`gender_code`) - Female, Male, or Undesignated <br>

 - **Birth Region** (`birth_reg_other`) - Broken into U.S. Census regions (South, Northeast, Midwest, West), Missing, and other (including U.S. territories and citizens born outside the U.S.) <br>

 - **Drivers License** (`drivers_lic`) - Whether or not the person possesses a drivers license <br>

 - **City** (`city_grp`) - Cities within Union County: Monroe, Matthews, Waxhaw, Indian Trail, Other (includes all other cities/ towns within the county) <br>


For each of the three election years, I modeled voter participation as both a binary target (Vote vs. No vote) and as a multiclass target (Early, Election Day, or No Vote). I trained additional binary target models on a dataset that combined all three election years.
When training both binary and multiclass models, I tried both Random Forest Classifiers (scikit-learn), and XGboost Classifiers (xgboost). 

For binary target models I tried Random Forest Classifiers with and without SMOTE to oversample the minority "No Vote" class and XGBoost Classifiers with and without addressing class imbalance with the `scale_pos_weight` hyperparameter.

For multiclass target models, I again tried Random Forest Classifiers with and without SMOTE, and then tested XGBoost classifiers with and without SMOTE.

Each election dataset was split into a training and test set. Binary and multiclass target models for the same year were trained using the same train-test split of the data. Models were trained, then tested, with predictive performance evaluated on the test set. The best models were chosen based on balanced accuracy between or among the target classes while attempting to maximize recall of the "No Vote" class.<br><br>

---

## Results
The best models for each election year, as well as the multi-year model, are presented and interpreted in the <a href="https://github.com/zero731/NC_Elections_Capstone/blob/main/Final_Part_III_Model_Interpret_UC_Elecs.ipynb"> Part III</a> notebook.

**Summary of model performance across election years:**
- Random Forest Classifiers and XGBoost Classifiers performed relatively similary for all years, but XGBoost tended to result in slightly higher overall accuracy across classes.
- Addressing class imbalances either via SMOTE or by making use of XGBoost's `scale_pos_weight` hyperparameter was necessary to improve the performance of all models.
- Across years, binary target model accuracy maxed out around 69% overall accuracy and the best multiclass models maxed out at around 50% overall accuracy.

Below are the confusion matrix and ROC-AUC curve for the best binary target model for the 2020 general election. The classifier had and overall accuracy of 66% when making predictions on the test set. Performance was nearly identical for the best 2012 and 2016 models.

![](/Figures/model_evals/best_2020_bin_eval.png)



Once the best models were selected, the relationships of the top predictive features with the target variable were interpreted using SHAP (SHapley Additive exPlanations). Below is a summary plot of the SHAP values for the best binary model for the 2020 general election. The most important features for predicting voter participation (Vote vs. No Vote) are ranked in descending order, with the top predictive features having the largest absolute SHAP values (longer bars).

![](/Figures/shap/2020_bin_shap_summ_bar.png)


Across all three election years, age group (generation, `gen_grp`), birth region (`birth_reg_other`), political party (`party_grp`), and possession of a drivers license (`drivers_lic`) emerged as some of the top predictors of registered voter participation. Interestingly, possession of a drivers license was not one of the top predictors when all three election years were combined to train a single model. The direction of each predictor's effect was interpreted using SHAP summary and force plots like those shown below for the same 2020 target model.

![](/Figures/shap/2020_bin_shap_summ.png)

This force plot breaks down which factors the model used to correctly predict that the voter represented by the third row of the training set did cast a vote in the 2020 election.

![](/Figures/shap/shap_force_2020_idx3.png)

In the case above, the model was pushed towards the prediction of "Vote" (1) by the fact that the voter's birth region information was missing, they belong to the Baby Boomer generation (and thus are not a millenial), and they have a drivers license. The fact the this person is not a Republican pushed the model in the incorrect direction towards "No Vote" (0), but not enough to overwhelm the factors more predictive of "Vote" (1). This example is characteristic of how the top predictive features influenced model predictions for all three election years.



### Age
Across all three general election years, age group (in the form of the categorical variable `gen_grp`) was one of the mostly highly predictive features of whether or not a registered voter actually cast a ballot in the election. Millennials consistently emerged as the least likely to vote in each election in Union County. No one belonging to Gen Z was old enough to register to vote in the 2012 election, and this generation made up a very small portion of those eligible to vote in 2016 and 2020. However, it appears that Gen Z is behaving similarly to Millennials in Union County and failing to turn out at the polls as consistently as Generation X and Baby Boomers do. 

![](/Figures/plotly_explore/vote_bin_by_gen_multi_yr.png)


### Birth Region
Across all three general election years, the fact that a registered voter's birth region information (U.S. state or territory or out of country) was missing emerged as a useful predictor. The other categories for birth region were not as useful as the 'Missing' category. Compared to the other categories, 'Missing' birth region is the only group with a substantially higher proportion of its members turning out to vote than not.

![](/Figures/plotly_explore/birth_reg_by_vote_bin_multi_yr.png)



### Political Party
Across all three general election years, whether or not someone was registered as a Republican emerged as a top predictive feature of participation in the election. Republicans in Union County appear to be more likely to vote than not, whereas voters that registered as unaffiliated or as members of the Libertarian, Green, or Constitution party are less likely to vote. These 'Other' voters appear to be making up an increasing portion of registered non-voters as time has passed. The participation by Union County Democrats in the past three general elections appears to be less consistent.

![](/Figures/plotly_explore/party_by_vote_bin_multi_yr.png)



### Drivers License
Voters that do not possess a drivers license make up a relatively small portion of the registered voter population (<10%). This may be due in part to perceived barriers to registering without this form of ID. People may be less likely to register to vote if they feel that not having a photo ID will make it more difificult for them when it comes time to actually cast a ballot. <br>
A valid drivers license/ photo ID was not required to vote in the 2020 election. However, the issue of requiring a photo ID to vote in elections in North Carolina has been a source of confusion and frustration due to a voter ID law passed in 2018 and blocked from taking effect in early 2019. People without drivers licenses tended to be less likely to vote across all 3 election years.

![](/Figures/plotly_explore/drivers_lic_by_vote_bin_multi_yr.png)<br><br>

---

## Conclusions/ Recommendations
Overall, it was relatively difficult to predict whether or not a registered voter in Union County would cast a ballot based on information in their voter registration record. This was true for 2012, 2016, 2020, and when all three elections were combined into a single model. Model performance may be improved if voter registration and history records could be supplemented with information such as education and income level. However, this type of information is not readily available in a way that can be connected to individual voters. Even so, training models on the voter registration and voter history data that is freely available did highlight important trends within and between years and raise some interesting questions. 

Union County, North Carolina has trended increasingly red over the past several years. Like many other battleground states, it is mainly the more populous metro areas such as Mecklenburg and Wake County in NC that allow for the potential to flip from red to blue. With elections as close as they were in 2020, it's extremely important to get people to the polls and to understand why they don't turnout. Increased turnout of early voters and a dramatic increase in mail-in ballots for the 2020 election seemed promising for Democratic candidates, but in many cases Democratic candidates fell short of victory, even if only by a few hundred votes the closest races. 

As Democrats in North Carolina seek to increase turnout for their candidates in future elections, here are my recommendations specific to Union County:

 - Focus on getting Gen Z and millennials to the polls. Many of them are registered, which isn't surprising given that it's something you can do online, but around a third of those who are registered are not bothering to show up and vote. 

- Investigate why individuals whose voter registration is missing birth region information are so much more likely to vote. Why is the information missing and what makes these voters different? Is this a demographic that is more likely to vote a certain way? Originally I thought that maybe people who were born out of the country would be more likely to not disclose this information, especially given the recent political climate. On the other hand, it seems like naturalized citizens would likely be required to provide more thorough documentation. Perhaps there is some relationship between a tendency to skip over providing non-required information or how and when someone registers and whether or not someone votes.

- Ensure that voters stay very clearly informed about voter ID laws as they change. People who do not possess drivers licenses often belong to low income and/or minority groups that tend to lean Democratic. Make sure they know their rights and look into providing people with transportation to and from the polls. This may be especially important in areas like Union County which have very few options for public transit.

- Continue making efforts to appeal to voters that do not align with one of the two major parties. These voters continue to make up an increasing proportion of registered voters in Union County.<br><br>

---

## Future Work

Currently my plans for future work with this project include:
 - Scaling up to a statewide analysis once all North Carolina counties have finalized their voter history records and statistics for the 2020 general election.
 - Further investigating the interaction effects among demographic features for each election year in Union County.
 - Adding the following sections to my Union County registered voters dashboard:
    - A section to explore trends in voter registration status (Active, Removed, Denied, Inactive).
    - A section to compare the current registered voter population to the most recent U.S. Census data for Union County.