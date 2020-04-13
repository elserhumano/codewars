def to_2digits(value):
  if value < 10:
    return '0'+str(value)
  else:
    return str(value)

def make_readable(seconds):
  # Do something
  hours = int(seconds/3600)
  minutes = int((seconds - hours*3600) / 60)
  seconds = int(seconds - (hours*3600 + minutes*60))

  readable = to_2digits(hours)+':'+to_2digits(minutes)+':'+to_2digits(seconds)
  return readable


def make_readable2(s):
  return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


#print(make_readable(86399))
print(make_readable2(1715))
