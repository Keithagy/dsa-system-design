use std::collections::HashSet;

pub struct Solution {}
impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let n_usize: usize = n.try_into().expect("n to never be negative");
        if n == 0 {
            return true;
        }
        if flowerbed.is_empty() {
            return false;
        }
        if flowerbed.len() == 1 {
            return n == 1 && flowerbed[0] == 0;
        }

        let mut planted_positions: HashSet<usize> = HashSet::with_capacity(n_usize);
        for i in 0..flowerbed.len() {
            if planted_positions.len() >= n_usize {
                return true;
            }

            if flowerbed[i] == 1 {
                continue;
            }

            match i {
                0 => {
                    if !Self::has_flower_planted_at(&flowerbed, &planted_positions, i + 1) {
                        planted_positions.insert(i);
                    }
                }
                _ if i == flowerbed.len() - 1 => {
                    if !Self::has_flower_planted_at(&flowerbed, &planted_positions, i - 1) {
                        planted_positions.insert(i);
                    }
                }
                _ => {
                    if !Self::has_flower_planted_at(&flowerbed, &planted_positions, i - 1)
                        && !Self::has_flower_planted_at(&flowerbed, &planted_positions, i + 1)
                    {
                        planted_positions.insert(i);
                    }
                }
            }
        }
        planted_positions.len() >= n_usize
    }
    fn has_flower_planted_at(
        flowerbed: &[i32],
        planted_positions: &HashSet<usize>,
        idx: usize,
    ) -> bool {
        flowerbed[idx] == 1 || planted_positions.contains(&idx)
    }
}
