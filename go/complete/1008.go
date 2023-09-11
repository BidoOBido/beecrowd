package main

import "fmt"

func main() {
	var number, hours int
	var valuePerHour float32

	fmt.Scan(&number, &hours)
	fmt.Scan(&valuePerHour)

	salary := float32(hours) * valuePerHour

	fmt.Printf("NUMBER = %d\nSALARY = U$ %.2f\n", number, salary)
}