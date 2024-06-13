import pandas as pd
from sklearn.model_selection import train_test_split
from causalnex.structure import StructureModel
from causalnex.structure.notears import from_pandas
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import numpy as np


class CausalLearning:
    def __init__(self, data_path, target_variable):
        self.data_path = data_path
        self.target_variable = target_variable
        self.data = None
        self.train_data = None
        self.holdout_data = None
        self.sm = None
        self.direct_causes = None
        self.rf_all = None
        self.rf_causal = None
        self.xgb_all = None
        self.xgb_causal = None

    def load_data(self):
        self.data = pd.read_csv(self.data_path)
        self.data['Trip Start Time'] = pd.to_datetime(self.data['Trip Start Time'])
        self.data['Trip End Time'] = pd.to_datetime(self.data['Trip End Time'])
        self.train_data, self.holdout_data = train_test_split(self.data, test_size=0.2, random_state=42)

    def create_causal_graph(self):
        relevant_columns = ['Trip Origin', 'Trip Destination', 'Trip Start Time', 'Trip End Time', 'Holiday', 'Weekday']
        train_data_subset = self.train_data[relevant_columns]
        self.sm = from_pandas(train_data_subset, w_threshold=0.8)
        viz = plot_structure(self.sm, graph_attributes={"scale": "1.5"},
                             all_node_attributes=NODE_STYLE.WEAK,
                             all_edge_attributes=EDGE_STYLE.WEAK)
        viz.view()
        self.direct_causes = self.sm.get_parents(self.target_variable)
        print("Direct Causes of Target Variable:", self.direct_causes)

    def compare_causal_graphs(self):
        ground_truth_edges = set(self.sm.edges)
        fractions = [0.1, 0.2, 0.5, 0.8]
        jaccard_scores = []

        for frac in fractions:
            frac_data = self.train_data.sample(frac=frac, random_state=42)
            frac_sm = from_pandas(frac_data, w_threshold=0.8)
            frac_edges = set(frac_sm.edges)
            intersection = len(ground_truth_edges & frac_edges)
            union = len(ground_truth_edges | frac_edges)
            jaccard_scores.append(intersection / union)

        print("Jaccard Similarity Scores:", jaccard_scores)

    def train_models(self):
        features_all = self.train_data.drop(columns=[self.target_variable])
        features_causal = self.train_data[self.direct_causes]
        X_train_all, X_test_all, y_train, y_test = train_test_split(features_all, self.train_data[self.target_variable], test_size=0.2, random_state=42)
        X_train_causal, X_test_causal, _, _ = train_test_split(features_causal, self.train_data[self.target_variable], test_size=0.2, random_state=42)

        self.rf_all = RandomForestClassifier(random_state=42)
        self.rf_all.fit(X_train_all, y_train)
        self.rf_causal = RandomForestClassifier(random_state=42)
        self.rf_causal.fit(X_train_causal, y_train)
        
        self.xgb_all = XGBClassifier(random_state=42)
        self.xgb_all.fit(X_train_all, y_train)
        self.xgb_causal = XGBClassifier(random_state=42)
        self.xgb_causal.fit(X_train_causal, y_train)

        pred_rf_all = self.rf_all.predict(X_test_all)
        pred_rf_causal = self.rf_causal.predict(X_test_causal)
        pred_xgb_all = self.xgb_all.predict(X_test_all)
        pred_xgb_causal = self.xgb_causal.predict(X_test_causal)

        print("Random Forest (all features) Accuracy:", accuracy_score(y_test, pred_rf_all))
        print("Random Forest (causal features) Accuracy:", accuracy_score(y_test, pred_rf_causal))
        print("XGBoost (all features) Accuracy:", accuracy_score(y_test, pred_xgb_all))
        print("XGBoost (causal features) Accuracy:", accuracy_score(y_test, pred_xgb_causal))

    def evaluate_holdout(self):
        X_holdout_all = self.holdout_data.drop(columns=[self.target_variable])
        X_holdout_causal = self.holdout_data[self.direct_causes]
        y_holdout = self.holdout_data[self.target_variable]

        holdout_pred_rf_all = self.rf_all.predict(X_holdout_all)
        holdout_pred_rf_causal = self.rf_causal.predict(X_holdout_causal)
        holdout_pred_xgb_all = self.xgb_all.predict(X_holdout_all)
        holdout_pred_xgb_causal = self.xgb_causal.predict(X_holdout_causal)

        print("Random Forest (all features) Hold-out Accuracy:", accuracy_score(y_holdout, holdout_pred_rf_all))
        print("Random Forest (causal features) Hold-out Accuracy:", accuracy_score(y_holdout, holdout_pred_rf_causal))
        print("XGBoost (all features) Hold-out Accuracy:", accuracy_score(y_holdout, holdout_pred_xgb_all))
        print("XGBoost (causal features) Hold-out Accuracy:", accuracy_score(y_holdout, holdout_pred_xgb_causal))

# Usage
# pipeline = CausalLearningPipeline(data_path='path_to_your_dataset.csv', target_variable='Unfulfilled Requests')
# pipeline.load_data()
# pipeline.create_causal_graph()
# pipeline.compare_causal_graphs()
# pipeline.train_models()
# pipeline.evaluate_holdout()
