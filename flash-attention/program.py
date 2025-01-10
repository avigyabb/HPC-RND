import torch

import triton
import triton.language as tl

def test_op(
  BATCH_SIZE: int, 
  NUM_HEADS: int, 
  SEQ_LEN: int, 
  HEAD_DIM: int, 
  causal, 
  dtype=torch.float(16)
):
  Q = (
    # creates a 4D tensor
    torch.empty((BATCH_SIZE, NUM_HEADS, SEQ_LEN, HEAD_DIM), dtype=dtype, device="cuda")
    .normal(mean=0.0, std=0.5)
    .requires_grad_()
  )

  K = (
    torch.empty((BATCH_SIZE, NUM_HEADS, SEQ_LEN, HEAD_DIM), dtype=dtype, device="cuda")
    .normal(mean=0.0, std=0.5)
    .requires_grad_()
  )
