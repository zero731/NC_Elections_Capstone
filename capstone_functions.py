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
    unique_vals['%'] = pd.Series(df[col].value_counts(normalize=True, dropna=dropna))
    
    return unique_vals





def plot_count(feature, hue, data, show_legend=True):
    
    """Takes in a feature/ column name, the DataFrame containing the column, and the target variable 
    (default for this notebook is 'Gen_2020') and returns a barplot for that feature grouped by
    voting method.
    """
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    plt.figure(figsize=(8,6))
    fig = sns.countplot(x=feature,
                        palette='nipy_spectral',
                        hue=hue,
                        data=data)
    fig.set_title('Voting Method vs {}'.format(feature), fontsize=16, weight='bold')
    fig.set_xlabel('Voting Method', fontsize=14, weight='bold')
    fig.set_ylabel(feature.title(), fontsize=14, weight='bold')
    
    if show_legend==False:
        fig.get_legend().remove()
    
    return fig






def eval_classifier(clf, X_test, y_test, model_descr='',
                    target_labels=['Hate Speech', 'Offensive', 'Neither'],
                    cmap='Blues', normalize='true', save=False, fig_name=None):
    
    """Given an sklearn classification model (already fit to training data), test features, and test labels,
       displays sklearn.metrics classification report and confusion matrix. A description of the model 
       can be provided to model_descr to customize the title of the classification report.
       
       
    Args:
        clf (estimator): Fitted classifier.
        X_test (series or array): Subset of X data used for testing.
        y_test (series or array): Subset of y data used for testing.
        model_descr (str): A description of the model for customizing plot title.
        target_labels (list of strings, default=['Hate Speech', 'Offensive', 'Neither']): List of class labels 
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
                    target_labels=['Hate Speech', 'Offensive', 'Neither'],
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





def plot_feat_importance(clf, clf_step_name, vec_step_name, model_title='', save=False, fig_name=None):
    
    """Takes in an sklearn classifier already fit to training data, the name of the step for that model
       in the modeling pipeline, the vectorizer step name, and optionally a title describing the model. 
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
        >>> plot_feat_importance(clf=my_model, clf_step_name='clf', vec_step_name='vec',
                                 model_title='My Model', save=True, fig_name='my_model_feat_import')
    
    """

    import pandas as pd
    from sklearn.model_selection import GridSearchCV
    import matplotlib.pyplot as plt
    
    fig_filepath = 'Figures/'
    
    feature_importances = (
        clf.named_steps[clf_step_name].feature_importances_)
    
    feature_names = (
        clf.named_steps[vec_step_name].vocabulary_) 
    
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






def plot_coefficients(clf, clf_step_name, vec_step_name,
                      class_label, model_title='', top_features=10,
                      save=False, fig_name=None):
    
    """Takes in an sklearn classifier already fit to training data, the name of the step for that model
       in the modeling pipeline, the vectorizer step name, a class label, and optionally a title describing the model. 
       Returns a horizontal barplot showing the top 20 most important features by coefficient weight (10 most 
       positive and 10 most negative).
       
    Args:
        clf (estimator): An sklearn Pipeline with a vectorizer steps and final step is a fitted classifier.
        clf_step_name (str): The name given to the classifier step of the pipe.
        vec_step_name (str): The name given to the vectorizer step of the pipe.
        class_label (int): Integer representing numerically encoded class of interest.
        model_title (str): A description of the model for customizing plot title.
        top_features (int, default=10): Number of top positive and top negative coefficients to plot
            (so default of 10 returns bar plot with 20 bars total).
        save (bool, default=False): Whether to save the returned figure.
        fig_name (str, optional): What to name the file if the image is being saved.
    
    Returns:
        figure: Matplotlib.pyplot bar plot figure showing the coefficient weights for the top
            20 most important features.
    
    Example:
        >>> plot_coefficients(clf=my_model, clf_step_name='clf', vec_step_name='vec',
                                 class_label=0, model_title='My Model', top_features=10,
                                 save=True, fig_name='my_model_coeffs')
    
    """
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    fig_filepath = 'Figures/'
    
    ## Get the coefficients for the specified class label
    feature_coefs = (
        clf.named_steps[clf_step_name].coef_[class_label])
    
    ## Get the vocabulary from the fit vectorizer
    feature_names = (
        clf.named_steps[vec_step_name].vocabulary_) 
    # Create a version of the vocab dict with keys and values swapped
    vocab_swap = (
        {value:key for key, value in feature_names.items()}) 

    
    ## Store the top 10 positive coefficients and their indices
    pos_10_index = (
        np.argsort(clf.named_steps[clf_step_name].coef_[class_label])[-top_features:])
    pos_10_coefs = (
        np.sort(clf.named_steps[clf_step_name].coef_[class_label])[-top_features:])
    
    ## Store the top 10 negative coefficients and their indices
    neg_10_index = (
        np.argsort(clf.named_steps[clf_step_name].coef_[class_label])[:top_features])
    neg_10_coefs = (
        np.sort(clf.named_steps[clf_step_name].coef_[class_label])[:top_features])
    
    ## Combine top positive and negative into one list for indices and one for coefs
    top_20_index = list(pos_10_index) + list(neg_10_index)
    top_20_coefs = list(pos_10_coefs) + list(neg_10_coefs)

    
    ## Get list of top predictive words and use it as index for series of coef values
    top_words = []

    for i in top_20_index:
        top_words.append(vocab_swap[i])

    top_20 = pd.Series(top_20_coefs, index=top_words)
    
    
    ## Create plot
    plt.figure(figsize=(8,6))
    
    # Color code positive coefs blue and negative red
    colors = ['blue' if c < 0 else 'red' for c in top_20]
    
    # Adjust title according to specified class code
    class_dict = {0: 'Hate Speech', 1: 'Offensive Language', 2: 'Neither'}
    title_class = class_dict[class_label]
    
    fig = top_20.sort_values().plot(kind='barh', color=colors)
    fig.set_title('Top Words for Predicting {} - {}'.format(title_class, model_title),
                  fontsize=18, fontweight='bold')
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12)
    
    if save:
        plt.savefig(fig_filepath+fig_name+'_'+title_class.replace(' ', '_'), bbox_inches = "tight")
    
    plt.show()
    
    return fig

