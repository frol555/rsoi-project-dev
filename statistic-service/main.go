package main

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)


func main() {
	router := gin.Default()
	router.GET("/", getDefault)

	httpPort := os.Getenv("PORT")
	if httpPort == "" {
		httpPort = "8050"
	}

	router.Run("0.0.0.0:" + httpPort)
}

func getDefault(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, "statistic-service")
}

