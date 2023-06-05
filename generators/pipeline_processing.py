def read_lines(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def parse_lines(lines):
    for line in lines:
        for word in line.split():
            yield word


def count_words(words):
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        yield counts


with open("file.txt", "r") as f:
    lines = read_lines(f)
    words = parse_lines(lines)
    counts = count_words(words)
    for count in counts:
        print(count)
