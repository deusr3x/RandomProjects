package main

import (
	"fmt"
	"math"
)

func isprime(num int) bool {
	if num == 2 {
		return true
	}
	if num%2 == 0 {
		return false
	}
	for i := 3; i <= (int(math.Sqrt(float64(num)))); i += 2 {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	// num := 0
	count := 2
	ans := 0
	for count < 2000000 {
		if isprime(count) {
			ans += count
		}
		count++
	}
	fmt.Println(ans)
}
