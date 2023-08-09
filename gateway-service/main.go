package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	// GET API 
	router.GET("/", getDefault)
	router.GET("/events", getEvents)

	httpPort := os.Getenv("PORT")
	if httpPort == "" {
		httpPort = "8080"
	}

	router.Run("0.0.0.0:" + httpPort)
}

func getDefault(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, "Hello from Gateway!")
}

func getEvents(c *gin.Context) {
	resp, err := http.Get("http://event:8050/events")
	if err != nil {
		fmt.Println(err)
	}
	defer resp.Body.Close()

	var decodeData interface{}
	err = json.NewDecoder(resp.Body).Decode(&decodeData)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(decodeData)
	c.IndentedJSON(http.StatusOK, decodeData)
}

