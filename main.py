fname = "sample.ino"

lines = ""

def formatInitializer(s):
    values = s.replace(" = ", " ").split(" ")
    values[-1] = values[-1][:-1]
    return "//Declares a(n) {} variable called {} and stores {} in it.".format(values[0], values[1], values[2])

def formatPinMode(s):
    start = s.find("pinMode")
    values = s[start:].replace("(", " ").replace(");", "").split(" ");
    values[1] = values[1][:-1]
    return "//allow pin {} to {}".format(values[1], values[2].lower())

def formatDigitalWrite(s):
    start = s.find("digitalWrite")
    values = s[start:].replace("(", " ").replace(");", "").split(" ");
    return "//turn pin {} {}".format(values[1], "on" if values[2] == "HIGH" else "off")

with open(fname, 'r') as f:
    lines = f.read().split("\n")

for i in lines:
    if ("int" in i and " = " in i and "for" not in i):
        print(i, formatInitializer(i))
    if ("pinMode" in i):
        print(i, formatPinMode(i))
    if ("digitalWrite" in i):
        print(i, formatDigitalWrite(i))
