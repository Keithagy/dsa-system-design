pub struct Solution {}
impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let highest = candies.iter().max();
        match highest {
            Some(highest) => candies
                .iter()
                .map(|count| count + extra_candies >= *highest)
                .collect(),
            None => unreachable!("candies has minimum length 2"),
        }
    }
}
