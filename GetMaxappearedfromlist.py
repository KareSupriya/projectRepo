def solve(nums): 
  from collections import Counter
  e = Counter(nums)
  value, count = e.most_common()[0]
  return value
