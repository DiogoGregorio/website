# Function to return the nth word according to the rules described by the user
from typing import Optional

def get_nth_word(phrase: Optional[str], number: Optional[int]) -> str:
    """
    Returns the word associated with `number` from `phrase`:
      - If number is None -> "NULL ERROR"
      - If phrase is None or contains no words -> "empty phrase"
      - If number <= 0 -> "value below the allowed"
      - If number > number of words -> "value above the allowed"
      - Otherwise return the nth word (1-based index)
    
    Words are defined by splitting on any whitespace.
    """
    # Check for NULL number first
    if number is None:
        return "NULL ERROR"
    
    # Normalize phrase input
    if phrase is None:
        # treat None phrase as empty
        return "empty phrase"
    
    # Split on whitespace to get words (this will ignore extra spaces)
    words = phrase.split()
    
    if len(words) == 0:
        return "empty phrase"
    
    # If number is 0 or negative -> below allowed
    if number <= 0:
        return "value below the allowed"
    
    # If number is larger than available words -> above allowed
    if number > len(words):
        return "value above the allowed"
    
    # Otherwise return the (number-1)th element
    return words[number - 1]

phrase = input("phrase: ")
number = int(input("number: "))

output = get_nth_word(phrase, number)
print("The word is -> ", output)

