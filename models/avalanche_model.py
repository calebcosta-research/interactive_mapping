"""Simplified avalanche risk model placeholder."""

import numpy as np


def predict_risk(snowfall: float, temp_gradient: float) -> float:
    """Return a dummy risk score based on input weather metrics."""
    # This is purely illustrative and not scientifically accurate.
    risk = snowfall * 0.5 + temp_gradient * 0.3
    return risk


if __name__ == "__main__":
    score = predict_risk(snowfall=30, temp_gradient=10)
    print(f"Risk score: {score:.2f}")
