import sys
import torch
import torch.nn.functional as F

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
algo, _, *data = open(in_file).read().splitlines()

algo = torch.Tensor([x == "#" for x in algo])
img = torch.Tensor([[x == "#" for x in y] for y in data])[None, None]
kernel = torch.Tensor([1 << (8-i) for i in range(9)]).view(1,1,3,3)

def enhance(img, pad):
    img = F.pad(img, (2,)*4, 'constant', value=pad)
    conv_img = F.conv2d(img, kernel).long()
    out_img = algo[conv_img]
    return out_img
 
# Part 1 & 2
for step in range(50):
    img = enhance(img, pad=step%2)
    if (step == 1): print(img.sum())

print(img.sum())