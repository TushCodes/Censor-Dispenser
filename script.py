# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import copy 

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(text, censors):
  censors.sort(reverse=True)
  for terms in censors:
    if terms in text.lower():
      text = text.replace(terms, ("*"*len(terms)))
      text = text.replace(terms.capitalize(), ("*"*len(terms)))
  return text

def censor_with_negative(text, neg_censors, censors):
  neg_censors.sort(reverse=True)
  text = censor(text, censors)
  for terms in neg_censors:
    if terms in text.lower():
      text = text.replace(terms, ("*"*len(terms)))
      text = text.replace(terms.capitalize(), ("*"*len(terms)))
  return text

def strong_censor(text, neg_censors, censors):
  text = censor_with_negative(text, neg_censors, censors)
  text_words = text.split()
  temp_text_words = copy.copy(text_words)

  for i in range(1, len(text_words)-1):
    if "*" in text_words[i]:
      temp_text_words[i-1] = "*"*len(text_words[i-1])
      temp_text_words[i] = "*"*len(text_words[i]) #repairing the bug
      temp_text_words[i+1] = "*"*len(text_words[i+1])
  text_words = temp_text_words

  #special cases
  if "*" in text_words[0]:
    text_words[1] = "*"*len(text_words[1])
  if "*" in text_words[-1]:
    text_words[-2] = "*"*len(text_words[2])

  return " ".join(text_words)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

print(strong_censor(email_four, negative_words, proprietary_terms))
print(email_four)