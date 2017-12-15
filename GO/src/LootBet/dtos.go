package lootBet

type Match struct {
	HomeTeam    string     `json:"HomeTeamName"`
	AwayTeam    string     `json:"AwayTeamName"`
	MatchName   string     `json:"Name"`
	DateOfMatch string     `json:"DateOfMatch"`
	Category    Category   `json:"Category"`
	Tournament  Tournament `json:"Tournament"`
	IsLive      bool       `json:"IsLive"`
	MatchOdds   []Odd      `json:"PreviewOdds"`
	IsActive    bool       `json:"IsActive"`
	StreamURL   string     `json:"StreamUrl"`
}

type Category struct {
	Name string `json:"Name"`
}

type Tournament struct {
	Name string `json:"Name"`
}

type Odd struct {
	TeamName string  `json:"Title"`
	Value    float64 `json:"Value"`
	IsLive   bool    `json:"IsLive"`
}
