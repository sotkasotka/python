import bisect

def hello():
 print('Hello, world!')
def fib(n):
 a = b = 1
 for i in range(n - 2):
    a, b = b, a + b
 return b

def filter_list(list_a, k):
  """
  Переписывает из списка А в список В только те элементы, значения которых не равны заданному значению К.

  Args:
    list_a (list): Исходный список.
    k (int): Заданное значение.

  Returns:
    list: Список элементов, значения которых не равны заданному значению.
  """

  list_b = []
  for element in list_a:
    if element != k:
      list_b.append(element)

  return list_b


def insert_in_ordered_list(list_a, value_k):
  """Вставляет значение в упорядоченный список.

  Args:
    list_a: Упорядоченный список чисел.
    value_k: Значение для вставки.

  Returns:
    Упорядоченный список с вставленным значением.
  """

  index = bisect.bisect_left(list_a, value_k)

  list_a.insert(index, value_k)

  return list_a

def fill_list(list_a, num_elements, value):
    """
    Заполняет заданное число элементов списка заданным значением.

    Args:
        list_a (list): Список, который нужно заполнить.
        num_elements (int): Количество элементов, которые нужно заполнить.
        value (int): Значение, которым нужно заполнить элементы.

    Returns:
        list: Заполненный список.
    """

    if not list_a:
        raise ValueError("Список не может быть пустым.")

    if num_elements > len(list_a):
        raise ValueError("Количество элементов для заполнения не может превышать длину списка.")

    for i in range(num_elements):
        list_a[i] = value

    return list_a