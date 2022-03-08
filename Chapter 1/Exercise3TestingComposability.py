def test_identity(f: "A to B", test: "A") -> bool:
  
  # Defining the identity function
  def id(item: "A") -> "A":
    return item

  # Defining the composition function
  def compose(f: "A to B", g: "B to C") -> "A to C":
    return lambda x: g(f(x))

  if compose(f, id)(test) == f(test) and compose(id, f)(test) == f(test): 
    return True

  else:
    return False


if __name__ == "__main__":

  print()
  print(test_identity(lambda x: x + 1, 2))
  print(test_identity(lambda y: f"{y} works!", "It"))