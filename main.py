import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from src.data_preparation import prepare_data
from src.statistical_tests import chi_square_test, calculate_effect_size, calculate_confidence_interval
from src.visualization import (plot_conversion_rates, plot_ads_distribution, 
                               plot_conversion_by_ads, plot_heatmap, plot_cumulative_conversions)
from src.advanced_analysis import segmentation_analysis, ad_fatigue_analysis, calculate_confidence_interval as calc_ci

def main():
    # Set up file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'raw', 'marketing_AB_test_data.csv')
    results_dir = os.path.join(current_dir, 'results')
    figures_dir = os.path.join(results_dir, 'figures')
    
    # Create results directories if they don't exist
    os.makedirs(figures_dir, exist_ok=True)

    # Prepare the data
    print("Preparing data...")
    df = prepare_data(data_path)

    # Print data info for debugging
    print("Data columns:", df.columns.tolist())
    print("Unique values in 'test group':", df['test group'].unique())

    # Perform statistical tests
    print("Performing statistical tests...")
    chi2, p_value = chi_square_test(df, 'test group', 'converted')
    risk_ratio, arr = calculate_effect_size(df, 'test group', 'converted')
    ci_lower, ci_upper = calculate_confidence_interval(df, 'test group', 'converted')

    # Create visualizations
    print("Creating visualizations...")
    
    plot_conversion_rates(df, 'test group', 'converted')
    plt.savefig(os.path.join(figures_dir, 'conversion_rates.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plot_ads_distribution(df)
    plt.savefig(os.path.join(figures_dir, 'ads_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plot_conversion_by_ads(df, 'test group', 'converted')
    plt.savefig(os.path.join(figures_dir, 'conversion_by_ads.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plot_heatmap(df, 'test group')
    plt.savefig(os.path.join(figures_dir, 'ad_views_heatmap.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plot_cumulative_conversions(df, 'test group', 'converted')
    plt.savefig(os.path.join(figures_dir, 'cumulative_conversions.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Additional analyses
    print("Performing advanced analyses...")
    
    day_conversion_fig = segmentation_analysis(df, 'test group', 'converted', 'most ads day')
    day_conversion_fig.savefig(os.path.join(figures_dir, 'conversion_by_day.png'), dpi=300, bbox_inches='tight')
    plt.close()

    hour_conversion_fig = segmentation_analysis(df, 'test group', 'converted', 'most ads hour')
    hour_conversion_fig.savefig(os.path.join(figures_dir, 'conversion_by_hour.png'), dpi=300, bbox_inches='tight')
    plt.close()

    ad_fatigue_fig = ad_fatigue_analysis(df, 'test group', 'converted')
    ad_fatigue_fig.savefig(os.path.join(figures_dir, 'ad_fatigue.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Calculate additional statistics
    ad_group = df[df['test group'] == 'ad']['converted']
    psa_group = df[df['test group'] == 'psa']['converted']
    ad_mean, psa_mean, ci_lower_diff, ci_upper_diff = calc_ci(ad_group, psa_group)

    # Get data for advanced analysis results
    day_conversion = df.groupby(['test group', 'most ads day'])['converted'].mean().unstack()
    hour_conversion = df.groupby(['test group', 'most ads hour'])['converted'].mean().unstack()
    
    df_ad = df[df['test group'] == 'ad']
    df_grouped = df_ad.groupby('total ads')['converted'].agg(['mean', 'count']).reset_index()
    df_grouped = df_grouped[df_grouped['count'] > 100]
    optimal_ads = df_grouped.loc[df_grouped['mean'].idxmax(), 'total ads']
    max_conversion_rate = df_grouped['mean'].max()

    # Write results to a text file
    results_file = os.path.join(results_dir, 'results.txt')
    with open(results_file, 'w') as f:
        f.write("A/B Testing Analysis Results\n")
        f.write("============================\n\n")
        f.write(f"Total sample size: {len(df)}\n")
        f.write(f"Ad group size: {len(df[df['test group'] == 'ad'])}\n")
        f.write(f"PSA group size: {len(df[df['test group'] == 'psa'])}\n\n")
        f.write("Conversion Rates:\n")
        f.write(f"Ad group: {ad_mean:.2%}\n")
        f.write(f"PSA group: {psa_mean:.2%}\n\n")
        f.write("Statistical Tests:\n")
        f.write(f"Chi-square statistic: {chi2:.4f}\n")
        f.write(f"p-value: {p_value:.4e}\n")
        f.write(f"Risk Ratio: {risk_ratio:.4f}\n")
        f.write(f"Absolute Risk Reduction: {arr:.4f}\n")
        f.write(f"95% Confidence Interval for difference in conversion rates: ({ci_lower:.4f}, {ci_upper:.4f})\n")
        f.write(f"95% Confidence Interval for absolute difference: ({ci_lower_diff:.2%}, {ci_upper_diff:.2%})\n\n")
        
        f.write("Segmentation Analysis:\n")
        f.write("Day of Week Conversion Rates:\n")
        f.write(day_conversion.to_string())
        f.write("\n\nBest performing days:\n")
        for group in day_conversion.index:
            best_day = day_conversion.loc[group].idxmax()
            best_rate = day_conversion.loc[group, best_day]
            f.write(f"{group}: {best_day} ({best_rate:.2%})\n")
        
        f.write("\nHour of Day Conversion Rates:\n")
        f.write(hour_conversion.to_string())
        f.write("\n\nBest performing hours:\n")
        for group in hour_conversion.index:
            best_hour = hour_conversion.loc[group].idxmax()
            best_rate = hour_conversion.loc[group, best_hour]
            f.write(f"{group}: {best_hour} ({best_rate:.2%})\n")
        
        f.write("\nAd Fatigue Analysis:\n")
        f.write(f"Optimal number of ads: {optimal_ads}\n")
        f.write(f"Maximum conversion rate: {max_conversion_rate:.2%}\n\n")
        
        f.write("Interpretation:\n")
        if p_value < 0.05:
            f.write(f"The difference in conversion rates between the ad and PSA groups is statistically significant (p < {p_value:.4e}).\n")
            if risk_ratio > 1:
                f.write(f"The ad campaign appears to be effective in increasing conversions. Users in the ad group are {(risk_ratio-1)*100:.1f}% more likely to convert than those in the PSA group.\n")
            else:
                f.write("The ad campaign does not appear to be effective in increasing conversions.\n")
        else:
            f.write(f"The difference in conversion rates between the ad and PSA groups is not statistically significant (p = {p_value:.4e}).\n")
            f.write("More data may be needed to draw a conclusive result.\n")
        

    print(f"Results written to {results_file}")
    print("Analysis complete. Check the results directory for output files.")

if __name__ == "__main__":
    main()