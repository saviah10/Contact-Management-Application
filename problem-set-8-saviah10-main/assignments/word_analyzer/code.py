## TODO: your code here!

def analyze_file(filename):
    #error below - nts - maybe put "..." as f
    with open(filename, 'r') as f:
        # nts - read over files
        text = f.read()
    words = text.split()
        # nts - make a set
    uniquewords = set(words)
    return len(words), len(uniquewords)

# nts - add strip so its by itself
    filename = input("Enter the filename to analyze: ").strip()
#error below
    totalwords, uniquewords = analyze_file(filename)
    print(f"Total words: {totalwords}")
    print(f"Unique words: {uniquewords}")


def test_analyze():
    assert analyze_file('assignments/word_analyzer/dracula.txt') == (160284, 18158)