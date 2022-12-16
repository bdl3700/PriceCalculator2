import math

class ItemType():
  def __init__(self, _name : str, _a_value: float, _e_value: float) -> None:
    self.name = _name
    self.a_value = _a_value
    self.e_value = _e_value
    pass

  def calculate_margin(self, cost: float) -> float:
    if cost > 0:
      return self.a_value / (1+ math.pow(self.e_value, (0-cost)))
    return 0.0
  
  def calculate_retail(self, cost: float) -> float:
    if (cost > 0):
      return cost / self.calculate_margin(cost)
    return 0.0

if __name__ == '__main__':
  # tests
  it = ItemType('type1', .73, 1.1)

  assert(it.name == 'type1')

  assert(round(it.calculate_margin(1), 8) == .38238095)
  assert(round(it.calculate_margin(2), 8) == .39968326)
  assert(round(it.calculate_margin(3), 8) == .41682969)
  assert(round(it.calculate_margin(4), 8) == .43374579)
  assert(round(it.calculate_margin(5), 8) == .45036116)

  assert(round(it.calculate_margin(10), 8) == .52686914)
  assert(round(it.calculate_margin(20), 8) == .63553219)
  assert(round(it.calculate_margin(30), 8) == .69043232)
  assert(round(it.calculate_margin(40), 8) == .71421937)
  assert(round(it.calculate_margin(50), 8) == .72383398)

  assert(round(it.calculate_margin(100), 8) == .72994703)
  assert(round(it.calculate_margin(200), 8) == .73)
  assert(round(it.calculate_margin(300), 8) == .73)
  assert(round(it.calculate_margin(400), 8) == .73)
  assert(round(it.calculate_margin(500), 8) == .73)
  print('margin tests passed')

  assert(round(it.calculate_retail(1), 6) == 2.615193)
  assert(round(it.calculate_retail(2), 6) == 5.003962)
  assert(round(it.calculate_retail(3), 6) == 7.197184)
  assert(round(it.calculate_retail(4), 6) == 9.221992)
  assert(round(it.calculate_retail(5), 6) == 11.102201)

  assert(round(it.calculate_retail(10), 6) == 18.980045)
  assert(round(it.calculate_retail(20), 6) == 31.469688)
  assert(round(it.calculate_retail(30), 6) == 43.451036)
  assert(round(it.calculate_retail(40), 6) == 56.005202)
  assert(round(it.calculate_retail(50), 6) == 69.076613)

  assert(round(it.calculate_retail(100), 5) == 136.99624)
  assert(round(it.calculate_retail(200), 4) == 273.9726)
  assert(round(it.calculate_retail(300), 4) == 410.9589)
  assert(round(it.calculate_retail(400), 5) == 547.94521)
  assert(round(it.calculate_retail(500), 5) == 684.93151)

  print('All tests passed')
