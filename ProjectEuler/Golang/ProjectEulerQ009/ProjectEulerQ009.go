package main

import (
	"fmt"
	"math"
)

func isSquare(num float64) bool {
	a := math.Sqrt(num)
	return (a - math.Floor(a)) == 0
}

func main() {
	for b := 2; b < 1000; b++ {
		for a := 1; a < b; a++ {
			c2 := a*a + b*b
			if isSquare(float64(c2)) {
				if a+b+int(math.Sqrt(float64(c2))) == 1000 {
					fmt.Println(a * b * int(math.Sqrt(float64(c2))))
					fmt.Println(a)
					fmt.Println(b)
					fmt.Println(math.Sqrt(float64(c2)))
				}
			}
		}
	}
}
