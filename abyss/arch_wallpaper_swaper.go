package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	//"os/exec"
	//"path/filepath"
)

type MyData struct {
	Field1 string
	Field2 string
}

func main() {
	wallpaper_location := "/home/sy/.config/hypr/hyprpaper.conf" 

	data := MyData{
		Field1: "preload = ~/Downloads/wallpaper/",
		Field2: "wallpaper = ,~/Downloads/wallpaper/",
	}

	//getting the user input
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("enter file name: ")
	userInput, _ := reader.ReadString('\n')

	//update the struct
	data.Field1 += userInput[:len(userInput)-1]
	data.Field2 += userInput[:len(userInput)-1]

	// Overwrite file with formatted content
	err := os.WriteFile(wallpaper_location, []byte(data.Field1+"\n"+data.Field2+"\n"), 0644)
	if err != nil {
		log.Fatal(err)
	}
	// how to execute a os comanned
	//cmd := exec.Command()
}
