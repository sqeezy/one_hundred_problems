import sys
import os

usage = "count_words_and_lines [filepath]"
countWords = 0
countLines = 0

if len(sys.argv)!=2:
    sys.exit(usage)

if os.path.isfile(sys.argv[1]):
    path = sys.argv[1]
    f = open(path,'r')

    for line in f:
        countLines += 1
        words = line.split(' ')
        countWords += len(words)

    print "{} contains {} lines with {} words.".format(path,countLines,countWords)

else:
    sys.exit("There is no valid file under the input path")
