f = open("nsnd.txt", "r", encoding="utf8")
lines = [line.replace("\n", "") for line in f.readlines()]
f.close()
with open("nghe_si_nhan_dan.txt", "w", encoding="utf8") as f:
    for line in lines:
        new_line = line.split("-")[0].split("(")[0]
        f.write(new_line + "\n")