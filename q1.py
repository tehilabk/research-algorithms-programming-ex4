
def bounded_subset(S: list, C: int):
    ans = [[]]
    S.sort()
    for i in S:
        #if there us numbers that bigger than c - remove tham
        if i > C:
            S.remove(i)
    for j in S:
        checkSubset = [sub + [j] for sub in ans]
        # append the sub if the sum of the sub <C
        ans.extend(sub for sub in checkSubset if sum(sub) <= C)


    # yield the subset that been found
    for subset in ans:
        yield subset



