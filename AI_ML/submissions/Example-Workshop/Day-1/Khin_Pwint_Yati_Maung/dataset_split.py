"""
Day 1 — Dataset and train/test split helpers
Student: Khin Pwint Yati Maung
Track: AI / ML
"""

# Simple dataset: hours studied → exam score
DATA = [
    {"hours": 1, "score": 45},
    {"hours": 2, "score": 50},
    {"hours": 3, "score": 55},
    {"hours": 4, "score": 60},
    {"hours": 5, "score": 68},
    {"hours": 6, "score": 72},
    {"hours": 7, "score": 78},
    {"hours": 8, "score": 85},
    {"hours": 9, "score": 90},
    {"hours": 10, "score": 95},
]


def train_test_split(data, train_ratio=0.8):
    """Manual split: first train_ratio of samples → train, rest → test."""
    split_index = int(len(data) * train_ratio)
    train = data[:split_index]
    test = data[split_index:]
    return train, test


def mean_absolute_error(y_true, y_pred):
    errors = [abs(t - p) for t, p in zip(y_true, y_pred)]
    return sum(errors) / len(errors)
