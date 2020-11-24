package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the dayOfProgrammer function below.
func dayOfProgrammer(year int32) string {

	var day int

	if year > 1918 {
		if day = 13; (!((year % 100) == 0) && ((year % 4) == 0)) || (year%400) == 0 {
			day = 12
		}
	} else if year < 1918 {
		if day = 13; (year % 4) == 0 {
			day = 12
		}
	} else {
		day = 26
	}

	return fmt.Sprintf("%02d.09.%04d", day, year)
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

	yearTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	year := int32(yearTemp)

	result := dayOfProgrammer(year)

	fmt.Fprintf(writer, "%s\n", result)

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
