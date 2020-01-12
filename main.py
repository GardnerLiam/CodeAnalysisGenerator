import sys
fname = sys.argv[1]

lines = ""

comments = [
        "//allow pin {} to {}",
        "//turn pin {} {}",
        "//write a value of {} in pin {}"
        ]

def formatInitializer(s):
    values = s.replace(" = ", " ").split(" ")
    values[-1] = values[-1][:-1]
    return "//Declares a(n) {} variable called {} and stores {} in it.".format(values[0], values[1], values[2])

def formatDelay(s):
    time = int(s[s.find("delay"):].replace("(", " ").replace(");", "").split(" ")[-1])
    return "//pause program for {} milliseconds".format(time)

def formatAnalogWrite(s):
    start = s.find("analogWrite")
    values = s[start:].replace("(", " ").replace(");", "").split(" ")
    return "//write a value of {} in pin {}".format(values[-1], values[1])

def formatPinCommand(s, command, index):
    global comments
    start = s.find(command)
    values = s[start:].replace("(", " ").replace(");", "").split(" ")
    if (values[-1] == "HIGH"):
        values[-1] = "on"
    if (values[-1] == "LOW"):
        values[-1] = "off"
    values[-1] = values[-1].lower()
    return comments[index].format(values[1], values[-1])

with open(fname, 'r') as f:
    lines = f.read().split("\n")
newtext = ""
for i in lines:
    if ("int" in i and " = " in i and "for" not in i):
        newtext += i + formatInitializer(i)
    elif ("delay" in i):
        newtext += i + formatDelay(i)
    elif ("pinMode" in i):
        newtext += i + formatPinCommand(i, "pinMode", 0)
    elif ("digitalWrite" in i):
        newtext += i + formatPinCommand(i, "digitalWrite", 1)
    elif ("analogWrite" in i):
        newtext += i + formatPinCommand(i, "analogWrite", 2)
    else:
        newtext += i
    newtext += "\n"
with open("edit-"+fname, 'w') as f:
    f.write(newtext)

