# Getting Started

```bash
pip install neuronforge
```

```python
from neuronforge import Trainer, Adam, CosineScheduler
from neuronforge.tracking import Experiment

exp = Experiment("my-experiment")
run = exp.start_run({"lr": 1e-3, "epochs": 50})

trainer = Trainer(model, Adam(lr=1e-3), loss_fn)
history = trainer.fit(train_data, epochs=50)
run.finish()
```
