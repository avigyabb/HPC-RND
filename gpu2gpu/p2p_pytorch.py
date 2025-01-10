import os
import torch
import torch.distributed as dist

def init_process(rank, size, backend='nccl'):
  dist.init_process_group(backend, rank=rank, world_size=size)
  print(f"Process {rank} initialized.")

def send_and_receive(rank, size):
  device = torch.device(f"cuda:{rank}")
  tensor = torch.zeros(1, device=device)

  if rank == 0:
    tensor += 24
    print(f"Process {rank} sending tensor: {tensor.item()}")
    dist.send(tensor=tensor, dst=1)
  elif rank == 1:
    dist.recv(tensor=tensor, src=0)
    print(f"Process {rank} received tensor: {tensor.item()}")
  else: # process will hang on ranks that are waiting to recv
    print(f"Process {rank} has no specific task.")


def main():
    rank = int(os.environ['RANK'])
    size = int(os.environ['WORLD_SIZE'])
    init_process(rank, size, backend='nccl')
    send_and_receive(rank, size)
    dist.destroy_process_group()

if __name__ == "__main__":
    main()

