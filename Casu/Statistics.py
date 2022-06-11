import scipy.stats as stats

def TestNormalDistribution(DataDict):
    statistic1, p_shapiro1 = stats.shapiro(DataDict['Data1'])
    statistic2, p_ks1 = stats.kstest(DataDict['Data1'], 'norm', mode='exact')
    statistic3, p_shapiro2 = stats.shapiro(DataDict['Data2'])
    statistic4, p_ks2 = stats.kstest(DataDict['Data2'], 'norm', mode='exact')

    if p_shapiro1 >= 0.05 and p_ks1 >= 0.05 and p_shapiro2 >= 0.05 and p_ks2 >= 0.05:
        DataDict['norm'] = True
        return DataDict

    elif p_shapiro1 < 0.05 or p_ks1 < 0.05 or p_shapiro2 < 0.05 or p_ks2 < 0.05:
        DataDict['norm'] = False
        return DataDict

    elif p_ks1 >= 0.05 and p_ks2 >= 0.05:
        DataDict['norm'] = True
        return DataDict

def statisticalTestingDependent(DataDict):
    if DataDict['norm'] == True:
        statistic, p_val = stats.ttest_rel(DataDict['Data1'], DataDict['Data2'], alternative=DataDict['alternativ'])
        return f'The students-T-test for dependent dataset returns a p value of {p_val} with a statistic of {statistic}'
    elif DataDict['norm'] == False:
        statistic, p_val = stats.wilcoxon(DataDict['Data1'], DataDict['Data2'], zero_method='pratt', alternative=DataDict['alternativ'])
        return f'The Wilcoxen-Pratt signed rank test returns a p value of {p_val} with a statistic of {statistic}'

def statisticalTestingIndependent(DataDict):
    if DataDict['norm'] == True:
        statistic, p_lev = stats.levene(DataDict['Data1'], DataDict['Data2'])
        if p_lev >= 0.05:
            statistic, p_val = stats.ttest_ind(DataDict['Data1'], DataDict['Data2'], equal_var=True, alternative=DataDict['alternativ'])
            return f'The students-T-test with equal variance returns a p value of {p_val} with a statistic of {statistic}'
        elif p_lev < 0.05:
            statistic, p_val = stats.ttest_ind(DataDict['Data1'], DataDict['Data2'], equal_var=False, alternative=DataDict['alternativ'])
            return f'The students-T-test with no equal variance returns a p value of {p_val} with a statistic of {statistic}'
    elif DataDict['norm'] == False:
        statistic, p_val_man = stats.mannwhitneyu(DataDict['Data1'], DataDict['Data2'], use_continuity=True, alternative=DataDict['alternativ'])
        return f'The MannWhitney-U test returns a p value of {p_val_man} with a statistic of {statistic}'

def StatisticalTesting(DataDict):
    DataDict = TestNormalDistribution(DataDict)
    if DataDict['dependent'] == True:
        result = statisticalTestingDependent(DataDict)
        return result
    elif DataDict['dependent'] == False:
        result = statisticalTestingIndependent(DataDict)
        return result