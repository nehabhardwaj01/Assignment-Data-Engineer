object question6 extends App {
  def calcSumOfSquares(n: List[Int]): Int = {
    var sum = 0
    for (num <- n) {
//      square = num * num // val is missing
      val square = num * num
      sum += square
    }
    sum
  }

  calcSumOfSquares([2,3,4])
}