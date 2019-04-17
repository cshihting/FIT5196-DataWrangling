
# An example of removing some % of data:
from nltk.probability import *

test_string = ["cat", "cat", "cat", "dog", "dog", "cat", "rabbit", "cat", "cat", "dog"]

test_set = set(test_string)

fd_x = FreqDist(test_string)

print(fd_x.freq('rabbit'))

less_set = set([w for w in test_set if fd_x.freq(w) < 0.30])
print(less_set)

reduced = [w for w in test_string if w not in less_set]
print(reduced)

fd_2 = FreqDist(reduced)
fd_2.plot(100, cumulative=True)


# An example of applying Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
twi_tokenizer = TweetTokenizer()
test_string = "The President of Taiwan CALLED ME today to wish me congratulations on winning the Presidency. Thank you!"
twi_tokens = twi_tokenizer.tokenize(test_string)
print(twi_tokens)
print(len(twi_tokens))