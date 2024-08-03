import matplotlib.pyplot as plt
import seaborn as sns

def plot_conversion_rates(df, group_col, target_col):
    conversion_rates = df.groupby(group_col)[target_col].mean()
    
    plt.figure(figsize=(10, 6))
    bars = sns.barplot(x=conversion_rates.index, y=conversion_rates.values, palette="deep")
    plt.title('Conversion Rates by Test Group', fontsize=16, fontweight='bold')
    plt.ylabel('Conversion Rate', fontsize=12)
    plt.xlabel('Test Group', fontsize=12)
    plt.ylim(0, max(conversion_rates.values) * 1.2)

    for i, v in enumerate(conversion_rates.values):
        bars.text(i, v, f'{v:.2%}', ha='center', va='bottom', fontweight='bold')

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.tight_layout()

def plot_ads_distribution(df):
    plt.figure(figsize=(14, 8))
    sns.histplot(data=df, x='total ads', hue='test group', stat='density', 
                 common_norm=False, kde=True, log_scale=(True, False))
    plt.title('Distribution of Total Ads Seen (Log Scale)', fontsize=16)
    plt.xlabel('Number of Ads (Log Scale)', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.legend(title='Test Group', title_fontsize='12', fontsize='10')
    
    # Calculate statistics
    stats = {}
    for group in df['test group'].unique():
        group_data = df[df['test group'] == group]['total ads']
        stats[group] = {
            'median': group_data.median(),
            'percentile_90': group_data.quantile(0.9)
        }

    # Plot vertical lines and add labels
    colors = {'ad': 'green', 'psa': 'red'}
    for i, (group, values) in enumerate(stats.items()):
        plt.axvline(values['median'], color=colors[group], linestyle='--', alpha=0.7)
        plt.axvline(values['percentile_90'], color=colors[group], linestyle=':', alpha=0.7)
        
        # Adjust y-position for labels to avoid overlap
        y_pos = plt.gca().get_ylim()[1] * (0.9 - i * 0.1)
        plt.text(values['median'], y_pos, f'{group} median: {values["median"]:.0f}', 
                 color=colors[group], ha='right', va='bottom', rotation=0)
        plt.text(values['percentile_90'], y_pos, f'{group} 90th percentile: {values["percentile_90"]:.0f}', 
                 color=colors[group], ha='left', va='bottom', rotation=0)

    plt.tight_layout()

def plot_conversion_by_ads(df, group_col, target_col):
    df_grouped = df.groupby(['total ads', group_col])[target_col].agg(['mean', 'count']).reset_index()
    df_grouped = df_grouped[df_grouped['total ads'] <= 500]  # Limit to 500 ads
    
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df_grouped, x='total ads', y='mean', hue=group_col, size='count', 
                    sizes=(20, 200), alpha=0.7)
    plt.title('Conversion Rate by Number of Ads Seen', fontsize=16)
    plt.xlabel('Number of Ads', fontsize=12)
    plt.ylabel('Conversion Rate', fontsize=12)
    plt.legend(title='Test Group', title_fontsize='12', fontsize='10')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))

def plot_heatmap(df, group_col):
    pivot = df[df[group_col] == 'ad'].pivot_table(
        values='user id', 
        index='most ads day', 
        columns='most ads hour', 
        aggfunc='count'
    )
    
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(days_order)
    
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Number of Users'})
    plt.title('Heatmap of Ad Views by Day and Hour', fontsize=16)
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Day of Week', fontsize=12)

def plot_cumulative_conversions(df, group_col, target_col):
    df_sorted = df.sort_values('user id')
    df_sorted['cumulative_conversions'] = df_sorted.groupby(group_col)[target_col].cumsum()
    df_sorted['cumulative_users'] = df_sorted.groupby(group_col).cumcount() + 1
    df_sorted['conversion_rate'] = df_sorted['cumulative_conversions'] / df_sorted['cumulative_users']
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()
    
    for group in df_sorted[group_col].unique():
        group_data = df_sorted[df_sorted[group_col] == group]
        ax1.plot(group_data['cumulative_users'], group_data['cumulative_conversions'], 
                 label=f'{group} (Cumulative)')
        ax2.plot(group_data['cumulative_users'], group_data['conversion_rate'], 
                 linestyle='--', label=f'{group} (Rate)')
    
    ax1.set_xlabel('Number of Users', fontsize=12)
    ax1.set_ylabel('Cumulative Conversions', fontsize=12)
    ax2.set_ylabel('Conversion Rate', fontsize=12)
    ax1.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)
    plt.title('Cumulative Conversions and Conversion Rates Over Time', fontsize=16)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))