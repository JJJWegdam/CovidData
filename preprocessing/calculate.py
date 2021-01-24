from pandas import Series


def weekly(new_cases_per_day: Series) -> (Series, Series):
    weekly_cases = Series(index=new_cases_per_day.index)
    weekly_change = Series(index=new_cases_per_day.index)
    for index, value in new_cases_per_day.iteritems():
        if index < 8:
            weekly_cases.iloc[index] = float('nan')
            weekly_change.iloc[index] = float('nan')
        else:
            weekly_cases.iloc[index] = new_cases_per_day.iloc[index - 6:index].sum()
            if new_cases_per_day.iloc[index-6-7:index-7].sum() != 0:
                weekly_change.iloc[index] = (new_cases_per_day.iloc[index-6:index].sum() /
                                             new_cases_per_day.iloc[index-6-7:index-7].sum()) - 1
            else:
                weekly_change.iloc[index] = 1
    return weekly_cases, weekly_change
