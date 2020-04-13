# Task
#  	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
# Rules
    # 1.  The input string will always be lower case but maybe empty.
    # 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
#
# Example
#         wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(people):
    # Code here
    if len(people) == 0:
        return []
    else:
      result = []
      for i in range(0, len(people)):
        temp = ''
        for j in range(0, len(people)):
            if i == j:
              temp += people[j].upper()
            else:
              temp += people[j]
        if people[i] != ' ':
          result.append(temp)
      return result



print(wave("hola que tal"))
