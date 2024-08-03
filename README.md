# A/B Testing Analysis: Optimizing Ad Campaign Performance

## Table of Contents
1. [Project Overview](#project-overview)
   - [Dataset](#dataset)
   - [Key Questions](#key-questions)
2. [Tools and Technologies Used](#tools-and-technologies-used)
3. [Project Structure](#project-structure)
4. [Methodology](#methodology)
5. [Detailed Graph Analysis](#detailed-graph-analysis)
   - [Distribution of Total Ads Seen](#1-distribution-of-total-ads-seen-ads_distributionpng)
   - [Conversion Rates by Test Group](#2-conversion-rates-by-test-group-conversion_ratespng)
   - [Conversion Rates by Day of Week](#3-conversion-rates-by-day-of-week-conversion_by_daypng)
   - [Conversion Rates by Hour of Day](#4-conversion-rates-by-hour-of-day-conversion_by_hourpng)
   - [Ad Fatigue Analysis](#5-ad-fatigue-analysis-ad_fatiguepng)
   - [Cumulative Conversions Over Time](#6-cumulative-conversions-over-time-cumulative_conversionspng)
   - [Heatmap of Ad Views by Day and Hour](#7-heatmap-of-ad-views-by-day-and-hour-ad_views_heatmappng)
7. [How to Run the Analysis](#how-to-run-the-analysis)
8. [Contact](#contact)
   
## Project Overview

This project analyzes the results of an A/B test conducted for a digital advertising campaign. The primary goal was to determine the effectiveness of the ad campaign compared to a control group shown Public Service Announcements (PSAs) and to identify optimal strategies for ad delivery.

### Dataset

- Total sample size: 588,101 user interactions
- Ad group size: 564,577
- PSA group size: 23,524

### Key Questions

1. Does the ad campaign significantly increase conversion rates?
2. Are there specific days or times when the ad campaign is most effective?
3. Is there an optimal number of ad exposures for maximizing conversions?
4. How does user behavior differ between the ad group and the control group?

## Tools and Technologies Used

- Python 3.8+
- Pandas for data manipulation
- NumPy for numerical computing
- Matplotlib and Seaborn for data visualization
- SciPy for statistical analysis

## Project Structure
```bash
ab-testing-analysis/
│
├── data/
│   ├── raw/
│   │   └── marketing_AB_test_data.csv
│   └── processed/
│       └── processed_AB_test_data.csv
│
├── src/
│   ├── data_preparation.py
│   ├── statistical_tests.py
│   ├── visualization.py
│   └── advanced_analysis.py
│
├── results/
│   ├── figures/
│   │   ├── ad_fatigue.png
│   │   ├── ad_views_heatmap.png
│   │   ├── ads_distribution.png
│   │   ├── conversion_by_ads.png
│   │   ├── conversion_by_day.png
│   │   ├── conversion_by_hour.png
│   │   ├── conversion_rates.png
│   │   └── cumulative_conversions.png
│   └── results.txt
│
├── requirements.txt
├── main.py
└── README.md
```
## Methodology

Our analysis followed a structured approach to ensure thorough and unbiased results:

1. Data Preparation
   - Loaded the raw dataset (588,101 user interactions)
   - Cleaned the data, handling any missing values or inconsistencies
   - Created derived features as needed for analysis

2. Exploratory Data Analysis (EDA)
   - Calculated basic statistics for ad and PSA groups
   - Visualized the distribution of ads seen by users
   - Examined initial conversion rates for both groups

3. Statistical Analysis
   - Performed chi-square test to determine statistical significance of conversion rate differences
   - Calculated risk ratio and absolute risk reduction to quantify the effect of the ad campaign
   - Computed confidence intervals for the difference in conversion rates

4. Segmentation Analysis
   - Analyzed conversion rates by day of the week
   - Examined conversion rates by hour of the day
   - Investigated the relationship between number of ads seen and conversion rate (ad fatigue analysis)

5. Visualization
   - Created various plots to illustrate key findings:
     - Conversion rates comparison
     - Distribution of total ads seen
     - Conversion rates by day and hour
     - Ad fatigue analysis
   - Iteratively improved visualizations for clarity and insight

6. In-depth Analysis
   - Examined each visualization to extract key insights
   - Compared performance between ad and PSA groups across different dimensions
   - Identified patterns and trends in the data

7. Recommendations Formulation
   - Based on the insights from our analysis, developed actionable recommendations
   - Focused on practical steps to optimize the ad campaign's performance

8. Results Compilation
   - Summarized key findings and insights
   - Compiled visualizations, statistical results, and recommendations into a comprehensive report

Throughout this process, we maintained a focus on the core questions of the A/B test:
- Is the ad campaign effective in increasing conversions?
- How do conversion rates vary across different times and exposure levels?
- What strategies can be employed to optimize the campaign's performance?

By following this structured approach, we ensured a comprehensive analysis that provides valuable insights for decision-making and campaign optimization.

## Detailed Graph Analysis

### 1. Distribution of Total Ads Seen (ads_distribution.png)
![ads_distribution](https://github.com/user-attachments/assets/e597c4b6-d137-46d4-998f-bbe37332e028)

**Analysis:**
This graph shows the distribution of the number of ads seen by users in both the ad and PSA groups. The x-axis represents the number of ads, while the y-axis shows the density of users who saw that number of ads.

**Key Insights:**
- The distribution is right-skewed for both groups, indicating that most users see a relatively small number of ads.
- The ad group has a wider distribution and a higher median number of ads seen compared to the PSA group.
- There's a long tail in the ad group, suggesting some users are exposed to a very high number of ads.

**Recommended Action:**
- Implement a more balanced ad exposure strategy to ensure a more uniform distribution.
- Set up frequency caps to limit over-exposure for users in the long tail.

### 2. Conversion Rates by Test Group (conversion_rates.png)

![conversion_rates](https://github.com/user-attachments/assets/a06fee5a-bf7c-494b-a292-a0e8fe3b3183)


**Analysis:**
This bar chart compares the overall conversion rates between the ad group and the PSA (control) group.

**Key Insights:**
- The ad group shows a significantly higher conversion rate (2.55%) compared to the PSA group (1.79%).
- The difference represents a 43.1% increase in conversion rate for the ad group.

**Recommended Action:**
- Continue and potentially expand the ad campaign given its clear positive impact on conversion rates.
- Investigate the characteristics of the ads that led to this success for future campaign designs.

### 3. Conversion Rates by Day of Week (conversion_by_day.png)

![conversion_by_day](https://github.com/user-attachments/assets/95f6181e-7f57-4530-8031-f3eb15a4fd72)


**Analysis:**
This graph shows how conversion rates vary across different days of the week for both the ad and PSA groups.

**Key Insights:**
- Monday and Tuesday show the highest conversion rates for both groups.
- The ad group consistently outperforms the PSA group across all days.
- Weekends (Saturday and Sunday) show the lowest conversion rates.

**Recommended Action:**
- Increase ad budget allocation for Mondays and Tuesdays by 20-25%.
- Develop weekend-specific ad creatives to improve performance on Saturdays and Sundays.

### 4. Conversion Rates by Hour of Day (conversion_by_hour.png)
![conversion_by_hour](https://github.com/user-attachments/assets/4e060176-6e2b-433e-bc4c-50808bc23c57)


**Analysis:**
This graph illustrates how conversion rates change throughout the day for both the ad group and the PSA (control) group.

**Key Insights:**

- The ad group consistently outperforms the PSA group across all hours.
- Peak performance for both groups occurs between 4-6 PM, with the ad group reaching about 3.1% conversion rate.
- Both groups show strong performance from 2 PM to 9 PM.
- Early morning hours (12 AM to 5 AM) show the lowest conversion rates for both groups.
- The ad group maintains some conversions during low-performing hours, while the PSA group drops to near-zero.

**Recommended Actions:**

- Increase ad budget and frequency during peak hours, especially between 4-6 PM.
- Develop a targeted ad strategy for the 2 PM to 9 PM window to capitalize on high performance.
- Create specialized ad content for early morning hours (12 AM to 5 AM) to improve performance during this low-converting period.

### 5. Ad Fatigue Analysis (ad_fatigue.png)

![ad_fatigue](https://github.com/user-attachments/assets/e2d52a26-25e8-498a-b952-f4282c3eae32)


**Analysis:**
This scatter plot shows the relationship between the number of ads seen and the conversion rate.

**Key Insights:**
- Conversion rates initially increase with more ad exposures.
- The optimal number of ad exposures is around 160, achieving a maximum conversion rate of 24.41%.
- After the optimal point, there's a slight decline in effectiveness, indicating potential ad fatigue.

**Recommended Action:**
- Aim for an average of 160 ad exposures per user over the campaign duration.
- Implement a gradual exposure plan to reach this optimal number without causing early fatigue.

### 6. Cumulative Conversions Over Time (cumulative_conversions.png)

![cumulative_conversions](https://github.com/user-attachments/assets/f11ba9ce-644b-4761-aaf1-6e5048bf2275)


**Analysis:**
This line graph shows the cumulative number of conversions over time for both groups.

**Key Insights:**
- The ad group shows a consistently higher rate of cumulative conversions.
- The gap between the ad and PSA group performance widens as the campaign progresses.
- There's no sign of the ad campaign losing effectiveness over time.

**Recommended Action:**
- Continue the campaign with the current strategy, as it shows sustained effectiveness.
- Consider extending the campaign duration to capitalize on the growing performance gap.

### 7. Heatmap of Ad Views by Day and Hour (ad_views_heatmap.png)

![ad_views_heatmap](https://github.com/user-attachments/assets/60213e80-4069-48ed-95e6-ab0aec3b7a2e)


**Analysis:**
This heatmap visualizes the concentration of ad views across different days of the week and hours of the day.

**Key Insights:**
- Weekday afternoons and evenings show the highest concentration of ad views.
- Late night and early morning hours have the lowest ad view counts.
- There's a noticeable drop in ad views during weekend mornings.

**Recommended Action:**
- Align ad scheduling with the high-density areas of the heatmap.
- Create strategies to increase engagement during low-density periods, especially on weekends.

## How to Run the Analysis

1. Clone this repository:
2. Install required packages:
pip install -r requirements.txt
3. Extract the .zip file in data to get the csv files required.
4. Run the main analysis script:
python main.py
5. Check the `results` folder for output files and visualizations.

## Future Work

- Conduct user segmentation based on demographics or behavior
- Analyze long-term user value post-conversion
- Implement multivariate testing for ad content optimization

## Contact

- Walid Benzineb - benzinebwal@gmail.com
