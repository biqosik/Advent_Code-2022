### DAY 7 ###
import collections

files = collections.defaultdict(int)
with open('data.txt') as file:
    line = next(file, None)
    while line:
        x = line.strip().split(" ")
        if x[1] == "cd":
            if x[2] == "/":
                path = ()
            elif x[2] == "..":
                path = path[:-1]
            else:
                path += (x[2],)
            line = next(file, None)
        elif x[1] == "ls":
            while True:
                line = next(file, None)
                if not line or line.startswith("$"):
                    break
                detail, name = line.split(" ")
                if detail == "dir":
                    continue
                for i in range(len(path)+ 1):
                    files[path[: len(path) - i]] += int(detail)
print(files)
print(sum(size for size in files.values() if size <= 100000))


total = files[()]
print(min(s for s in files.values() if total - s <= 70000000 - 30000000))
