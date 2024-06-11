import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

class ExploratoryDataAnalysis:
    def __init__(self, df):
        self.df = df
         
    
    # def initial_inspection(self):
    #     try:
    #         print("First few rows of the dataset:")
    #         print(self.df.head())
    #         print("\nSummary statistics:")
    #         print(self.df.describe())
    #         print("\nData types and missing values:")
    #         print(self.df.info())
    #     except Exception as e:
    #         print(f"An error occurred during initial inspection: {e}")
    
    def handle_missing_values(self, strategy="mean"):
        try:
            missing_values = self.df.isnull().sum()
            print("\nMissing values per column:")
            print(missing_values)

            if strategy == "drop":
                self.df = self.df.dropna()
            elif strategy == "mean":
                self.df.fillna(self.df.mean(), inplace=True)
            elif strategy == "mode":
                self.df.fillna(self.df.mode().iloc[0], inplace=True)
            elif strategy == "median":
                self.df.fillna(self.df.median(), inplace=True)
            else:
                print("Unknown strategy! No missing values were handled.")
        except Exception as e:
            print(f"An error occurred while handling missing values: {e}")
    
    def detect_outliers(self, method="zscore"):
        try:
            if method == "zscore":
                z_scores = np.abs(stats.zscore(self.df.select_dtypes(include=np.number)))
                outliers = (z_scores >= 3)
                print(f"\nOutliers detected using Z-score method:\n{outliers.sum(axis=0)}")
                return outliers
            elif method == "iqr":
                Q1 = self.df.quantile(0.25)
                Q3 = self.df.quantile(0.75)
                IQR = Q3 - Q1
                outliers = ((self.df < (Q1 - 1.5 * IQR)) | (self.df > (Q3 + 1.5 * IQR)))
                print(f"\nOutliers detected using IQR method:\n{outliers.sum(axis=0)}")
                return outliers
            else:
                print("Unknown method! No outliers were detected.")
                return pd.DataFrame(False, index=self.df.index, columns=self.df.columns)
        except Exception as e:
            print(f"An error occurred during outlier detection: {e}")
            return pd.DataFrame(False, index=self.df.index, columns=self.df.columns)
    
    def treat_outliers(self, outliers):
        try:
            print("\nTreating outliers by removal.")
            self.df = self.df[~outliers.any(axis=1)]
            return self.df
        except Exception as e:
            print(f"An error occurred while treating outliers: {e}")
            return f"An error occurred while treating outliers: {e}"
    
    def univariate_analysis(self):
        try:
           
            histograms = self.df.hist(bins=30, figsize=(20, 15))
            plt.tight_layout()  # Adjust layout to avoid overlapping
            plt.show()
            
            print("\nGenerating Box plots:")
            plt.figure(figsize=(20, 15))
            boxplots = sns.boxplot(data=self.df)
            plt.xticks(rotation=90)  # Rotate x labels for better readability
            plt.tight_layout()  # Adjust layout to avoid overlapping
            plt.show()
            
            return histograms, boxplots
        except Exception as e:
            print(f"An error occurred during univariate analysis: {e}")
            return None, None

    
    def bivariate_analysis(self):
        try:
            print("\nGenerating Pair plot:")
            pairplot = sns.pairplot(self.df)
            plt.show()
            
            print("\nGenerating Correlation matrix heatmap:")
            corr_matrix = self.df.corr()
            plt.figure(figsize=(12, 8))
            heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
            plt.show()
            
            return pairplot, heatmap
        except Exception as e:
            print(f"An error occurred during bivariate analysis: {e}")
            return None, None
    