import importlib

filename = 'List_II_64_01'
pyfile = './Desktop/GenQuiz/' + filename + '.py'
prob = importlib.import_module(filename)

f = open(pyfile, 'r')
j = 0
i = 0
write_mode = False

for line in f:
    if "# Problem" in line:
        write_mode = False
        i = i+1
        j = 0

    if write_mode:
        j = j+1
        command = line.replace('print(', 'prob.')
        try:
            out = eval(command[:-2])
            out = str(out) + "\n"

            fin = open(filename + "_" + str(j) + '_input.txt', 'w')
            fin.write(line)

            fout = open(filename + "_" + str(j) + '_output.txt', 'w')
            fout.write(out)
        except:
            continue

    if "# Test cases" in line:
        write_mode = True
