'''
Some languages like Chinese, Japanese, and Thai do not have spaces between words. However, most natural languages processing tasks like part-of-speech tagging require texts that have segmented words. A simple and reasonably effective algorithm to segment a sentence into its component words is called "MaxMatch".

MaxMatch
MaxMatch starts at the first character of a sentence and tries to find the longest valid word starting from that character. If no word is found, the first character is deemed the longest "word", regardless of its validity. In order to find the rest of the words, MaxMatch is then recursively invoked on all of the remaining characters until no characters remain. A list of all of the words that were found is returned.

So for the string "happyday", "happy" is found because "happyday" is not a valid word, nor is "happyda", nor "happyd". Then, MaxMatch is called on "day", and "day" is found. The output is the list ["happy", "day"] in that order.

The Challenge
Write max_match, which takes an alphanumeric, spaceless, lowercased String as input and returns a List of Strings of all the words found, in the order they were found. All valid words are in the Set VALID_WORDS, which only contains around 500 English words.

Note: This algorithm is simple and operates better on Chinese text, so accept the fact that some words will be segmented wrongly.
'''

VALID_WORDS = {'may', 'toasted', 'than', 'compensates', 'consumption', 'greatly', 'cool', 'math', 'bold', 'lazy', 'things', 'authority', 'visited', 'your', 'handkerchief', 'discovered', 'rock', 'place', 'laptop', 'told', 'ago', 'about', 'am', 'night', 'ass', 'plan', 'only', 'country', 'writing', 'life', 'floor', 'no', 'older', 'from', 'walk', 'ran', 'how', 'human', 'tooth', 'susan', 'slammed', 'work', 'counting', 'broken', 'seats', 'appreciated', 'currently', 'went', 'impassable', 'attendance', 'want', 'body', 'get', 'persons', 'piece', 'high', 'roof', 'loud', 'realise', 'unique', 'says', 'id', 'sixtyfour', 'would', 'river', 'story', 'sunburnt', 'shake', 'above', 'buttered', 'his', 'mysterious', 'syrup', 'windows', 'real', 'young', 'school', 'music', 'twinkling', 'reason', 'hand', 'him', 'join', 'free', 'comes', 'baggage', 'and', 'tuna', 'off', 'wrote', 'pig', 'room', 'little', 'same', 'midsent', 'tomorrow', 'returned', 'often', 'vacant', 'enough', 'rain', 'try', 'saying', 'kite', 'hear', 'after', 'shop', 'small', 'oh', 'thoughts', 'mary', 'test', 'wait', 'can', 'middle', 'yesterday', 'places', 'cream', 'together', 'house', 'not', 'weeks', 'records', 'many', 'out', 'amount', 'doll', 'what', 'donation', 'stars', 'stranger', 'velocity', 'year', 'once', 'made', 'should', 'roads', 'asking', 'drive', 'start', 'rather', 'pretty', 'clocks', 'stay', 'wont', 'however', 'alone', 'hurry', 'mind', 'time', 'revels', 'but', 'tomato', 'gods', 'sick', 'christmas', 'or', 'do', 'bad', 'have', 'shore', 'eat', 'as', 'alive', 'conditions', 'striped', 'freezer', 'fish', 'diary', 'until', 'again', 'memory', 'make', 'a', '1234', 'caramel', 'turned', 'with', 'remember', 'sundays', 'camel', 'donkey', 'need', 'passed', 'pie', 'officiates', 'sky', 'crashing', 'spotted', 'information', 'day', 'money', 'door', 'take', 'under', 'does', 'africa', 'piano', 'ended', 'saw', 'something', 'old', 'said', 'within', 'metaphysics', 'fine', 'milk', 'eating', 'tries', 'legless', 'lovely', 'red', 'research', 'green', 'neatly', 'laugh', 'didnt', 'read', 'table', 'happy', 'someone', '4', 'sometimes', 'detailed', 'plays', '1', 'taste', 'folded', 'flew', 'them', 'right', 'bird', 'got', 'store', 'book', 'it', 'maple', 'least', 'babies', 'coherent', 'leave', 'bunny', 'blue', 'other', 'calories', 'today', 'lake', 'glass', 'by', 'spend', 'love', 'where', 'see', 'great', 'find', 'busy', 'different', 'noisy', 'paper', 'did', 'paints', 'clock', 'mum', 'he', 'share', 'arrived', 'lease', 'any', 'everyone', 'of', 'stop', 'onesie', 'gotten', 'anyway', 'asked', 'true', 'dark', 'home', 'youre', 'sight', 'very', 'fence', 'decorated', 'town', 'all', 'ill', 'away', 'vividly', 'the', 'early', 'harder', 'nickname', 'why', 'exciting', 'ruin', 'hes', 'good', 'lizard', 'has', 'fox', 'italy', 'english', 'works', 'hump', 'hasnt', 'when', 'sounds', 'asia', 'jumps', 'was', 'yourself', 'this', 'abstraction', 'two', 'my', 'sentence', 'our', 'one', 'for', 'ever', 'perhaps', 'proud', 'they', '1111', 'pastels', 'learning', 'chocolate', 'me', 'outside', 'people', 'longer', 'combined', 'you', 'come', 'eaters', 'speaks', 'cows', 'colors', 'wednesday', 'either', 'friday', 'completely', 'first', 'cookies', 'white', 'approaches', 'think', 'apple', 'dessert', 'that', 'purple', 'is', 'waves', 'advised', 'used', 'isnt', 'werent', 'malls', 'loss', 'will', 'tom', 'way', 'now', 'worm', 'letter', 'recently', 'voice', 'yet', 'know', 'popcorn', 'best', 'cheat', 'teeth', 'everything', 'she', 'better', 'clean', 'her', 'june', 'coming', 'never', 'each', 'we', 'japanese', 'anyone', 'really', 'open', 'class', 'there', 'ends', 'check', 'to', 'always', 'couldnt', 'so', 'else', 'front', 'luck', 'quick', 'help', 'clear', 'jobs', 'thought', 'lot', 'glittering', 'rent', 'subsequently', 'be', 'meet', 'at', 'three', 'thinking', 'i', 'goodbye', 'bread', 'brown', 'if', 'back', 'throughout', 'poker', 'still', 'recommend', 'likes', 'combining', 'going', 'wow', 'had', 'promotion', 'meal', 'up', 'environment', 'fairy', 'checked', 'hour', 'favorite', 'dog', 'sure', 'shooter', 'later', 'cats', 'nancy', 'list', 'blog', 'go', 'adventure', 'thing', 'having', 'frame', 'last', 'like', 'step', 'let', 'dentist', 'party', 'its', 'hands', 'initially', 'person', 'here', 'on', 'fact', 'us', 'dont', 'been', 'years', 'too', 'random', 'easter', 'were', 'song', 'sentences', 'are', 'movie', 'playing', 'yeah', 'sandwiches', 'otherwise', 'ice', 'gem', 'joe', 'car', 'lets', 'next', 'buy', 'suit', 'wasnt', 'long', 'stole', 'borrowed', 'short', 'sauce', 'quite', 'cheese', 'shut', 'an', 'sugar', 'in', 'more', 'nor', 'pets', 'just', 'over', 'please', 'getting'}
def max_match(sentence):  
  curren_word = ''
  check_word = ''
  index = 0
  temp_index=0
  temp_word=''
  result = []
  c = ''
  while index <len(sentence):    
    c = sentence[index]
    filtered = [x for x in VALID_WORDS if x.startswith(c)]
    if (len(filtered)==0):
      result.append(c)      
    else:
      temp_index = index
      flag = True
      curren_word = c
      check_word= ''
      while (flag and temp_index<len(sentence)):        
        check_word = check_word + sentence[temp_index] 
        filtered = [x for x in VALID_WORDS if x.startswith(check_word)]
        if len(filtered)!=0:      
          if (check_word in VALID_WORDS):
            curren_word = check_word
            index = temp_index
        else:          
          flag = False
        temp_index = temp_index+1
      result.append(curren_word)    
    index = index+1
  return result

def main():
  print('win' in VALID_WORDS)
  print(max_match('ewingsa'))
 
main()