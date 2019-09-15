package main

import (
	"fmt"
	"math"
)

func primeFactors(num int) {
	for (num % 2) == 0 {
		fmt.Println(2)
		num = num / 2
	}

	for i:=3; i < (int(math.Sqrt(float64(num)) + 1)); i+=2 {
		for (num % i) == 0 {
			fmt.Println(i)
			num = num / i
		}
	}
	if num > 2 {
		fmt.Println(num)
	}
}

func main() {
	primeFactors(600851475143)
}