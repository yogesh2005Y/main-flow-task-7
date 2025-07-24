def partition(s):
    result = []

    def backtrack(start=0, path=[]):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            part = s[start:end]
            if part == part[::-1]:
                backtrack(end, path + [part])

    backtrack()
    return result

print(partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
