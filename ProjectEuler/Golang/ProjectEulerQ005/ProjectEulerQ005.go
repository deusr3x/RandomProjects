package main

import "fmt"

func f(num int) {
	for {
		count := 0
		for i := 20; i > 0; i-- {
			if (num % i) != 0 {
				break
			} else {
				count += 1
			}
		}
		if count == 20 {
			// fmt.Println(num)
			fmt.Println("go func: ", num)
			break
		}
		num += 1
	}
}

func main() {
	fmt.Println("Hello")
	num := 2520
	go f(num)
	// fmt.Scanln()

	for {
		count := 0
		for i := 20; i > 0; i-- {
			if (num % i) != 0 {
				break
			} else {
				count += 1
			}
		}
		if count == 20 {
			fmt.Println(num)
			break
		}
		num += 1
	}
	fmt.Println("done")
}
