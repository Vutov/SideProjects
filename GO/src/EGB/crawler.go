package egb

import (
	"encoding/json"
	"fmt"
)

// https://egb.com/bets?st=1496739600&ut=1496880000&f=
// TODO Get live matches - they have an other EndPoint
func GetData() []Match {
	data := Get(LootBetBaseApi + "sportmatch/Get?sportID=2357")
	var matches []Match
	err := json.Unmarshal([]byte(data), &matches)
	if err != nil {
		// TODO LOG
		fmt.Printf("\n%v", err)
	}

	return matches
}
