"""Hyperparameter search example."""

from neuronforge.search import GridSearch

grid = GridSearch({"lr": [1e-4, 1e-3, 1e-2]})
print("Grid search ready")
