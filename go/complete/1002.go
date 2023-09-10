package main

import (
	"fmt"
	"math"
)

const (
	PI = 3.14159
)

func main() {
	var r float64
	_, _ = fmt.Scan(&r)

	fmt.Printf("A=%.4f\n", PI * math.Pow(r, 2))
}