#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


def basic_hist(df, year, col, title=None, histnorm=None,
                  template='seaborn'):
    """Takes a DataFrame with a year column, filters the DataFrame to the
        provided election year, and returns a color-coded Plotly histogram 
        for the provided column.

    Args:
        df (DataFrame): A Pandas DataFrame
        year (int): Election year (2012, 2016, or 2020 only)
        col (str): Name of the df column for which to plot histogram
        title (str, optional): Title for the resulting plot. If none is provided,
            defaults to 'Distribution of labels[{col}] in {year} General Election'.
        histnorm (str, optional): Ploty histnorm parameter, but only takes None or 'percent'.
            Defaults to None.
        template (str, optional): Plotly style template. Defaults to 'seaborn'.

    Returns:
        Figure: Returns Plotly histogram of provided column for the specified year.
    """    

    import pandas as pd
    import plotly.express as px
    
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
        labels.update({'vote_bin': 'Voted in Election'})
        
    
    
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
            'Y': 'green',
            'N': 'crimson'
        }
        cat_orders.update({'drivers_lic': ['Y', 'N']})
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
                           title='Distribution of {} in {} General Election'.format(
                           labels[col], str(year)
                           ), 
                           color_discrete_sequence=['dodgerblue'],
                           category_orders=cat_orders,
                           labels=labels,
                           template=template,
                           histnorm=histnorm,
                           nbins=50
                      )
        
    
    else:
        fig = px.histogram(filtered_df, x=col, color=col,
                           color_discrete_map=color_map,
                           title='Distribution of {} in {} General Election'.format(
                           labels[col], str(year)
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
    
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################



def grp_hist(df, year, group_col_1, group_col_2, title=None,
             barmode='group', histnorm=None,
             template='seaborn'):
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

    Returns:
        Figure: Plotly histogram grouped by group_col_1 and color-coded
            according to group_col_2 for the specified election year. 
    """    
    import pandas as pd
    import plotly.express as px
    

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
        labels.update({'vote_bin': 'Voted in Election'})


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
            'Y': 'green',
            'N': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['Y', 'N']})
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

    if group_col_1 == 'birth_age_adj':
        labels.update({'birth_age_adj': 'Age'})
        fig = px.histogram(filtered_df, x=group_col_1, color=group_col_2,
                       color_discrete_map=color_map, barmode=barmode, 
                       title='{} by {} in {} General Election'.format(
                           labels[group_col_1],
                           labels[group_col_2],
                           str(year)
                           ), 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template,
                           histnorm=histnorm,
                       nbins=50
                      )


    else:
        fig = px.histogram(filtered_df, x=group_col_1, color=group_col_2,
                       color_discrete_map=color_map, barmode=barmode, 
                       title='{} by {} in {} General Election'.format(
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
    

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################



def grp_yr_hist(df, group_col_1, title=None, barmode='group',
                histnorm=None, template='seaborn'):
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

    Returns:
        Figure: Plotly histogram grouped by group_col_1 and color-coded
            according to group_col_2 for the specified election year. 
    """    
    import pandas as pd
    import plotly.express as px
    

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
        labels.update({'vote_bin': 'Voted in Election'})


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
        cat_orders.update({'drivers_lic': ['Y', 'N']})
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

    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################



def multi_yr_hist(df, group_col_1, group_col_2,
                  facet_feat='year', facet_spacing=0.05,
                  title=None, barmode='group', histnorm=None,
                  template='seaborn', width=1000, height=450):
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

    Returns:
        Figure: Plotly histograms grouped by group_col_1 and color-coded
            according to group_col_2, with one plot for each year. 
    """    

    
    import pandas as pd
    import plotly.express as px
    
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
        labels.update({'vote_bin': 'Voted in Election'})

    
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
            'Y': 'green',
            'N': 'crimson'
        }
    if (group_col_1 == 'drivers_lic') | (group_col_2 == 'drivers_lic'):
        cat_orders.update({'drivers_lic': ['Y', 'N']})
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
    
    
    if group_col_1 == 'birth_age_adj':
        labels.update({'birth_age_adj': 'Age'})
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
                           facet_col_spacing=facet_spacing,
                           nbins=50
                          )
        
    
    else:
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

    return fig


    
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################






#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################







#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################






#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################














def basic_pie(df, year, col, title=None,
                  template='seaborn'):
    
    import pandas as pd
    import plotly.express as px
    
    labels={}
    
    
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
    
    if col == 'Gen_{}'.format(str(year)):
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
        labels.update({'Gen_{}'.format(str(year)): 'Voting Method'})
        
    
    if col == 'vote_cat':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
        labels.update({'vote_cat': 'Voting Method'})
    
        
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
            'Y': 'green',
            'N': 'crimson'
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
    
    
    grouped_df = df.groupby([col]).size().to_frame().reset_index()
    grouped_df.rename(columns={0: 'Count'}, inplace=True)
    
    fig = px.pie(grouped_df, values='Count', names=col,
                 title=title, color=col,
                 color_discrete_map=color_map,
                 template=template,
                 labels=labels)
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################





#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################



def grp_pie(df, year, group_col_1, group_col_2, col_1_cat, title=None,
                  template='seaborn'):
    
    import pandas as pd
    import plotly.express as px
    
    labels={}
    
    
    if group_col_2 == 'gen_grp':
        color_map = {
            'Greatest-Silent': 'orchid',
            'Boomer': 'dodgerblue',
            'GenX': 'mediumspringgreen',
            'Millennial': 'gold',
            'GenZ': 'coral'
        }
        labels.update({'gen_grp': 'Generation'})
    
    
    if group_col_2 == 'party_grp':
        color_map = {
            'Dem': 'blue',
            'Rep': 'red',
            'Other': 'gold'
        }
        labels.update({'party_grp': 'Party'})
    
    if group_col_2 == 'Gen_{}'.format(str(year)):
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
        labels.update({'Gen_{}'.format(str(year)): 'Voting Method'})
        
        
    if group_col_2 == 'vote_cat':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
        labels.update({'vote_cat': 'Voting Method'})
        
        
    if group_col_2 == 'race_grp':
        color_map = {
            'White': 'forestgreen',
            'Black': 'firebrick',
            'Undesig.': 'mediumslateblue',
            'Other': 'fuchsia'
        }
        labels.update({'race_grp': 'Race'})
    
    if group_col_2 == 'gender_code':
        color_map = {
            'F': 'deeppink',
            'M': 'deepskyblue',
            'U': 'lawngreen'
        }
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
        labels.update({'birth_reg_other': 'Birth Region'})
    
    
    if group_col_2 == 'drivers_lic':
        color_map = {
            'Y': 'green',
            'N': 'crimson'
        }
        labels.update({'drivers_lic': 'Drivers License'})
        
    
    if group_col_2 == 'city_grp':
        color_map = {
            'Monroe': '#FD3216',
            'Waxhaw': '#00FE35',
            'Indian Trail': '#6A76FC',
            'Matthews': '#0DF9FF',
            'Other': '#F6F926'
        }
        labels.update({'city_grp': 'City'})
    
    
    grouped_df = df.groupby([group_col_1,
                             group_col_2]).size().to_frame().reset_index()
    grouped_df.rename(columns={0: 'Count'}, inplace=True)
    filtered_df = grouped_df.loc[grouped_df[group_col_1]==col_1_cat]
    
    fig = px.pie(filtered_df, values='Count', names=group_col_2,
                 title=title, color=group_col_2,
                 color_discrete_map=color_map,
                 template=template,
                 labels=labels)
    
    return fig



#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
