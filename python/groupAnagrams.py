from typing import List
from collections import defaultdict

def groupAnagrams(strs:List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
res = groupAnagrams(strs)
print(res)
    