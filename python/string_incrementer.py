def fill_with0(str_number, size):
    cero_numbers = ''
    for i in range(1, size-len(str_number)+1):
        cero_numbers += '0'
    return cero_numbers + str_number

def increment_string(strng):
    only_numbers = ''
    only_letters = ''
    for i in range(0, len(strng)):
      if strng[i].isdigit():
        only_numbers += strng[i]
      else:
        only_letters += strng[i]
    if only_numbers == '':
      return strng + '1'
    else:
      size = len(only_numbers)
      new_numbers = fill_with0(str(int(only_numbers) + 1), size)
      return only_letters + new_numbers


print (increment_string('hola099'))
