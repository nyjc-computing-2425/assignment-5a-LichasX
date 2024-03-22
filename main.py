def to_hms(seconds):
  """
  Converts seconds to hours, minutes, and seconds, and returns it as a list.

  Parameters
  ---------
  seconds: int
      the seconds to be calculated

  Returns
  ---------
  list
      a list of integers representing hours, minutes, seconds

  Example:
  >>> to_hms(10)
  [0, 0, 10]
  >>> to_hms(61)
  [0, 1, 1]
  >>> to_hms(7199)
  [1, 59, 59]
  """
  if type(seconds) != int:
    print("Unsupported input type.")
  else:
    return [seconds // 3600 ,(seconds // 60) % 60, seconds % 60]
