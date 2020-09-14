def worker(x):
    return x*x
def simple_configs(max_length, offsets=[1]):
 configs = list()
 for i in range(1, max_length+1):
  for o in offsets:
   for t in ['persist', 'mean', 'median']:
    cfg = [i, o, t]
    configs.append(cfg)
 return configs