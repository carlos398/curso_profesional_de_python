def main():
  a = 1

  def nested():
    print(a)

  nested() # 1

main()


"""
    Los closures son cuando recordamos una variable
    que fue eliminada con anterioridad en una funcion anidada

"""
#closures

def main():
  a = 1

  def nested():
    print(a)

  return nested

my_func = main()
my_func() # 1