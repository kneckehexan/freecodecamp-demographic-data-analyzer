import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', nrows=10)

    df['age'] = pd.to_numeric(df['age'], downcast='unsigned')
    df['fnlwgt'] = pd.to_numeric(df['fnlwgt'], downcast='unsigned')
    df['education-num'] = pd.to_numeric(df['education-num'], downcast='unsigned')
    df['capital-gain'] = pd.to_numeric(df['capital-gain'], downcast='unsigned')
    df['capital-loss'] = pd.to_numeric(df['capital-loss'], downcast='unsigned')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], downcast='unsigned')
    df['age'] = pd.to_numeric(df['age'], downcast='unsigned')
    df['fnlwgt'] = pd.to_numeric(df['fnlwgt'], downcast='unsigned')
    df['education-num'] = pd.to_numeric(df['education-num'], downcast='unsigned')
    df['capital-gain'] = pd.to_numeric(df['capital-gain'], downcast='unsigned')
    df['capital-loss'] = pd.to_numeric(df['capital-loss'], downcast='unsigned')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], downcast='unsigned')
    df['workclass'] = df['workclass'].astype('category')
    df['education'] = df['education'].astype('category')
    df['marital-status'] = df['marital-status'].astype('category')
    df['occupation'] = df['occupation'].astype('category')
    df['relationship'] = df['relationship'].astype('category')
    df['race'] = df['race'].astype('category')
    df['sex'] = df['sex'].astype('category')
    df['native-country'] = df['native-country'].astype('category')
    df['salary'] = df['salary'].astype('category')

    dtypes = df.dtypes
    colnames = dtypes.index
    types = [i.name for i in dtypes.values]
    column_types = dict(zip(colnames, types))

    df = pd.read_csv('adult.data.csv', dtype=column_types)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(['race'])

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df['education'] == 'Bachelors'])/len(df.index) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_high = ['Bachelors', 'Masters', 'Doctorate']
#    higher_education = (df[df['education'].isin(edu_high)]['salary'] == '>50K').sum()
#    lower_education = (df[~df['education'].isin(edu_high)]['salary'] == '>50K').sum()
    higher_education = len(df.loc[df['education'].isin(edu_high)])
    lower_education = len(df.loc[~df['education'].isin(edu_high)])

    # percentage with salary >50K
    higher_education_rich = ((df.loc[df['education'].isin(edu_high)]['salary'] == '>50K').sum()/higher_education * 100).round(1)
    lower_education_rich = ((df.loc[~df['education'].isin(edu_high)]['salary'] == '>50K').sum()/lower_education * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = (df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').sum()/num_min_workers * 100


    # What country has the highest percentage of people that earn >50K?
    hec = pd \
        .value_counts(df.loc[df['salary'] == '>50K', 'native-country']) \
        .sort_index() \
        .div( \
            df \
            .groupby('native-country') \
            .size()) \
        .sort_values(ascending=False)
    highest_earning_country = hec.keys()[0]
    highest_earning_country_percentage = (hec[0]*100).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = pd.value_counts(
        df[ \
            (df['native-country'] == 'India') & 
            (df['salary'] == '>50K') \
        ]['occupation']) \
        .keys()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
