package q733

type qCoords struct {
	r, c int
}

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	toChange := image[sr][sc]
	if toChange == color {
		return image
	}
	q := []qCoords{{sr, sc}}
	visited := make(map[qCoords]bool)
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if visited[cur] {
			continue
		}
		image[cur.r][cur.c] = color
		visited[cur] = true
		directions := []qCoords{
			{1, 0},
			{-1, 0},
			{0, 1},
			{0, -1},
		}
		for _, direction := range directions {
			rd, cd := direction.r, direction.c
			nr, nc := cur.r+rd, cur.c+cd
			if 0 <= nr && nr < len(image) && 0 <= nc && nc < len(image[0]) && image[nr][nc] == toChange && !visited[qCoords{nr, nc}] {
				q = append(q, qCoords{nr, nc})
			}
		}
	}
	return image
}

