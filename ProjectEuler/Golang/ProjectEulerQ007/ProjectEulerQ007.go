package main

import (
	"fmt"
	"math"
)

func isprime(num int) bool {
	if num == 2 {
		return true
	}
	if num % 2 == 0 {
		return false
	}
	for i:=3; i <= (int(math.Sqrt(float64(num)))); i+=2 {
		if num % i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var ans []int
	ans = append(ans,2)
	counter := 3
	for len(ans) < 10001 {
		if isprime(counter) {
			ans = append(ans,counter)
		}
		counter+=2
	}
	fmt.Println(ans[10000])
}