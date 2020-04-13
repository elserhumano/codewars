def generate_hashtag(s):
    #your code here
    if len(s) == 0:
        return False
    hash_tag = '#'
    for i in s.split():
        hash_tag += i.capitalize()
    if len(hash_tag) > 140:
      return False
    else:
      return hash_tag


print(generate_hashtag('Esto      es   una                 prueba   a                 ver'))
