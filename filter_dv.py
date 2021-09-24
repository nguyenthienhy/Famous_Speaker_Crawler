f = open("dv.txt", "r", encoding="utf8")
lines = [line.replace("\n", "") for line in f.readlines()]
f.close()
with open("dv.txt", "w", encoding="utf8") as f:
    for line in lines:
        if len(line.split()) > 1:
            f.write(line + "\n")