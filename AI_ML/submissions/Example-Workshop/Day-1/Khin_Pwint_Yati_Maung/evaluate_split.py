"""
Day 1 — Evaluate a simple baseline using train/test split
Student: Khin Pwint Yati Maung

Run with:
    python evaluate_split.py
"""

from dataset_split import DATA, mean_absolute_error, train_test_split


def main():
    train, test = train_test_split(DATA, train_ratio=0.8)

    # Baseline model: always predict the mean training score
    train_scores = [row["score"] for row in train]
    test_scores = [row["score"] for row in test]
    prediction = sum(train_scores) / len(train_scores)

    train_preds = [prediction] * len(train_scores)
    test_preds = [prediction] * len(test_scores)

    train_mae = mean_absolute_error(train_scores, train_preds)
    test_mae = mean_absolute_error(test_scores, test_preds)

    print("=== Train/Test Split Demo ===")
    print(f"Train samples: {len(train)}")
    print(f"Test samples:  {len(test)}")
    print(f"Baseline prediction (train mean score): {prediction:.2f}")
    print(f"Train MAE: {train_mae:.2f}")
    print(f"Test MAE:  {test_mae:.2f}")
    print("\nNote: test MAE is the fairer estimate of real-world performance.")


if __name__ == "__main__":
    main()
