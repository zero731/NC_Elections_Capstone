## Define function for grouping birth state/country into categories
def get_birth_reg_census(state):
    
    if state in ['AS', 'GU', 'MP', 'PR', 'VI', 'OC']:
        return 'Other'
    
    # the rest of the categories are based on U.S. Census Bureau regions
    elif state in ['CT', 'ME', 'MA', 'NH', 'RI', 'VT',
                     'NJ', 'NY', 'PA']:
        return 'Northeast'
    
    elif state in ['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 
                     'DC', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR',
                     'LA', 'OK', 'TX']:
        return 'South'
    
    elif state in ['IL', 'IN', 'MI', 'OH', 'WI',
                     'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD']:
        return 'Midwest'
    
    elif state in ['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT',
                     'WY', 'AK', 'CA', 'HI', 'OR', 'WA']:
        return 'West'
    
    else:
        return 'Missing'


## Define function for grouping into generation categories by birth year
def get_gen_grp(birth_year):
    
    if birth_year < 1946:
        return 'Greatest-Silent'
    
    elif (birth_year > 1945) & (birth_year < 1965):
        return 'Boomer'
    
    elif (birth_year > 1964) & (birth_year < 1981):
        return 'GenX'
    
    elif (birth_year > 1980) & (birth_year < 1997):
        return 'Millennial'
    
    elif birth_year > 1996:
        return 'GenZ'
    
    else:
        return 'Missing'


## Define function for cleaning and preparing df for visualization
def clean_vreg(df):

    import pandas as pd
    import numpy as np

    # Recast registr_dt as datetime variable
    df['registr_dt'] = pd.to_datetime(df['registr_dt'])

    # Fill null values in birth_state with 'Missing'
    df['birth_state'].fillna(value='Missing', inplace=True)

    # Recast drivers_lic for sake of clarity in figures
    df['drivers_lic'] = np.where(df['drivers_lic']=='Y',
                                 'License',
                                 'No License')

    # Create new column grouping most infrequent party categories (<5% of voters)
      # into same group as those who are unaffiliated
    df['party_grp'] = np.where(df['party_cd'].isin(['REP', 'DEM']),
                               df['party_cd'].str.title(),
                               'Other')

    # Create new column grouping most infrequent race categories (<5% of voters)
    df['race_grp'] = np.where(df['race_code'].isin(['W', 'B', 'U']),
                              df['race_code'],
                              'O')
    
    race_grp_map = {'W': 'White',
                    'B': 'Black',
                    'U': 'Undesig.',
                    'O': 'Other'}
    
    df['race_grp'] = df['race_grp'].map(race_grp_map)

    # Create new column grouping most infrequent cities (<5% of voters)
    df['res_city_desc'].fillna('Missing', inplace=True)
    df['city_grp'] = np.where(df['res_city_desc'].isin(['MONROE', 
                                                        'WAXHAW',
                                                        'INDIAN TRAIL',
                                                        'MATTHEWS',
                                                        'Missing']),
                              df['res_city_desc'].str.title(),
                              'Other')

    # Create a new column grouping birth_state into U.S. Census regions,
      # lumping territories and out of country into 'Other'
    df['birth_reg_other'] = df['birth_state'].apply(get_birth_reg_census)

    # Create a new column grouping birth_year into generations, 
      # also lumping Silent in with Greatest
    df['gen_grp'] = df['birth_year'].apply(get_gen_grp)

    # Reformat voter_status_desc labels
    df['voter_status_desc'] = np.where(
        df['voter_status_desc']=='TEMPORARY',
        'Temp',
        df['voter_status_desc'].str.title())

    # Select only the necessary columns
    cleaned_df = df[['voter_status_desc', 'reason_cd', 'city_grp', 
             'race_grp', 'party_grp', 'gen_grp', 'gender_code', 
             'birth_age', 'birth_reg_other', 'drivers_lic',
             'registr_dt']].copy()
    
    return cleaned_df