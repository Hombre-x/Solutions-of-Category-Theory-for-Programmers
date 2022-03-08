def compose(f: "A to B", g: "B to C") -> "A to C":
  return lambda x: g(f(x))


if __name__ == "__main__":

  func1 = lambda x: x + 1
  func2 = lambda x: x * 2
  print(compose(func2, func1)(2))