## Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


## Import DataFrames
gen_elecs_df = pd.read_csv('Data/UC_gen_elecs.gz')





##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Define functions used for widgets
##########################################################################
##########################################################################


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
###### Define and cache functions used to produce visualizations
##########################################################################
##########################################################################


#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def basic_hist(df, year, col, title=None,
                  template='seaborn', save=False, fig_name=None):
    """Takes a DataFrame with a year column, filters the DataFrame to the
        provided election year, and returns a color-coded Plotly histogram 
        for the provided column.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        col (str): Name of the df column for which to plot histogram
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'Distribution of labels[{col}] in {year} General Election'.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Returns Plotly histogram of provided column for the specified year.
    """    


    fig_filepath = 'Figures/'

    title_font_dict = {
        'family':'Arial Black',
        'size':24
    }
    
    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    ax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }

    
    cat_orders = {}
    labels = {}
    
    if col == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})
    
    
    if col == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})
    
    
    if col == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})
        
    
    if col == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})
        
        
    if col == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})
        
    
    
    if col == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})
    
            
    if col == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})
    
    
    if col == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})
        
        
    if col == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})
    
    
    if col == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
        cat_orders.update(
            {
                'drivers_lic': [
                    'License',
                    'No License'
                ]
            }
            )
        labels.update({'drivers_lic': 'Drivers License'})
        
    
    if col == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})
        


    filtered_df = df.loc[df['year']==int(year)]    
    
    if col == 'birth_age_adj':
        labels.update({'birth_age_adj': 'Age'})
        fig = px.histogram(filtered_df, x=col,
                           title='Distribution of {} <br> in {} General Election'.format(
                           labels[col], str(year)
                           ), 
                           color_discrete_sequence=['dodgerblue'],
                           category_orders=cat_orders,
                           labels=labels,
                           template=template,
                           nbins=50
                      )
        
    
    else:
        fig = px.histogram(filtered_df, x=col, color=col,
                           color_discrete_map=color_map,
                           title='Distribution of {} <br> in {} General Election'.format(
                           labels[col], str(year)
                           ),
                           category_orders=cat_orders,
                           labels=labels,
                           template=template
                          )
    

    fig.update_layout(
        title_font=title_font_dict,
        showlegend=False
        )

    fig.update_yaxes(
        title='Number of Registered Voters',
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )
    

    if save:
        fig.write_html(fig_filepath+fig_name+'.html')
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def grp_hist(df, year, group_col_1, group_col_2, title=None,
             barmode='group', histnorm=None,
             template='seaborn', save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first
        column specified, then color-codes by the second provided column
        to create a Plotly histogram for the specified election year.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the histograms
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'labels[{group_col_1}] by labels[{group_col_2}] in {year} General Election'.
        barmode (str, optional): Plotly barmode parameter. Defaults to 'group'.
        histnorm (str, optional): Plotly histnorm parameter, but only takes None or 'percent'.
             Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly histogram grouped by group_col_1 and color-coded
            according to group_col_2 for the specified election year. 
    """    


    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        }
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        },
        'title': ''
    }

    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    ax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }


    cat_orders = {}
    labels = {}


    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})


    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})


    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})


    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})


    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})


    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})


    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})


    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})


    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})


    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['License', 'No License']})
        labels.update({'drivers_lic': 'Drivers License'})


    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})



    filtered_df = df.loc[df['year']==int(year)] 

    fig = px.histogram(filtered_df, x=group_col_1, color=group_col_2,
                       color_discrete_map=color_map, barmode=barmode, 
                       title='{} by {} <br> in {} General Election'.format(
                           labels[group_col_1],
                           labels[group_col_2],
                           str(year)
                           ), 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template,
                           histnorm=histnorm
                      )
    if histnorm=='percent':
        fig.update_yaxes(title='Percent of Registered Voters')
        
    if histnorm==None:
        fig.update_yaxes(title='Number of Registered Voters')
    

    fig.update_layout(
        title=title_dict,
        legend = leg_dict
        )

    fig.update_yaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def stack_grp_hist(df, year, group_col_1, group_col_2, title=None, 
                   percent=None, template='seaborn',
                   save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first
        column specified, then color-codes by the second provided column
        to create a stacked Plotly bar chart for the specified election year.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the histograms
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'labels[{group_col_1}] by labels[{group_col_2}] in {year} General Election'.
        barmode (str, optional): Plotly barmode parameter. Defaults to 'group'.
        histnorm (str, optional): Plotly histnorm parameter, but only takes None or 'percent'.
             Defaults to None.
        percent (str, optional): If 'percent', plots bars as percentages.
            If None, plots as raw counts. Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        save (bool, optional): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly stacked bar chart grouped by group_col_1 and color-coded
            according to group_col_2 for the specified election year. 
    """    


    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        }
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        },
        'title': ''
    }

    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    ax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }


    cat_orders = {}
    labels = {}


    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})


    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})


    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})


    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})


    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})


    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})


    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})


    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})


    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})


    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['License', 'No License']})
        labels.update({'drivers_lic': 'Drivers License'})


    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})



    filtered_df = df.loc[df['year']==int(year)].copy() 
    
    df_slice = filtered_df[[group_col_1, group_col_2, 'year']]
    grpby_slice = df_slice.groupby([group_col_1, group_col_2]).count()
    grpby_slice.reset_index(inplace=True)
    grpby_slice.rename(columns={'year':'Count'}, inplace=True)
    
    total_count_slice = df_slice.drop(
        columns=['year']
    ).groupby([group_col_1]).count()
    
    total_count_slice.reset_index(inplace=True)
    total_count_slice.rename(columns={group_col_2:'Total'}, inplace=True)
    
    merge_slice = grpby_slice.merge(total_count_slice, on=group_col_1)
    merge_slice['Percent'] = round(
        (merge_slice['Count'] / merge_slice['Total'])*100, 2
    )

    if percent:
        fig = px.bar(merge_slice, x=group_col_1, y='Percent',
                           color=group_col_2, color_discrete_map=color_map, 
                           title='{} by {} <br> in {} General Election'.format(
                               labels[group_col_1],
                               labels[group_col_2],
                               str(year)
                               ), 
                           category_orders=cat_orders,
                           labels=labels,
                           template=template
                          )
        fig.update_yaxes(title='Percent of Registered Voters')
    
    
    
    else:
        fig = px.bar(merge_slice, x=group_col_1, y='Count',
                           color=group_col_2, color_discrete_map=color_map, 
                           title='{} by {} <br> in {} General Election'.format(
                               labels[group_col_1],
                               labels[group_col_2],
                               str(year)
                               ), 
                           category_orders=cat_orders,
                           labels=labels,
                           template=template
                          )
        fig.update_yaxes(title='Number of Registered Voters')
    

    fig.update_layout(
        title=title_dict,
        legend = leg_dict
        )

    fig.update_yaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def grp_yr_hist(df, group_col_1, title=None, barmode='group',
                histnorm=None, template='seaborn', save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first
        group_col_1, then color-codes by election year to create a Plotly histogram.

    Args:
        df (DataFrame): A Pandas DataFrame
        group_col_1 (str): Name of the df column by which to group
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'labels[{group_col_1}] by Election Year'.
        barmode (str, optional): Plotly barmode parameter. Defaults to 'group'.
        histnorm (str, optional): Plotly histnorm parameter, but only takes None or 'percent'.
             Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly histogram grouped by group_col_1 and color-coded
            according to group_col_2 for the specified election year. 
    """    


    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'y': 0.85
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        },
        'title': ''
    }

    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    ax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }



    cat_orders = {'year': [2012,2016,2020]}
    labels = {'year': 'Election Year'}

    color_map = {
            2012: 'darkviolet',
            2016: 'limegreen',
            2020: 'orangered'
        }

    if group_col_1 == 'gen_grp':
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})


    if group_col_1 == 'party_grp':
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})


    if group_col_1 == 'vote_method_4':
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})


    if group_col_1 == 'vote_method_5':
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})


    if group_col_1 == 'vote_bin':
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})


    if group_col_1 == 'pri_vote_bin':
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})


    if group_col_1 == 'race_grp':
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})


    if group_col_1 == 'gender_code':
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})


    if group_col_1 == 'birth_reg_other':
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})


    if group_col_1 == 'drivers_lic':
        cat_orders.update(
            {
                'drivers_lic': [
                    'License',
                    'No License'
                ]
            }
        )
        labels.update({'drivers_lic': 'Drivers License'})


    if group_col_1 == 'city_grp':
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})


    if group_col_1 == 'birth_age_adj':
        labels.update({'birth_age_adj': 'Age'})
        fig = px.histogram(df, x=group_col_1, color='year',
                       color_discrete_map=color_map, barmode=barmode, 
                       title='{} by {}'.format(
                               labels[group_col_1], labels['year']
                           ), 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template,
                       histnorm=histnorm,
                       nbins=50
                      )


    else:
        fig = px.histogram(df, x=group_col_1, color='year',
                       color_discrete_map=color_map, barmode=barmode, 
                       title='{} by {}'.format(
                               labels[group_col_1], labels['year']
                           ), 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template,
                       histnorm=histnorm
                      )
    
    if histnorm=='percent':
        fig.update_yaxes(title='Percent of Registered Voters')
        
    if histnorm==None:
        fig.update_yaxes(title='Number of Registered Voters')

    fig.update_layout(
        title=title_dict,
        legend=leg_dict
        )

    fig.update_yaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=ax_tick_font_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def multi_yr_hist(df, group_col_1, group_col_2,
                  facet_feat='year', facet_spacing=0.05,
                  title=None, barmode='group', histnorm=None,
                  template='seaborn', width=1000, height=450,
                  save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first
        column specified, then color-codes by the second provided column
        to create a Plotly histogram subplot for each election year.

    Args:
        df (DataFrame): A Pandas DataFrame
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the histograms
        facet_feat (str, optional): Name of column for which to create subplots.
             Defaults to 'year'.
        facet_spacing (float, optional): Spacing parameter for Plotly subplots.
             Defaults to 0.05.
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'labels[{group_col_1}] by labels[{group_col_2}] General Elections'.
        barmode (str, optional): Plotly barmode parameter. Defaults to 'group'.
        histnorm (str, optional): Plotly histnorm parameter, but only takes None or 'percent'.
             Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        width (int, optional): Width of figure. Defaults to 1000.
        height (int, optional): Height of figure. Defaults to 450.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly histograms grouped by group_col_1 and color-coded
            according to group_col_2, with one plot for each year. 
    """    


    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'yref':'container',
        'y':0.92
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        },
        'title': ''
    }

    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    xax_tick_font_dict = {
        'family':'Arial Black',
        'size':13
    }

    yax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }

    ann_dict = {
        'font': {
            'family':'Arial Black',
        'size': 18
        },
        'yref':'paper',
        'y':0.99
    }


    cat_orders = {'year': [2012, 2016, 2020]}
    labels = {}
    
    
    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})
    
    
    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})
    
    
    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})
        
        
    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})
    
    
    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})

    
    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})
    
        
    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})
    
    
    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})
        
        
    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})
    
    
    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['License', 'No License']})
        labels.update({'drivers_lic': 'Drivers License'})
        
    
    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})
    
    
    fig = px.histogram(df, x=group_col_1, color=group_col_2,
                           color_discrete_map=color_map, barmode=barmode, 
                           title='{} by {} in General Elections'.format(
                               labels[group_col_1], labels[group_col_2]
                           ), 
                           facet_col=facet_feat,
                           category_orders=cat_orders,
                           labels=labels,
                           histnorm=histnorm,
                           template=template,
                           width=width, height=height,
                           facet_col_spacing=facet_spacing
                      )
        
    if histnorm=='percent':
        fig.update_yaxes(title='Percent of Registered Voters')
        
    if histnorm==None:
        fig.update_yaxes(title='Number of Registered Voters')
    
    fig.update_yaxes(title_text='',row=1, col=2)
    fig.update_yaxes(title_text='',row=1, col=3)

    fig.update_xaxes(title_text='',row=1, col=1)
    fig.update_xaxes(title_text='',row=1, col=3)

    fig.update_layout(
        title=title_dict,
        legend=leg_dict
        )

    fig.update_yaxes(
        title_font=ax_title_font_dict,
        tickfont=yax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=xax_tick_font_dict
    )

    fig.for_each_annotation(
        lambda x: x.update(text=x.text.split("=")[-1])
    )

    fig.update_annotations(
        ann_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')

    return fig


    
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def stack_multi_yr_hist(df, group_col_1, group_col_2,
                        facet_feat='year', facet_spacing=0.05,
                        title=None, percent=None,
                        template='seaborn', width=1000, height=450,
                        save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first
        column specified, then color-codes by the second provided column
        to create a Plotly stacked bar chart subplot, one for each election 
        year.

    Args:
        df (DataFrame): A Pandas DataFrame
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the histograms
        facet_feat (str, optional): Name of column for which to create subplots.
             Defaults to 'year'.
        facet_spacing (float, optional): Spacing parameter for Plotly subplots.
             Defaults to 0.05.
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'labels[{group_col_1}] by labels[{group_col_2}] General Elections'.
        percent (str, optional): If 'percent', plots bars as percentages.
            If None, plots as raw counts. Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        width (int, optional): Width of figure. Defaults to 1000.
        height (int, optional): Height of figure. Defaults to 450.
        save (bool, optional): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly stacked bar charts grouped by group_col_1 and color-coded
            according to group_col_2, with one plot for each year. 
    """    


    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'yref':'container',
        'y':0.92
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        },
        'title': ''
    }

    ax_title_font_dict = {
        'family':'Arial Black',
        'size':18
    }

    xax_tick_font_dict = {
        'family':'Arial Black',
        'size':13
    }

    yax_tick_font_dict = {
        'family':'Arial Black',
        'size':15
    }

    ann_dict = {
        'font': {
            'family':'Arial Black',
        'size': 18
        },
        'yref':'paper',
        'y':0.99
    }


    cat_orders = {'year': [2012, 2016, 2020]}
    labels = {}
    
    
    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        cat_orders.update({'gen_grp': ['GenZ', 'Millennial', 'GenX',
                                         'Boomer', 'Greatest-Silent']})
        labels.update({'gen_grp': 'Generation'})
    
    
    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})
    
    
    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})
        
        
    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})
    
    
    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})

    
    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})
    
        
    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})
    
    
    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})
        
        
    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})
    
    
    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['License', 'No License']})
        labels.update({'drivers_lic': 'Drivers License'})
        
    
    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})
    
    
    df_slice = df.copy()
    df_slice = df_slice[[group_col_1, group_col_2, facet_feat, 'birth_age_adj']]
    grpby_slice = df_slice.groupby([
        facet_feat, group_col_1, group_col_2
    ]).count()
    grpby_slice.reset_index(inplace=True)
    grpby_slice.rename(columns={'birth_age_adj':'Count'}, inplace=True)
    

    total_count_slice = df.copy()
    total_count_slice = total_count_slice.drop(
            columns=['birth_age_adj']
        ).groupby(
            [facet_feat,group_col_1]
        ).count()
    total_count_slice.reset_index(inplace=True)
    total_count_slice.rename(columns={group_col_2:'Total'}, inplace=True)
    

    merge_slice = grpby_slice.merge(total_count_slice,
                                     on=[facet_feat,group_col_1])
    merge_slice['Percent'] = round(
            (merge_slice['Count'] / merge_slice['Total']) * 100, 2
        )
    
    
    
    if percent:
        fig = px.bar(merge_slice, x=group_col_1, y='Percent', 
                     color=group_col_2, color_discrete_map=color_map,
                     title='{} by {} in General Elections'.format(
                         labels[group_col_1],
                         labels[group_col_2]
                     ), 
                               facet_col=facet_feat,
                               category_orders=cat_orders,
                               labels=labels,
                               template=template,
                               width=width, height=height,
                               facet_col_spacing=facet_spacing
                          )
        fig.update_yaxes(title='Percent of Registered Voters')  
        
        
        
    else:
        fig = px.bar(merge_slice, x=group_col_1, y='Count', 
                     color=group_col_2, color_discrete_map=color_map,
                     title='{} by {} in General Elections'.format(
                         labels[group_col_1],
                         labels[group_col_2]
                     ), 
                               facet_col=facet_feat,
                               category_orders=cat_orders,
                               labels=labels,
                               template=template,
                               width=width, height=height,
                               facet_col_spacing=facet_spacing
                          )
        fig.update_yaxes(title='Number of Registered Voters')
        
        
    
    fig.update_yaxes(title_text='',row=1, col=2)
    fig.update_yaxes(title_text='',row=1, col=3)

    fig.update_xaxes(title_text='',row=1, col=1)
    fig.update_xaxes(title_text='',row=1, col=3)

    fig.update_layout(
        title=title_dict,
        legend=leg_dict
        )

    fig.update_yaxes(
        title_font=ax_title_font_dict,
        tickfont=yax_tick_font_dict
    )

    fig.update_xaxes(
        title_font=ax_title_font_dict,
        tickfont=xax_tick_font_dict
    )

    fig.for_each_annotation(
        lambda x: x.update(text=x.text.split("=")[-1])
    )

    fig.update_annotations(
        ann_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def basic_pie(df, year, col, title=None,
                  template='seaborn', showlegend=True, save=False, fig_name=None):
    """Takes a DataFrame with a year column, filters the DataFrame to the
        provided election year, and returns a Plotly pie chart for the provided
        column.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        col (str): Name of the df column by which to group
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'Registered Voters by {col} in {year}'.
        template (str, optional): [description]. Defaults to 'seaborn'.
        showlegend (bool, optional): Whether to display the figure legend.
            Defaults to True.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly pie chart color-coded according to col
            for the specified election year. 
    """    


    fig_filepath = 'Figures/'
    
    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'xref': 'paper',
        'yref': 'paper'
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        }
    }
    
    
    labels={}
    
    if col == 'birth_age_adj':
        col='gen_grp'

    if col == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
        labels.update({'gen_grp': 'Generation'})
    
    
    if col == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
        labels.update({'party_grp': 'Party'})
    
    
    if col == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
        labels.update({'vote_method_4': 'Voting Method'})
        
    
    if col == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
        labels.update({'vote_method_5': 'Voting Method'})
        
        
    if col == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
        labels.update({'vote_bin': 'Voted (Y/N)'})
        
    
    
    if col == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
        labels.update({'pri_vote_bin': 'Voted in Primary'})
    
            
    if col == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
        labels.update({'race_grp': 'Race'})
    
    
    if col == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
        labels.update({'gender_code': 'Gender'})
        
        
    if col == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
        labels.update({'birth_reg_other': 'Birth Region'})
    
    
    if col == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
        labels.update({'drivers_lic': 'Drivers License'})
        
    
    if col == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
        labels.update({'city_grp': 'City'})
    
    
    filtered_df = df.loc[df['year']==int(year)] 
    grouped_df = filtered_df.groupby([col]).size().to_frame().reset_index()
    grouped_df.rename(columns={0: 'Count'}, inplace=True)
    
    if title==None:
        title='Registered Voters by {} in {}'.format(
                     labels[col], year
                 )

    fig = px.pie(grouped_df, values='Count', names=col,
                 title=title,
                 color=col,
                 color_discrete_map=color_map,
                 template=template,
                 labels=labels)
    
    fig.update_traces(hoverinfo='label+value', textinfo='percent',
                      textfont_size=15, 
                      insidetextfont={'family':'Arial Black'},
                      outsidetextfont={'family':'Arial Black',
                                       'color': 'black'}
                     )
    
    fig.update_layout(
        title=title_dict,
        legend=leg_dict,
        showlegend=showlegend
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def grp_pie(df, year, group_col_1, group_col_2, col_1_cat, title=None,
                  template='seaborn', showlegend=True, save=False, fig_name=None):
    """Takes a DataFrame with a year column, filters to the specified election 
        year, groups the df by the first column specified, filters to include 
        only the specified category from that column, then displays the composition 
        of that group as categories from the second provided column as a Plotly
        pie chart.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the 
            pie chart
        col_1_cat (str): One of the category labels from group_col_1
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to '{group_col_1} ({col_1_cat}) by <br> {group_col_2} in {year}'.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        showlegend (bool, optional): Whether to display the figure legend. 
            Defaults to True.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Plotly pie chart grouped by group_col_1, filtered to include only
            col_1_cat, and broken down into categories from group_col_2.
    """    

    fig_filepath = 'Figures/'

    
    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'yref':'paper',
        'xref':'paper'
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        }
    }
    
    
    labels={}
    
    if group_col_2 == 'birth_age_adj':
        group_col_2='gen_grp'
    
    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        labels.update({'gen_grp': 'Generation'})


    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        labels.update({'party_grp': 'Party'})


    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        labels.update({'vote_method_4': 'Voting Method'})


    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        labels.update({'vote_method_5': 'Voting Method'})


    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        labels.update({'vote_bin': 'Voted (Y/N)'})


    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        labels.update({'pri_vote_bin': 'Voted in Primary'})


    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        labels.update({'race_grp': 'Race'})


    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        labels.update({'gender_code': 'Gender'})


    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        labels.update({'birth_reg_other': 'Birth Region'})


    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        labels.update({'drivers_lic': 'Drivers License'})


    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        labels.update({'city_grp': 'City'})
    
    df = df.loc[df['year']==int(year)] 
    grouped_df = df.groupby([group_col_1,
                             group_col_2]).size().to_frame().reset_index()
    grouped_df.rename(columns={0: 'Count'}, inplace=True)
    filtered_df = grouped_df.loc[grouped_df[group_col_1]==col_1_cat]
    
    
    if title==None:
        title='{} ({}) by <br>  {} in {}'.format(
            labels[group_col_1], 
            col_1_cat,
            labels[group_col_2],
            str(year)
                 )
    
    fig = px.pie(filtered_df, values='Count', names=group_col_2,
                 title=title, color=group_col_2,
                 color_discrete_map=color_map,
                 template=template,
                 labels=labels)
    
    fig.update_traces(hoverinfo='label+value', textinfo='percent',
                      textfont_size=15, 
                      insidetextfont={'family':'Arial Black'},
                      outsidetextfont={'family':'Arial Black',
                                       'color': 'black'}
                     )
    
    fig.update_layout(
        title=title_dict,
        legend=leg_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')
    
    return fig

#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


@st.cache
def multi_grp_pie(df, group_col_1, group_col_2, col_1_cat,
                  facet_feat='year', title=None,
                  template='seaborn', width=900, height=450,
                  save=False, fig_name=None):
    """Takes a DataFrame with a year column, groups the df by the first column
        specified, filters to include only the specified category from that column,
        then displays the composition of that group as categories from the second
        provided column as a Plotly pie chart. Produces one pie chart for each
        election year.

    Args:
        df (DataFrame): A Pandas DataFrame
        group_col_1 (str): Name of the df column by which to group
        group_col_2 (str): Name of the df column by which to color-code the 
            pie chart
        col_1_cat (str): One of the category labels from group_col_1
        facet_feat (str, optional): Name of column for which to create subplots.
            Defaults to 'year'.
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to '{group_col_1} ({col_1_cat}) by {group_col_2}'.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.
        width (int, optional): Width dimension of the figure. Defaults to 900.
        height (int, optional): Height dimension of the figure. Defaults to 450.
        save (bool, default=False): Whether to save the returned figure. Defaults to False.
        fig_name (str, optional): What to name the file if the image is being saved.
            Defaults to None.

    Returns:
        Figure: Multiple Plotly pie charts, one for each year, grouped by group_col_1,
         filtered to include only col_1_cat, and broken down into categories 
         from group_col_2.
    """    

    
    fig_filepath = 'Figures/'

    title_dict = {
        'font' : {
            'family':'Arial Black',
            'size':24
        },
        'yref': 'container',
        'y':.85
    }

    leg_dict = {
        'font' : {
            'family':'Arial Black',
            'size':13
        }
    }
    
    ann_dict = {
        'font': {
            'family':'Arial Black',
        'size': 18
        },
        'yref': 'paper',
        'y':.87
    }
    
    
    labels={}
    cat_orders={}
    
    if group_col_2 == 'birth_age_adj':
        group_col_2='gen_grp'
    
    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
    if (group_col_1 == 'gen_grp') | (group_col_2 == 'gen_grp'):
        labels.update({'gen_grp': 'Generation'})


    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
    if (group_col_1 == 'party_grp') | (group_col_2 == 'party_grp'):
        cat_orders.update({'party_grp': ['Dem', 'Rep', 'Other']})
        labels.update({'party_grp': 'Party'})


    if group_col_2 == 'vote_method_4':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_4') | (group_col_2 == 'vote_method_4'):
        cat_orders.update({'vote_method_4': ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'vote_method_4': 'Voting Method'})


    if group_col_2 == 'vote_method_5':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_method_5') | (group_col_2 == 'vote_method_5'):
        cat_orders.update({'vote_method_5': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_method_5': 'Voting Method'})


    if group_col_2 == 'vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'vote_bin') | (group_col_2 == 'vote_bin'):
        cat_orders.update({'vote_bin': ['Y', 'N']})
        labels.update({'vote_bin': 'Voted (Y/N)'})


    if group_col_2 == 'pri_vote_bin':
        color_map = {
            'Y': 'blue',
            'N': 'goldenrod'
        }
    if (group_col_1 == 'pri_vote_bin') | (group_col_2 == 'pri_vote_bin'):
        cat_orders.update({'pri_vote_bin': ['Y', 'N']})
        labels.update({'pri_vote_bin': 'Voted in Primary'})


    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
    if (group_col_1 == 'race_grp') | (group_col_2 == 'race_grp'):
        cat_orders.update({'race_grp': ['White',
                                        'Black',
                                        'Undesig.',
                                        'Other']})
        labels.update({'race_grp': 'Race'})


    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
    if (group_col_1 == 'gender_code') | (group_col_2 == 'gender_code'):
        cat_orders.update({'gender_code': ['F', 'M', 'U']})
        labels.update({'gender_code': 'Gender'})


    if group_col_2 == 'birth_reg_other':
        color_map = {
            'South': '#AB63FA',
            'Missing': '#FFA15A',
            'Northeast': '#19D3F3',
            'Midwest': '#FF6692',
            'Other': '#B6E880',
            'West': '#FF97FF'
        }
    if (group_col_1 == 'birth_reg_other') | (group_col_2 == 'birth_reg_other'):
        cat_orders.update({'birth_reg_other': ['South',
                                               'Missing',
                                               'Northeast',
                                               'Midwest',
                                               'Other',
                                               'West']})
        labels.update({'birth_reg_other': 'Birth Region'})


    if group_col_2 == 'drivers_lic':
        color_map = {
            'License': 'green',
            'No License': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['License', 'No License']})
        labels.update({'drivers_lic': 'Drivers License'})


    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
    if (group_col_1 == 'city_grp') | (group_col_2 == 'city_grp'):
        cat_orders.update({'city_grp': ['Monroe',
                                        'Waxhaw',
                                        'Indian Trail',
                                        'Matthews',
                                        'Other']})
        labels.update({'city_grp': 'City'})
    
    
    # Create subplots, using 'domain' type for pie charts
    specs = []
    for i in range(df[facet_feat].nunique()):
        specs.append({'type':'domain'})
    specs = [specs]
    subplot_titles = []
    for val in sorted(df[facet_feat].unique()):
        subplot_titles.append('{}={}'.format(facet_feat, str(val)))
    fig = make_subplots(rows=1, cols=df[facet_feat].nunique(),
                        specs=specs,
                        subplot_titles=subplot_titles)
    
    for i, val in enumerate(sorted(df[facet_feat].unique())):        
        val_fig = grp_pie(df, year=val, 
                              group_col_1=group_col_1,
                              group_col_2=group_col_2,
                              col_1_cat=col_1_cat,
                              title=str(val))
        val_data = val_fig['data'][0]
           
        fig.add_trace(
            val_data,
            row=1, col=i+1
        )
    
    if title==None:
        title='{} ({}) by {}'.format(
            labels[group_col_1], 
            col_1_cat,
            labels[group_col_2]
                 )
    fig.update_layout(title_text=title,
                      template=template,
                      title=title_dict,
                      legend=leg_dict,
                      width=width,
                      height=height)
    
    fig.for_each_annotation(
        lambda x: x.update(text=x.text.split("=")[-1])
    )

    fig.update_annotations(
        ann_dict
    )


    if save:
        fig.write_html(fig_filepath+fig_name+'.html')
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################

##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Build dashboard layout and widgets
##########################################################################
##########################################################################

## Settings for app page
st.set_page_config(
    page_title='Union County Registered Voters',
    layout='centered',
    initial_sidebar_state='auto',
    page_icon=':us:'
)



##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Define Sidebar for Navigation
##########################################################################
##########################################################################
side_title = st.sidebar.header(
    'Choose Sections to Display:'
)
side_sec_1 = st.sidebar.subheader(
    'Explore by Year'
)

side_syr_select_1 = st.sidebar.checkbox(
    label='One Variable',
    value=True,
    key='syr_select_1'
)

side_syr_select_2 = st.sidebar.checkbox(
    label='Two Variables',
    value=False,
    key='syr_select_2'
)

side_sec_2 = st.sidebar.subheader(
    'Compare Years'
)

side_myr_select_1 = st.sidebar.checkbox(
    label='One Variable',
    value=True,
    key='myr_select_1'
)

side_myr_select_2 = st.sidebar.checkbox(
    label='Two Variables',
    value=False,
    key='myr_select_2'
)



##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Introduction Section
##########################################################################
##########################################################################

## Set page title
st.title('Registered Voter Participation in Union County, North Carolina')

## Introduction 
# Define container for the section
intro = st.beta_container()
intro.write("")
intro.markdown(
    """
    **Created by: Max Steele -- <maxsteele731@gmail.com>**\n
    **[Github Project Repo](https://github.com/zero731/NC_Elections_Capstone)**
    """
)
intro.markdown('')
intro.markdown(
    """
    This dashboard allows you to interactively explore and visualize 
    trends in registered voter turnout in Union County, NC for the
    2012, 2016, and 2020 general elections. Use the sidebar selection 
    menu to display/hide sections.
    """
)

intro.markdown(
    """
    The data used to produce this dashboard were obtained from the
    [North Carolina State Board of Elections (NCSBE)](https://www.ncsbe.gov/results-data).
    The dataset combines information from voter registration records with voter
    history data.
    """
)


data_note = intro.beta_expander(
    'Important Note for Interpreting Graphs:',
    expanded=True
)
data_note.markdown(
    """
    When interpreting the raw counts and percentages in the graphs you
    create, keep in mind the specific population that the data 
    reflects:\n - **Registered voters** eligible to vote in Union County
    in the 2020 general election, **NOT** all people in the county who 
    were legally eligible to register to vote.\n\n - Voters whose 
    registration status was neither _"Removed"_ nor _"Denied"_  as of 
    when the data files were obtained from NCSBE on January 4th, 2021. 
    This may have removed some voters from the 2012 and 2016 datasets 
    who might have been eligible to vote in those elections, but were 
    not eligible in 2020 (the date of voter registration status change is 
    not made available by NCSBE).\n\n - For the 2012 and 2016 elections,
    the population of registered voters was further filtered based on 
    registration date and age to remove people who did not register in 
    time in a certain year or were not yet old enough to vote.
    """
)

plotly_note = intro.beta_expander(
    'Interactive Graph Functionality:'
)
plotly_note.markdown(
    """
    The graphs you can create are interactive and were created using 
    [Plotly](https://plotly.com/). As you hover over the a graph,
    certain information will be displayed and a Modebar will appear. 
    Find a tutorial on how to use the Modebar 
    [here](https://plotly.com/chart-studio-help/getting-to-know-the-plotly-modebar/).
    You can switch to a fullscreen view by clicking on the divergent 
    arrows associated with the Modebar.
    """
)



##########################################################################
##########################################################################
##########################################################################
##########################################################################
###### Section for exploring by year
##########################################################################
##########################################################################

if side_syr_select_1:
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


if side_syr_select_2:
    ##########################################################################
    ##########################################################################
    ##########################################################################
    ## Grouped histogram for a single year
    # Define container for section
    single_yr_grp = st.beta_container()
    single_yr_grp.header('Explore trends for a single election year:')
    single_yr_grp.subheader('Break down trends across 2 variables at a time:')
    syg_col_1, syg_col_2, syg_col_3 = single_yr_grp.beta_columns(3)

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
    ghist_norm = syg_col_3.radio(
        label='Display as: ',
        options = [None, 'percent'],
        index=0,
        format_func=norm_label,
        key='g_norm'
    )


    # Choose bar type
    ghist_bar = syg_col_3.radio(
        label='Bar type: ',
        options = ['Grouped', 'Stacked'],
        index=0,
        key='g_bar'
    )


    # Plot grouped histogram for a single year
    if ghist_bar=='Grouped':
        syg_hist = grp_hist(
            gen_elecs_df, ghist_year,
            ghist_group_col_1,
            ghist_group_col_2,
            histnorm=ghist_norm
        )
    if ghist_bar=='Stacked':
        syg_hist = stack_grp_hist(
            gen_elecs_df, ghist_year,
            ghist_group_col_1,
            ghist_group_col_2,
            percent=ghist_norm
        )

    single_yr_grp.plotly_chart(syg_hist, use_container_width=True)


    ##########################################################################
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

if side_myr_select_1:
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
if side_myr_select_2:
    ## Grouped histogram subplots per year 
    # Define container for section
    multi_yr = st.beta_container()
    multi_yr.header('Compare trends across election years:')
    multi_yr.subheader('Break down trends across 2 variables at a time:')
    myr_col_1, myr_col_2, myr_col_3 = multi_yr.beta_columns(3)


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
        index=2,
        format_func=format_col_names,
        key='m_grp_col_1'
    )

    # Choose 2nd column to group by/ investigate
    if myrhist_group_col_1 in vote_method_opts:
        myrhist_group_col_2 = myr_col_1.selectbox(
            label='Then by: ',
            options = non_vote_method_opts,
            index=1,
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


    # Choose bar type
    myrhist_bar = myr_col_3.radio(
        label='Bar type: ',
        options = ['Grouped', 'Stacked'],
        index=0,
        key='myr_bar'
    )


    # Plot grouped histogram for a single year
    if myrhist_bar=='Grouped':
        myr_hist = multi_yr_hist(
            gen_elecs_df, 
            myrhist_group_col_1, 
            myrhist_group_col_2,
            histnorm=myrhist_norm,
            width=900, height=450
            )
    if myrhist_bar=='Stacked':
        myr_hist = stack_multi_yr_hist(
            gen_elecs_df,
            myrhist_group_col_1,
            myrhist_group_col_2,
            percent=myrhist_norm
        )

    multi_yr.plotly_chart(myr_hist, use_container_width=False)

    
    ##########################################################################
    ##########################################################################
    ## Grouped pie charts for each year
    # Define container for section
    multi_yr_grp_pie = st.beta_container()
    mygp_col_1, mygp_col_2 = multi_yr_grp_pie.beta_columns(2)


    # Choose category from column 2 to investigate
    if myrhist_group_col_2=='gen_grp':
        mygpie_col_cat_opt = [
            'Millennial', 'GenX',
            'Boomer', 'Greatest-Silent'
        ]

    else:
        for opt in myrhist_col_opt:
            if myrhist_group_col_2==opt:
                mygpie_col_cat_opt = gen_elecs_df[myrhist_group_col_2].unique()

    mygpie_col_1_cat = mygp_col_1.selectbox(
        label='Choose category: ',
        options = mygpie_col_cat_opt,
        index=1,
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

    genZ_note = multi_yr_grp_pie.beta_expander('Why is Gen Z not a category option?')
    genZ_note.write(
        """
        Gen Z is not a category here because there is no 2012 plot for this age group.
        No one belonging to this age group was old enough to vote during this election 
        year. The 2016 and 2020 pie charts for Gen Z can be viewed when grouping by two
        variables in the single election year section.
        """
    )