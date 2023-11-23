use std::collections::HashSet;

pub struct Solution {}
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let vowels: HashSet<char> = vec!['a', 'e', 'i', 'o', 'u'].into_iter().collect();
        let mut chars: Vec<char> = s.chars().collect();
        let mut beginning = 0;
        let mut end = chars.len() - 1;

        while beginning < end {
            while beginning < end && !vowels.contains(&chars[beginning].to_ascii_lowercase()) {
                beginning += 1;
            }
            while beginning < end && !vowels.contains(&chars[end].to_ascii_lowercase()) {
                end -= 1;
            }
            if beginning >= end {
                break;
            }
            chars.swap(beginning, end);
            beginning += 1;
            end -= 1;
        }
        chars.into_iter().collect()
    }
}
