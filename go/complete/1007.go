package main

import "fmt"

func main() {
	var A, B, C, D int

	fmt.Scan(&A, &B, &C, &D)

	diferenca := (A * B - C * D)

	fmt.Printf("DIFERENCA = %d\n", diferenca)
}