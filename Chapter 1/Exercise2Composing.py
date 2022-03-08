def compose(f: "A to B", g: "B to C") -> "A to C":
  return lambda x: g(f(x))