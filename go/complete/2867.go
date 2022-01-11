package main

import "fmt"
import "math"

func main() {
  var casos, n, m int
  var saida float64

  fmt.Scanln(&casos)

  for i := 0; i < casos; i++{
    fmt.Scan(&n)
    fmt.Scan(&m)

    saida = math.Floor((float64(m) * math.Log10(float64(n)) + 1))

    fmt.Println(saida)
  }
}