

class Rounder():
  def round(self, input):
    threshold = (0, 0.5)
    #  find the appropriate threshold
    for t in self.rounding_thresholds:
      threshold = t
      if t[0] > input:
        break
    
    # round
    if (round((input % threshold[1]) / threshold[1], 5) <= self.round_down_threshold):  # added a round operator to accomodate floating point error
      return input - (input % threshold[1])
    return input + (threshold[1] - (input % threshold[1]))

  def __init__(self, _rounding_thresholds=[(0.0, 0.5)], _round_down_threshold = 0.3) -> None:
    self.rounding_thresholds = _rounding_thresholds
    self.round_down_threshold = _round_down_threshold
    pass


if __name__ == '__main__':
  # tests
  r = Rounder(_rounding_thresholds=[(5, .5), (20, 2), (100, 13)], _round_down_threshold=0.2)
  assert(r.round(1.3) == 1.5)
  assert(r.round(1.1) == 1)
  assert(r.round(.9) == 1)

  assert(r.round(10.3) == 10)
  assert(r.round(10.51) == 12)
  assert(r.round(19.9) == 20)

  assert(r.round(20.1) == 26)
  assert(r.round(35.2) == 39)
  assert(r.round(40.25) == 39)
  print('All tests passed')