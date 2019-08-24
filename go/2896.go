package main

import "fmt"

func main() {
  var casos, garrafas, bonus, ganho, sobra int

  fmt.Scanln(&casos)

  for i := 0; i < casos; i++{
    fmt.Scan(&garrafas)
    fmt.Scan(&bonus)

    ganho = garrafas / bonus
    sobra = garrafas % bonus

    fmt.Println(ganho + sobra)
  }
}