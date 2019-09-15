package main

import "fmt"

func IsEven(num int) bool {
	if (num%2) == 0 {
		return true
	} else {
		return false
	}
}

func calcFib(a int, b int) int {
	return a + b
}

func main() {
	evensum := 0
	sum := 1
	pastsum := 1
	futuresum := 0
	for futuresum < 4000000 {
		futuresum = calcFib(sum, pastsum)
		pastsum = sum
		sum = futuresum
		if IsEven(futuresum) {
			evensum += futuresum
		}
	}
	fmt.Println(sum)
	fmt.Println(futuresum)
	fmt.Println(evensum)
}