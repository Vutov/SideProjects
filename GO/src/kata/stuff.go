package kata

func IsTriangle(a, b, c int) bool {
	if a > 0 && b > 0 && c > 0 && a+b > c && b+c > a && a+c > b {
		return true
	}

	return false
}
