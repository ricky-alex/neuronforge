# Hyperparameter Search

## Grid Search

Exhaustively evaluates all combinations.

## Random Search

Samples random combinations for large parameter spaces.

```python
from neuronforge.search import GridSearch

grid = GridSearch({
    "lr": [1e-4, 1e-3, 1e-2],
    "batch_size": [16, 32, 64],
})
result = grid.run(objective_fn)
```
