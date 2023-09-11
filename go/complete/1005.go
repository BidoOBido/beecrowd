package main

import "fmt"

func main() {
	var A, B float64

	fmt.Scan(&A, &B)

	fmt.Printf("MEDIA = %.4f\n", (A+B)/2)
}