## Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

## Import functions created for visualizations
from plotly_year_functions import *

## Settings for app page
st.set_page_config(
    page_title='Union County Elections',
    layout='centered',
    initial_sidebar_state='auto'
)

## Set page title
st.title('Registered Voter Participation in Union County, North Carolina')

## Import DataFrames
gen_elecs_df = pd.read_csv('Data/UC_gen_elecs.gz')
elec_2020_df = gen_elecs_df.copy().loc[
    gen_elecs_df['year'] == 2020
]

## Define function for formatting column names as labels to choose from
def format_col_names(name):
    col_to_label = {
        'vote_method_4': 'Voting Method (4 categories)',
        'vote_method_5': 'Voting Method (5 categories)',
        'vote_bin': 'Voted (Y/N)',
        'pri_vote_bin': 'Voted in Primary (Y/N)',
        'birth_age_adj': 'Age',
        'gen_grp': 'Generation',
        'party_grp': 'Political Party',
        'gender_code': 'Gender',
        'race_grp': 'Race',
        'birth_reg_other': 'Birth Region',
        'drivers_lic': 'Drivers License (Y/N)',
        'city_grp': 'City',
        'year': 'Election Year'
    }
    
    return col_to_label[name]

## Define function for formatting categories as labels to choose from
def format_cat_names(name):
    cat_to_label = {
        'Rep': 'Republican',
        'Dem': 'Democrat',
        'Y': 'Yes',
        'N': 'No',
        'Boomer': 'Baby Boomer',
        'GenX': 'Generation X',
        'GenZ': 'Gen Z',
        'M': 'Male',
        'F': 'Female',
        'U': 'Undesignated',
        'Undesig.': 'Undesignated'
    }
    if name in cat_to_label.keys():
        return cat_to_label[name]

    else:
        return name


## Define function for formatting histnorm argument options
def norm_label(arg):
    if arg==None:
        return 'Count'
    if arg=='percent':
        return 'Percent'





##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Section for exploring by year
##########################################################################
##########################################################################

## Basic histogram for a single year
# Define container for section
single_yr_bas = st.beta_container()
single_yr_bas.header('Explore trends for a single election year:')
single_yr_bas.subheader('Explore one variable at a time:')
syb_col_1, syb_col_2 = single_yr_bas.beta_columns(2)

# Choose year to explore
bhist_year = syb_col_2.radio(
    label='Year: ',
    options = [2012, 2016, 2020],
    index=2,
    key='b_year'
)

# Choose column to group by/ investigate
bhist_col_opt = [
    'vote_method_4', 'vote_method_5', 'vote_bin', 
    'pri_vote_bin', 'birth_age_adj', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
     'birth_reg_other', 'drivers_lic', 'city_grp'
]
bhist_group_col = syb_col_1.selectbox(
    label='See the distribution of: ',
    options = bhist_col_opt,
    index=0,
    format_func=format_col_names,
    key='b_col'
)

# Plot basic histogram
syb_hist = basic_hist(
    gen_elecs_df, bhist_year, bhist_group_col
)
single_yr_bas.plotly_chart(syb_hist, use_container_width=True)

##########################################################################
## Basic pie chart for a single year

# Plot basic pie chart
syb_pie = basic_pie(
    gen_elecs_df,
     bhist_year,
      bhist_group_col,
      title=''
)
single_yr_bas.plotly_chart(syb_pie, use_container_width=True)

single_yr_bas.markdown('***')


##########################################################################
##########################################################################
##########################################################################
## Grouped histogram for a single year
# Define container for section
single_yr_grp = st.beta_container()
single_yr_grp.header('Explore trends for a single election year:')
single_yr_grp.subheader('Break down trends across 2 variables at a time:')
syg_col_1, syg_col_2 = single_yr_grp.beta_columns(2)

## Basic histogram for a single year
# Choose year to explore
ghist_year = syg_col_2.radio(
    label='Year: ',
    options = [2012, 2016, 2020],
    index=2,
    key='g_year'
)

# Choose 1st column to group by/ investigate
ghist_col_opt = [
    'vote_method_4', 'vote_method_5', 'vote_bin', 
    'pri_vote_bin', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
    'birth_reg_other', 'drivers_lic', 'city_grp'
]

vote_method_opts = [
    'vote_method_4', 'vote_method_5', 'vote_bin'
]

non_vote_method_opts = [
    'pri_vote_bin', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
    'birth_reg_other', 'drivers_lic', 'city_grp'
]

ghist_group_col_1 = syg_col_1.selectbox(
    label='Group by: ',
    options = ghist_col_opt,
    index=0,
    format_func=format_col_names,
    key='g_grp_col_1'
)

# Choose 2nd column to group by/ investigate
if ghist_group_col_1 in vote_method_opts:
    ghist_group_col_2 = syg_col_1.selectbox(
        label='Then by: ',
        options = non_vote_method_opts,
        index=2,
        format_func=format_col_names,
        key='g_grp_col_2'
    )

else: 
    ghist_group_col_2 = syg_col_1.selectbox(
            label='Then by: ',
            options = ghist_col_opt,
            index=0,
            format_func=format_col_names,
            key='g_grp_col_2'
        )


# Choose raw count or percent
ghist_norm = syg_col_2.radio(
    label='Display as: ',
    options = [None, 'percent'],
    index=0,
    format_func=norm_label,
    key='g_norm'
)

# Plot grouped histogram for a single year
syg_hist = grp_hist(
    gen_elecs_df, ghist_year,
    ghist_group_col_1,
    ghist_group_col_2,
    histnorm=ghist_norm
)
single_yr_grp.plotly_chart(syg_hist, use_container_width=True)


##########################################################################
## Grouped pie charts for a single year
# Define container for section
single_yr_grp_pie = st.beta_container()
sygp_col_1, sygp_col_2 = single_yr_grp_pie.beta_columns(2)


# Choose category from column 2 to investigate
for opt in ghist_col_opt:
    if ghist_group_col_2==opt:
        sgpie_col_cat_opt = gen_elecs_df.loc[gen_elecs_df['year']==ghist_year][ghist_group_col_2].unique()

sgpie_col_1_cat = sygp_col_1.selectbox(
    label='Choose category: ',
    options = sgpie_col_cat_opt,
    index=0,
    format_func=format_cat_names,
    key='gpie_cat'
)

# Plot basic pie chart
sygp_pie = grp_pie(
    gen_elecs_df,
     ghist_year,
     ghist_group_col_2,
      ghist_group_col_1,
      sgpie_col_1_cat
)
single_yr_grp_pie.plotly_chart(sygp_pie, use_container_width=True)


single_yr_grp_pie.markdown('***')


##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Section for exploring year comparisons
##########################################################################
##########################################################################

## Histogram grouped by election year
# Define container for section
grpby_yr = st.beta_container()
grpby_yr.header('Compare trends across election years:')
grpby_yr.subheader('Explore one variable at a time:')
gyr_col_1, gyr_col_2 = grpby_yr.beta_columns(2)


# Choose column to group by/ investigate
gyrhist_col_opt = [
    'vote_method_4', 'vote_method_5', 'vote_bin', 
    'pri_vote_bin', 'birth_age_adj', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
     'birth_reg_other', 'drivers_lic', 'city_grp'
]
gyrhist_group_col = gyr_col_1.selectbox(
    label='See the distribution of: ',
    options = gyrhist_col_opt,
    index=0,
    format_func=format_col_names,
    key='gyr_col'
)

# Choose raw count or percent
gyrhist_norm = gyr_col_2.radio(
    label='Display as: ',
    options = [None, 'percent'],
    index=0,
    format_func=norm_label,
    key='gyr_norm'
)

# Plot histogram grouped by election year
gyr_hist = grp_yr_hist(
    gen_elecs_df,
     gyrhist_group_col,
      histnorm=gyrhist_norm
)
grpby_yr.plotly_chart(gyr_hist, use_container_width=True)


grpby_yr.markdown('***')

##########################################################################
##########################################################################
##########################################################################
## Grouped histogram subplots per year 
# Define container for section
multi_yr = st.beta_container()
multi_yr.header('Compare trends across election years:')
multi_yr.subheader('Break down trends across 2 variables at a time:')
myr_col_1, myr_col_2 = multi_yr.beta_columns(2)


# Choose 1st column to group by/ investigate
myrhist_col_opt = [
    'vote_method_4', 'vote_method_5', 'vote_bin', 
    'pri_vote_bin', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
    'birth_reg_other', 'drivers_lic', 'city_grp'
]

vote_method_opts = [
    'vote_method_4', 'vote_method_5', 'vote_bin'
]

non_vote_method_opts = [
    'pri_vote_bin', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
    'birth_reg_other', 'drivers_lic', 'city_grp'
]

myrhist_group_col_1 = myr_col_1.selectbox(
    label='Group by: ',
    options = myrhist_col_opt,
    index=0,
    format_func=format_col_names,
    key='m_grp_col_1'
)

# Choose 2nd column to group by/ investigate
if myrhist_group_col_1 in vote_method_opts:
    myrhist_group_col_2 = myr_col_1.selectbox(
        label='Then by: ',
        options = non_vote_method_opts,
        index=3,
        format_func=format_col_names,
        key='m_grp_col_2'
    )

else: 
    myrhist_group_col_2 = myr_col_1.selectbox(
            label='Then by: ',
            options = myrhist_col_opt,
            index=1,
            format_func=format_col_names,
            key='m_grp_col_2'
        )


# Choose raw count or percent
myrhist_norm = myr_col_2.radio(
    label='Display as: ',
    options = [None, 'percent'],
    index=0,
    format_func=norm_label,
    key='myr_norm'
)


# Grouped histogram subplots for each election year
myr_hist = multi_yr_hist(
    gen_elecs_df, 
    myrhist_group_col_1, 
    myrhist_group_col_2,
    histnorm=myrhist_norm,
    width=900, height=450
)
multi_yr.plotly_chart(myr_hist, use_container_width=False)

##########################################################################
## Grouped pie charts for each year
# Define container for section
multi_yr_grp_pie = st.beta_container()
mygp_col_1, mygp_col_2 = multi_yr_grp_pie.beta_columns(2)


# Choose category from column 2 to investigate
for opt in myrhist_col_opt:
    if myrhist_group_col_2==opt:
        mygpie_col_cat_opt = gen_elecs_df[myrhist_group_col_2].unique()

mygpie_col_1_cat = mygp_col_1.selectbox(
    label='Choose category: ',
    options = mygpie_col_cat_opt,
    index=0,
    format_func=format_cat_names,
    key='mygpie_cat'
)

# Plot basic pie chart
mygp_pie = multi_grp_pie(
    gen_elecs_df,
     myrhist_group_col_2,
      myrhist_group_col_1,
      mygpie_col_1_cat
)
multi_yr_grp_pie.plotly_chart(mygp_pie, use_container_width=False)