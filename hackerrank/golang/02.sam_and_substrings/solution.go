package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strings"
)

// Complete the substrings function below.
func substrings_TLE(n string) int32 {

	var l int64
	var s int64
	var t int64
	var p int64
	var i int64
	var j int64

	l = int64(len(n))
	s = 0
	p = 1
	t = int64(math.Pow(10, 9) + 7)
	for i = 0; i < l; i++ {
		for j = l - (i + 1); j >= 0; j-- {
			s = (s + ((int64(n[j]) - 48) * (j + 1) * p)) % t
		}
		p = (p * 10) % t
	}

	return int32(s)
}

func substrings_LIN(n string) int32 {

	var l int64
	var s int64
	var t int64
	var p int64
	var i int64
	var j int64

	l = int64(len(n))
	s = 0
	p = 1
	t = int64(math.Pow(10, 9) + 7)
	for i = l; i > 0; i-- {
		j = ((int64(n[i-1]) - 48) * i * p)
		s = (s + j) % t
		p = ((p * 10) + 1) % t
	}

	return int32(s)
}

func substrings(n string) int32 {

	var l int64
	var s int64
	var t int64
	var p int64
	var i int64

	l = int64(len(n))
	p = int64(n[0]) - 48
	s = p
	t = int64(math.Pow(10, 9) + 7)
	for i = 1; i < l; i++ {
		p = ((p * 10) + ((i + 1) * (int64(n[i] - 48)))) % t
		s = (s + p) % t
	}

	return int32(s)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout := os.Stdout

	if os.Getenv("OUTPUT_PATH") != "" {
		stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
		checkError(err)
		defer stdout.Close()
	}

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	n := readLine(reader)

	result := substrings(n)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
