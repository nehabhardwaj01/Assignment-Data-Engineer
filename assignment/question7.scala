def sum_of_n_natural_numbers(n: Int): Int = {
  Range.inclusive(1, n).foldLeft(0)(_ + _)
  // Alternatively, the sum method can be used
  // Range.inclusive(1, n).sum
}
