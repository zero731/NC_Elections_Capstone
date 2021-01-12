def check_unique(col, df, dropna=False):
    
    """Takes in a Pandas DataFrame and specific column name and returns a Pandas DataFrame 
    displaying the unique values in that column as well as the count of each unique value. 
    Default is to also provide a count of NaN values.
    
    Args:
        col (str): Name of the column you want to check.
        df (Pandas DataFrame): DataFrame containing the column to check the unique values of.
        dropna (bool, default=False): Whether or not to drop null values from list of values.
    
    Returns:
        DataFrame: Pandas DataFrame with columns for the unique values in the specified column, 
            the number of occurrences of each unique value in that column, and the percentage of 
            the column made up by each unique value.
    
    Example:
        >>> df = pd.DataFrame({'a': [2, 4, 4, 6],
                               'b': [2, 1, 3, 4]})

        >>> check_unique(col='a', df, dropna=False)
        
            count   %
        4   2   0.50
        6   1   0.25
        2   1   0.25
    """
    
    import pandas as pd
    
    unique_vals = pd.DataFrame()
    unique_vals['count'] = pd.Series(df[col].value_counts(dropna=dropna))
    unique_vals['%'] = pd.Series(round(df[col].value_counts(normalize=True, dropna=dropna)*100, 2))
    
    return unique_vals


#################################################################################
#################################################################################

#################################################################################
#################################################################################


def plot_count(variable, data, rotation=0, figsize=(10,7)):
    
    """Takes in a variable/ column name and the DataFrame containing the column
    and returns a countplot for that variable with counts in descending order.
    """
    
    import matplotlib.pyplot as plt
    import seaborn as sns    
    
    plt.figure(figsize=figsize)
    ax = sns.countplot(x=data[variable],
                       order=data[variable].value_counts().index,
                       palette='nipy_spectral')
    
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
    ax.set_title('{} Counts'.format(variable.title()), fontsize=16, weight='bold')
    ax.set_xlabel('{}'.format(variable), fontsize=14, weight='bold')
    ax.set_ylabel('Count', fontsize=14, weight='bold')
    
    return ax



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def compare_age_distr(df1, df1_label, df2, df2_label, stat='density'):
    
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig,ax = plt.subplots(figsize=(10,7))
    
    sns.histplot(df1['birth_age'], stat=stat, color='r',
             label=df1_label, alpha=0.6, ax=ax)
    sns.histplot(df2['birth_age'], stat=stat,
             label=df2_label, alpha=0.6, ax=ax)
    
    ax.set_title('Current Age Distributions:\n{} vs. {}'.format(
        df1_label,df2_label), fontsize=16, weight='bold')
    ax.set_xlabel('Age', fontsize=14, weight='bold')
    ax.set_ylabel('{}'.format(stat.title()), fontsize=14, weight='bold')
    ax.set_xlim(15,115)
    ax.legend()
    
    return fig,ax



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def basic_px_hist(df, year, col, title=None,
                template='seaborn'):
    
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
    
    
    if col == 'Gen_{}'.format(str(year)):
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
        cat_orders.update({'Gen_{}'.format(str(year)): ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'Gen_{}'.format(str(year)): 'Voting Method'})
        
    
    if col == 'vote_cat':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
        cat_orders.update({'vote_cat': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_cat': 'Voting Method'})
        
        
        
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
        
    
    fig = px.histogram(df, x=col, color=col,
                       color_discrete_map=color_map,
                       title=title, 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template
                      )
    
    return fig



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



def grp_px_hist(df, year, group_col_1, group_col_2, title=None, barmode='group',
                template='seaborn'):
    
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
    
    
    if group_col_2 == 'Gen_{}'.format(str(year)):
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Other': 'aqua'
        }
    if (group_col_1 == 'Gen_{}'.format(str(year))) | (group_col_2 == 'Gen_{}'.format(str(year))):
        cat_orders.update({'Gen_{}'.format(str(year)): ['Early', 'No Vote',
                                        'Election Day', 'Other']})
        labels.update({'Gen_{}'.format(str(year)): 'Voting Method'})
        
        
    if group_col_2 == 'vote_cat':
        color_map = {
            'Early': 'navy',
            'No Vote': 'goldenrod',
            'Election Day': 'teal',
            'Mail': 'blue',
            'Other': 'aqua'
        }
    if (group_col_1 == 'vote_cat') | (group_col_2 == 'vote_cat'):
        cat_orders.update({'vote_cat': ['Early', 'No Vote',
                                        'Election Day', 'Mail',
                                        'Other']})
        labels.update({'vote_cat': 'Voting Method'})
        
        
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
                       title=title, 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template,
                       nbins=50
                      )
        
    
    else:
        fig = px.histogram(df, x=group_col_1, color=group_col_2,
                       color_discrete_map=color_map, barmode=barmode, 
                       title=title, 
                       category_orders=cat_orders,
                       labels=labels,
                       template=template
                      )
    
    return fig



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



def eval_classifier(clf, X_test, y_test, model_descr='',
                    target_labels=['Early', 'Election Day', 'No Vote'],
                    cmap='Blues', normalize='true', save=False, fig_name=None):
    
    """Given an sklearn classification model (already fit to training data), test features, and test labels,
       displays sklearn.metrics classification report and confusion matrix. A description of the model 
       can be provided to model_descr to customize the title of the classification report.
       
       
    Args:
        clf (estimator): Fitted classifier.
        X_test (series or array): Subset of X data used for testing.
        y_test (series or array): Subset of y data used for testing.
        model_descr (str): A description of the model for customizing plot title.
        target_labels (list of strings, default=['Early', 'Election Day', 'No Vote']): List of class labels 
            used for formatting tick labels.
        cmap (str, default='Blues'): Specifies a color map that can be used by sklearn's plot_confusion_matrix.
        normalize (str, {'true', 'pred', 'all', None}, default='true'): Whether to normalize the
        confusion matrix over the true (rows), predicted (columns) conditions or all the population. 
        If None, confusion matrix will not be normalized.
        save (bool, default=False): Whether to save the returned figure.
        fig_name (str, optional): What to name the file if the image is being saved.
    
    Returns:
        display: Sklearn classification report and confusion matrix.
    
    Example:
        >>> eval_classifier(clf=my_model, X_test, y_test, model_descr='My Model',
                    target_labels=['Early', 'Election Day', 'No Vote'],
                    cmap='Blues', normalize='true', save=true, fig_name='my_model_eval')
    
    """
    
    import matplotlib.pyplot as plt
    from sklearn.metrics import classification_report, plot_confusion_matrix
    
    
    fig_filepath = 'Figures/'
    
    ## get model predictions
    y_hat_test = clf.predict(X_test)
    
    
    ## Classification Report
    report_title = 'Classification Report: {}'.format(model_descr)
    divider = ('-----' * 11) + ('-' * (len(model_descr) - 31))
    report_table = classification_report(y_test, y_hat_test,
                                         target_names=target_labels)
    print(divider, report_title, divider, report_table, divider, divider, '\n', sep='\n')
    
    
    ## Make Subplots for Figures
    fig, axes = plt.subplots(figsize=(10,6))
    
    ## Confusion Matrix
    plot_confusion_matrix(clf, X_test, y_test, 
                          display_labels=target_labels, 
                          normalize=normalize, cmap=cmap, ax=axes)
    
    axes.set_title('Confusion Matrix:\n{}'.format(model_descr),
                   fontdict={'fontsize': 18,'fontweight': 'bold'})
    axes.set_xlabel(axes.get_xlabel(),
                       fontdict={'fontsize': 12,'fontweight': 'bold'})
    axes.set_ylabel(axes.get_ylabel(),
                       fontdict={'fontsize': 12,'fontweight': 'bold'})
    axes.set_xticklabels(axes.get_xticklabels(),
                       fontdict={'fontsize': 10,'fontweight': 'bold'})
    axes.set_yticklabels(axes.get_yticklabels(), 
                       fontdict={'fontsize': 10,'fontweight': 'bold'})
    
    
    if save:
        plt.savefig(fig_filepath+fig_name, bbox_inches = "tight")
    
    fig.tight_layout()
    plt.show()

    return fig, axes



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def eval_bin_clf(clf, X_test, y_test, model_descr='',
                    target_labels=['No Vote', 'Vote'],
                    cmap='Blues', normalize='true', save=False, fig_name=None):
    
    """Given an sklearn binary classification model (already fit to training data), test features, and test labels,
       displays sklearn.metrics classification report, confusion matrix, and ROC curve. A description of the model 
       can be provided to model_descr to customize the title of the classification report.
       
       
    Args:
        clf (estimator): Fitted classifier with a binary target.
        X_test (series or array): Subset of X data used for testing.
        y_test (series or array): Subset of y data used for testing.
        model_descr (str): A description of the model for customizing plot title.
        target_labels (list of strings, default=['No Vote', 'Vote']): List of class labels 
            used for formatting tick labels.
        cmap (str, default='Blues'): Specifies a color map that can be used by sklearn's plot_confusion_matrix.
        normalize (str, {'true', 'pred', 'all', None}, default='true'): Whether to normalize the
        confusion matrix over the true (rows), predicted (columns) conditions or all the population. 
        If None, confusion matrix will not be normalized.
        save (bool, default=False): Whether to save the returned figure.
        fig_name (str, optional): What to name the file if the image is being saved.
    
    Returns:
        display: Sklearn classification report and confusion matrix.
    
    Example:
        >>> eval_classifier(clf=my_model, X_test, y_test, model_descr='My Model',
                    target_labels=['No Vote', 'Vote'],
                    cmap='Blues', normalize='true', save=true, fig_name='my_model_eval')
    
    """
    
    import matplotlib.pyplot as plt
    from sklearn.metrics import classification_report, plot_confusion_matrix, plot_roc_curve
    
    
    fig_filepath = 'Figures/'
    
    ## get model predictions
    y_hat_test = clf.predict(X_test)
    
    
    ## Classification Report
    report_title = 'Classification Report: {}'.format(model_descr)
    divider = ('-----' * 11) + ('-' * (len(model_descr) - 31))
    report_table = classification_report(y_test, y_hat_test,
                                         target_names=target_labels)
    print(divider, report_title, divider, report_table, divider, divider, '\n', sep='\n')
    
    
    ## Make Subplots for Figures
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
    
    ## Confusion Matrix
    plot_confusion_matrix(clf, X_test, y_test, 
                                  display_labels=target_labels, 
                                  normalize=normalize, cmap=cmap, ax=axes[0])
    
    axes[0].set_title('Confusion Matrix', fontdict={'fontsize': 18,'fontweight': 'bold'})
    axes[0].set_xlabel(axes[0].get_xlabel(),
                       fontdict={'fontsize': 12,'fontweight': 'bold'})
    axes[0].set_ylabel(axes[0].get_ylabel(),
                       fontdict={'fontsize': 12,'fontweight': 'bold'})
    axes[0].set_xticklabels(axes[0].get_xticklabels(),
                       fontdict={'fontsize': 10,'fontweight': 'bold'})
    axes[0].set_yticklabels(axes[0].get_yticklabels(), 
                       fontdict={'fontsize': 10,'fontweight': 'bold'})
    
    
    ## ROC Curve
    plot_roc_curve(clf, X_test, y_test, ax=axes[1])
    # plot line that demonstrates probable success when randomly guessing labels
    axes[1].plot([0,1],[0,1], ls='--', color='r')
    
    axes[1].set_title('ROC Curve', 
                      fontdict={'fontsize': 18,'fontweight': 'bold'})
    axes[1].set_xlabel(axes[1].get_xlabel(), 
                      fontdict={'fontsize': 12,'fontweight': 'bold'})
    axes[1].set_ylabel(axes[1].get_ylabel(), 
                      fontdict={'fontsize': 12,'fontweight': 'bold'})
    
    
    if save:
        plt.savefig(fig_filepath+fig_name, bbox_inches = "tight")
    
    fig.tight_layout()
    plt.show()

    return fig, axes



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def fit_grid_clf(clf, params, X_train, y_train, X_test, y_test, bin_target=False,
                 model_descr='', score='accuracy', cv=5,
                 target_labels=['Early', 'Election Day', 'No Vote']):
    
    """Given an sklearn classification model, hyperparameter grid, X and y training data, 
       and a GridSearchCV scoring metric (default is 'accuracy', which is the default metric for 
       GridSearchCV), fits a grid search of the specified parameters on the training data and 
       returns the grid object. Function also takes in X_test and y_test to get predictions and 
       evaluate model performance on test data. Prints out parameters of the best estimator as well 
       as its classification report and confusion matrix. A description of the model can be provided
       to model_descr to customize the title of the classification report.
       
    Args:
        clf (estimator): Fitted classifier.
        params (dict): Dictionary with parameters names (`str`) as keys and lists of 
            parameter settings to try as values.
        X_train (series or array): Subset of X data used for training.
        y_train (series or array): Subset of y data used for training.
        X_test (series or array): Subset of X data used for testing.
        y_test (series or array): Subset of y data used for testing.
        model_descr (str): A description of the model for customizing plot title.
        score (str, default='accuracy'): A string indicating a scoring method compatible with 
            sklearn.model_selection's GridSearchCV.
    
    Returns:
        grid: Fitted GridSearchCV object
    
    Example:
        >>> param_grid = {'param_name_1':[(1,1),(1,2),(1,3)],
                          'param_name_2':[0.005, 2, 3],
                         }
        >>> fit_grid_clf(clf=my_model, params=param_grid, X_train, y_train, X_test, y_test,
                 model_descr='My Model', score='accuracy')
    
    """
    
    from sklearn.model_selection import GridSearchCV
    import datetime as dt
    from tzlocal import get_localzone
    
    
    start = dt.datetime.now(tz=get_localzone())
    fmt= "%m/%d/%y - %T %p"
    
    print('---'*20)    
    print(f'***** Grid Search Started at {start.strftime(fmt)}')
    print('---'*20)
    print()
    
    grid = GridSearchCV(clf, params, scoring=score, cv=cv, n_jobs=-1)
    grid.fit(X_train, y_train)
    
    end = dt.datetime.now(tz=get_localzone())
    
    print(f'\n***** Training Completed at {end.strftime(fmt)}')
    print(f"\n***** Total Training Time: {end-start}")
    print('\n')
    
    print('Best Parameters:')
    print(grid.best_params_)
    print('\n')
    if bin_target:
        eval_bin_clf(grid.best_estimator_, X_test, y_test, model_descr)
    else:
        eval_classifier(grid.best_estimator_, X_test, y_test, model_descr, target_labels)
    
    return grid



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def plot_feat_importance(clf, clf_step_name, feature_names,
                         model_title='', save=False, fig_name=None):
    
    """Takes in an sklearn classifier already fit to training data, the name of the step for that model
       in the modeling pipeline, and optionally a title describing the model. 
       Returns a horizontal barplot showing the top 20 most important features in descending order.
         
    Args:
        clf (estimator): An sklearn Pipeline with a vectorizer steps and final step is a fitted classifier.
        clf_step_name (str): The name given to the classifier step of the pipe.
        vec_step_name (str): The name given to the vectorizer step of the pipe.
        model_title (str): A description of the model for customizing plot title.
        save (bool, default=False): Whether to save the returned figure.
        fig_name (str, optional): What to name the file if the image is being saved.
    
    Returns:
        figure: Matplotlib.pyplot bar plot figure showing the feature importance values for the 
            20 most important features.
    
    Example:
        >>> plot_feat_importance(clf=my_model, clf_step_name='clf', feature_names=feature_names,
        model_title='My Model', save=True, fig_name='my_model_feat_import')
    
    """

    import pandas as pd
    from sklearn.model_selection import GridSearchCV
    import matplotlib.pyplot as plt
    
    fig_filepath = 'Figures/'
    
    feature_importances = (
        clf.named_steps[clf_step_name].feature_importances_)
    
    importance = pd.Series(feature_importances, index=feature_names)
    plt.figure(figsize=(8,6))
    fig = importance.sort_values().tail(20).plot(kind='barh')
    fig.set_title('{} Feature Importances'.format(model_title), fontsize=18, fontweight='bold')
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12)
    
    if save:
        plt.savefig(fig_filepath+fig_name, bbox_inches = "tight")

    plt.show()
    
    return fig



#################################################################################
#################################################################################

#################################################################################
#################################################################################



def multi_shap_summ(multi_shap_vals, X_train, label):
    
    import pandas as pd
    import shap
    
    ## Load JS visualization code to notebook
    shap.initjs()
    
    ## Create dict for mapping class labels
    label_dict = {0: 'Early',
                  1: 'Election Day',
                  2: 'No Vote'}
    
    ## Format and add description above plot
    print('\n')
    print('******************** {} Class ********************'.format(
        label_dict[label])
         )
    
    ## Plot summary plot for specified class label
    shap.summary_plot(multi_shap_vals[label], X_train)
    
    
    
#################################################################################
#################################################################################

#################################################################################
#################################################################################

    

def multi_shap_force(clf, clf_step_name, index,
                 X_train_df, y_train,
                 explainer, multi_shap_vals,
                 classes='all'):

    import pandas as pd
    import shap

    ## Load JS visualization code to notebook
    shap.initjs()

    ## Create dict for mapping class labels
    label_dict = {0: 'Early',
                  1: 'Election Day',
                  2: 'No Vote'}

    ## Store the model's prediction and ground truth label for that index
    pred = int(clf.named_steps[clf_step_name].predict(X_train_df.iloc[index,:]))
    true_label = pd.Series(y_train).iloc[index]

    ## Print model prediction for ith row of training set
    print('Model Prediction: {} - {}'.format(pred,
                                             label_dict[pred]))

    ## Print ground truth label ith row of training set
    print('Ground Truth Label: {} - {}'.format(true_label,
                                               label_dict[true_label]))

    print()

    if classes == 'all':
        ## Visualize the ith prediction's explanation for all classes
        print('Early Vote Class (0)')
        display(shap.force_plot(explainer.expected_value[0],
                    multi_shap_vals[0][index],
                    X_train_df.iloc[index,:]))
        print()

        print('Election Day Vote Class (1)')
        display(shap.force_plot(explainer.expected_value[1],
                    multi_shap_vals[1][index],
                    X_train_df.iloc[index,:]))
        print()

        print('No Vote Class (2)')
        display(shap.force_plot(explainer.expected_value[2],
                    multi_shap_vals[2][index],
                    X_train_df.iloc[index,:]))

    elif classes == 'pred':
        print('Predicted: {} Class {}'.format(label_dict[pred], pred))
        display(shap.force_plot(explainer.expected_value[pred],
                                multi_shap_vals[pred][index],
                                X_train_df.iloc[index,:]))

    elif classes == 'true':
        print('True: {} Class {}'.format(label_dict[true_label], true_label))
        display(shap.force_plot(explainer.expected_value[true_label],
                    multi_shap_vals[true_label][index],
                    X_train_df.iloc[index,:]))

    elif classes == 'both':
        print('Predicted: {} Class {}'.format(label_dict[pred], pred))
        display(shap.force_plot(explainer.expected_value[pred],
                                multi_shap_vals[pred][index],
                                X_train_df.iloc[index,:]))
        print()

        print('True: {} Class {}'.format(label_dict[true_label], true_label))
        display(shap.force_plot(explainer.expected_value[true_label],
                    multi_shap_vals[true_label][index],
                    X_train_df.iloc[index,:]))
