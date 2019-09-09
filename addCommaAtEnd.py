import re
def simplify_spaces(s):
    return re.sub('\s+', ' ', s)

def strip_comments(text):
    return re.sub('//.*?\n|/\*.*?\*/', '', text, flags=re.S)

def strip_source(source):
    source = (line.strip() for line in source.split('\n'))
    source = (simplify_spaces(line).strip() for line in source)
    source = (line for line in source if line != '' or line.startswith('//'))
    source = strip_comments('\n'.join(source))
    return source

if __name__ == "__main__":
    filename = '/Users/arunkumar/RegressionDetection/fuzzball/vocabulary.json'
    f = open(filename, "r")
    final = []
    lines = f.read()
    # lines = strip_source(lines)
    # print(lines)
    for line in lines:
        m = re.match("(.*)\}$", line)
        # if line == m:
        # print(line)
        if m is not None and line != " ":
            # print(line)
            line = line + ','
            final.append(line)
        else:
            final.append(line)
            # print(line)
    a = (''.join(final))
    f = open(filename, "w")
    f.write(a)
    f.close()