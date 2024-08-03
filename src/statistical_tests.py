import numpy as np
import scipy.stats as stats
import pandas as pd

def chi_square_test(df, group_col, target_col):
    """
    Perform chi-square test of independence.
    
    Args:
    df (pd.DataFrame): Input dataframe
    group_col (str): Name of the column containing group labels
    target_col (str): Name of the column containing target variable
    
    Returns:
    float: Chi-square statistic
    float: p-value
    """
    contingency_table = pd.crosstab(df[group_col], df[target_col])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2, p_value

def calculate_effect_size(df, group_col, target_col):
    """
    Calculate effect size (Risk Ratio and Absolute Risk Reduction).
    
    Args:
    df (pd.DataFrame): Input dataframe
    group_col (str): Name of the column containing group labels
    target_col (str): Name of the column containing target variable
    
    Returns:
    float: Risk Ratio
    float: Absolute Risk Reduction
    """
    group_rates = df.groupby(group_col)[target_col].mean()
    risk_ratio = group_rates['ad'] / group_rates['psa']
    arr = group_rates['ad'] - group_rates['psa']
    return risk_ratio, arr

def calculate_confidence_interval(df, group_col, target_col, confidence=0.95):
    """
    Calculate confidence interval for the difference in proportions.
    
    Args:
    df (pd.DataFrame): Input dataframe
    group_col (str): Name of the column containing group labels
    target_col (str): Name of the column containing target variable
    confidence (float): Confidence level (default 0.95 for 95% CI)
    
    Returns:
    tuple: Lower and upper bounds of the confidence interval
    """
    ad_data = df[df[group_col] == 'ad'][target_col]
    psa_data = df[df[group_col] == 'psa'][target_col]
    
    ad_mean = ad_data.mean()
    psa_mean = psa_data.mean()
    ad_var = ad_data.var()
    psa_var = psa_data.var()
    
    n_ad = len(ad_data)
    n_psa = len(psa_data)
    
    se = np.sqrt(ad_var/n_ad + psa_var/n_psa)
    
    z_score = stats.norm.ppf((1 + confidence) / 2)
    margin_of_error = z_score * se
    
    return (ad_mean - psa_mean - margin_of_error, ad_mean - psa_mean + margin_of_error)