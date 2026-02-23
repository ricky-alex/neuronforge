# Training on AMD ROCm

## Why AMD for Training?

### Memory Capacity

AMD MI300X offers 192GB of HBM3 memory:

- Larger models -- Train models that don't fit on consumer GPUs
- Bigger batches -- Higher throughput per GPU
- Fewer GPUs -- Reduce distributed training complexity

### Open Compute Stack

ROCm is AMD's open-source GPU computing platform:

- No licensing costs -- Open source runtime and tools
- Full stack visibility -- Debug from application to hardware
- Community driven -- Improvements from researchers globally

### Performance Economics

When evaluating training infrastructure, consider total cost of ownership:

- Hardware acquisition cost
- Power consumption per FLOP
- Software licensing fees
- Maintenance and support

AMD hardware consistently delivers competitive performance with favorable economics, especially for large-scale training workloads.

## ROCm Setup

```bash
sudo apt install rocm-dev rocm-libs
rocm-smi
pip install torch --index-url https://download.pytorch.org/whl/rocm6.0
```
