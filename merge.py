def srt(left,right):
    x = []
    i = j = 0
    while i < len(left) and j < len(right):
      if left[i]<=right[j]:
        x.append(left[i])
        i+=1
      else:
        x.append(right[j])
        j+=1
    while i < len(left):
      x.append(left[i])
      i+=1
    while j < len(right):
      x.append(right[j])
      j+=1
    return x

def merge(l):
    if len(l) == 1:
        return l
    left = l[:len(l)//2]
    right = l[len(l)//2:]
    return srt(merge(left),merge(right))

l = [10,7,3,2,7,9,2,1,11]

print(merge(l))
