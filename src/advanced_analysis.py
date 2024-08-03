import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def segmentation_analysis(df, group_col, target_col, segment_col):
    conversion = df.groupby([group_col, segment_col])[target_col].mean().unstack()
    plt.figure(figsize=(12, 6))
    
    if segment_col == 'most ads day':
        conversion.plot(kind='bar')
        plt.title('Conversion Rates by Day of Week', fontsize=16)
        plt.xlabel('Test Group', fontsize=12)
        plt.legend(title='Day of Week', title_fontsize='12', fontsize='10')
    elif segment_col == 'most ads hour':
        for group in conversion.index:
            plt.plot(conversion.columns, conversion.loc[group], marker='o', label=group)
        
        plt.title('Conversion Rates by Hour of Day', fontsize=16)
        plt.xlabel('Hour of Day', fontsize=12)
        plt.legend(title='Test Group', title_fontsize='12', fontsize='10', loc='upper left', bbox_to_anchor=(1, 1))
        
        # Set x-axis ticks to show all hours
        plt.xticks(range(24))
        
        # Add grid for better readability
        plt.grid(True, linestyle='--', alpha=0.7)
    else:
        raise ValueError(f"Unsupported segment column: {segment_col}")

    plt.ylabel('Conversion Rate', fontsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    plt.tight_layout()
    return plt.gcf()

def ad_fatigue_analysis(df, group_col, target_col):
    df_ad = df[df[group_col] == 'ad']
    df_grouped = df_ad.groupby('total ads')[target_col].agg(['mean', 'count']).reset_index()
    df_grouped = df_grouped[df_grouped['count'] > 100]  # Filter for reliability

    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df_grouped, x='total ads', y='mean', size='count', sizes=(20, 200))
    plt.title('Ad Fatigue Analysis', fontsize=16)
    plt.xlabel('Number of Ads Seen', fontsize=12)
    plt.ylabel('Conversion Rate', fontsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    plt.tight_layout()
    return plt.gcf()

def calculate_confidence_interval(ad_group, psa_group):
    ad_mean = ad_group.mean()
    psa_mean = psa_group.mean()
    ad_var = ad_group.var()
    psa_var = psa_group.var()
    n_ad = len(ad_group)
    n_psa = len(psa_group)
    
    pooled_se = np.sqrt(ad_var/n_ad + psa_var/n_psa)
    margin_of_error = 1.96 * pooled_se  # 95% confidence interval
    ci_lower = (ad_mean - psa_mean) - margin_of_error
    ci_upper = (ad_mean - psa_mean) + margin_of_error

    return ad_mean, psa_mean, ci_lower, ci_upper