package main

// you can also use imports, for example:
import "fmt"

// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(S string) string {
	chars := make([]rune, 0)

	for _, c := range S {
		var space int = -1
		submit := true

		// put or drop from space
		for i, ava := range chars {
			if ava == c {
				chars[i] = 0
				submit = false
				break
			} else if ava == 0 && space < 0 {
				space = i
			}
		}

		// if gets submitted
		if submit {
			if space >= 0 {
				chars[space] = c
			} else {
				chars = append(chars, c)
			}
		}

		// fmt.Println(c, chars, submit, space)
	}

	ret := ""
	// arrange letter
	for _, c := range chars {
		ret += string(c)
	}

	return ret
}

func main() {
	fmt.Println(Solution("ACCAABBC"))
	fmt.Println(Solution("ABCBBCBA"))
	fmt.Println(Solution("ABSHCAHSCAHSHSC"))
	fmt.Println(Solution("ACCAABBC"))
	fmt.Println(Solution("ACCAABBC"))
	fmt.Println(Solution("ACCAABBC"))
}
