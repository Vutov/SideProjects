package egb

import (
	"fmt"

	"github.com/go-resty/resty"
)

func Get(url string) string {
	//TODO Extract to reuse

	response, err := resty.R().Get(url)
	if err != nil {
		// TODO log
		fmt.Printf("\n%v", err)
	}

	if response.StatusCode() != OK {
		// TODO LOG
		fmt.Printf("\nResponse Code Error: %v", response.StatusCode())
	}

	fmt.Printf("\nResponse Time: %v", response.Time())
	fmt.Printf("\nResponse Recevied At: %v", response.ReceivedAt())

	return response.String()
}
