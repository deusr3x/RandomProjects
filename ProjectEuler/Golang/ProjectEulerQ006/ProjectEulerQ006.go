package main

import "fmt"

func main() {
	// squaresum := 0
	// sum := 0
	limit := 100
	sum := limit*(limit + 1) / 2
	sum_sq := (2*limit + 1)*(limit + 1)*limit / 6
	// for i:=1; i<101; i++ {
	// 	squaresum += i*i
	// 	sum += i
	// }
	fmt.Println(sum*sum - sum_sq)
}