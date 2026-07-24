# Day 1 Submission: Understanding Train/Test Split

**Student:** Khin Pwint Yati Maung  
**Workshop:** Example-Workshop  
**Day:** 1  
**Track:** AI / ML

---

## Part 1: Summary

A train/test split divides a dataset into two parts: a **training set** used to teach the model, and a **test set** held back for evaluation. The model should never “see” the test samples during learning. This setup measures **generalization**—how well the model performs on new data—rather than memorization of examples it already fitted.

Without a split, high accuracy on the same data used for training can hide **overfitting**, where the model captures noise instead of useful patterns. By reserving unseen test data, practitioners get a more honest estimate of real-world performance. Train/test splitting is therefore one of the first and most important habits in building trustworthy machine learning systems.

---

## Part 2: Split Results

**Dataset:** study hours → exam score (10 samples)  
**Method:** manual 80/20 split (first 8 train, last 2 test)  
**Model:** predict the mean of training scores (baseline model)

| Item | Value |
|------|-------|
| Train samples | 8 |
| Test samples | 2 |
| Train MAE | 8.75 |
| Test MAE | 7.50 |

See `dataset_split.py` for the data and split logic, and `evaluate_split.py` to run the evaluation.

---

## Part 3: Verification — Train vs Test Performance

| Evaluation set | MAE | Notes |
|----------------|-----|-------|
| Training set | 8.75 | Model was fitted using these labels’ average |
| Test set | 7.50 | Unseen samples; fairer estimate of performance |

In this tiny baseline example the scores are similar. If **train error were much lower than test error**, that would suggest overfitting: the model fits training data well but fails to generalize. Holding out a test set makes that gap visible before deploying a model.

### Write-Up

Train/test splits protect machine learning projects from misleading results. When evaluation uses only training data, a model can look excellent while failing on new inputs. Separating test data forces an honest check: if performance drops sharply, the model may be overfitting and needs simpler features, more data, or regularization. This practice builds trust with stakeholders because reported metrics reflect unseen cases, not memorized ones. Even simple projects benefit: a clear split, documented sizes, and side-by-side train/test metrics make experiments reproducible and decisions safer.
