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


##########################################################################
##########################################################################
###### Section for exploring by year

st.subheader('Explore trends for a single election year:')

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


## Define function for formatting histnorm argument options
def norm_label(arg):
    if arg==None:
        return 'Count'
    if arg=='percent':
        return 'Percent'


## Basic histogram for a single year
# Choose year to explore
bhist_year = st.radio(
    label='Year: ',
    options = [2012, 2016, 2020],
    index=2
)

# Choose column to group by/ investigate
bhist_col_opt = [
    'vote_method_4', 'vote_method_5', 'vote_bin', 
    'pri_vote_bin', 'birth_age_adj', 'gen_grp',
    'party_grp', 'gender_code', 'race_grp',
     'birth_reg_other', 'drivers_lic', 'city_grp'
]
bhist_group_col = st.selectbox(
    label='Group by: ',
    options = bhist_col_opt,
    index=0,
    format_func=format_col_names
)

# Choose raw count or percent
bhist_norm = st.radio(
    label='Display as: ',
    options = [None, 'percent'],
    index=0,
    format_func=norm_label
)


basic_histogram = basic_hist(
    gen_elecs_df, bhist_year, bhist_group_col, histnorm=bhist_norm
)
st.plotly_chart(basic_histogram, use_container_width=True)


## Grouped histogram for a single year
grp_histogram = grp_hist(gen_elecs_df, 2020, 'vote_method_4', 'party_grp')
st.plotly_chart(grp_histogram, use_container_width=True)

st.markdown('***')

##########################################################################
##########################################################################
###### Section for exploring year comparisons

st.subheader('Compare trends across election years:')

## Histogram grouped by election year
by_yr_histogram = grp_yr_hist(gen_elecs_df, 'vote_method_4')
st.plotly_chart(by_yr_histogram, use_container_width=True)


## Grouped histogram subplots per year 
all_yr_hist = multi_yr_hist(
    gen_elecs_df, 'vote_method_4', 'gen_grp',
    width=900, height=450
)
st.plotly_chart(all_yr_hist, use_container_width=False)