# Task: Understanding Train/Test Split

## Objective

The goal of this task is to help you understand why machine learning models must be evaluated on unseen data, and how a train/test split supports fair model evaluation.

## Background

In machine learning, a model learns patterns from data. If you train and evaluate on the same data, you may get an overly optimistic score that does not reflect real-world performance. A **train/test split** separates data into a training set (used to learn) and a test set (used only to evaluate). This is a foundational practice for measuring generalization.

## Task Instructions

### Part 1: Understanding the Basics

1. **Research**:

   - Look up the definition of train/test split.
   - Understand the terms: training set, test set, overfitting, and generalization.
   - Find out why evaluating on unseen data matters.

2. **Summarize**:
   - Write a short paragraph (100–150 words) explaining what a train/test split is and why it is used in machine learning.

### Part 2: Performing a Simple Split

1. **Data Preparation**:

   - Create a small dataset of at least **10** samples (you may invent simple numeric features, e.g. study hours → exam score).

2. **Split the Data**:

   - Split into roughly **80% training** and **20% test** data.
   - You may do this manually or with a library (e.g. scikit-learn’s `train_test_split`). State which method you used.

3. **Simple Model**:

   - Fit a very simple model on the training set only (e.g. predict the average training target, or a simple linear relationship).
   - Evaluate on the test set using a basic metric (e.g. Mean Absolute Error).

4. **Structured Representation**:
   - Present a table showing: number of train samples, number of test samples, train metric, and test metric.

### Part 3: Verification

1. **Compare Fair vs Unfair Evaluation**:

   - Compute the same metric when evaluating on the **training** set versus the **test** set.
   - Explain what a large gap between train and test performance might mean.

2. **Write-Up**:
   - Write a short explanation (100–150 words) on how train/test splits help detect overfitting and improve trust in model results.

## Deadline

- Submit your completed task by 12PM Tomorrow.

## Resources

- [Train–test split – Wikipedia](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [scikit-learn: train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

---

Good luck!
