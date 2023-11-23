pub struct Solution {}
impl Solution {
    pub fn reverse_words_idiomatic(s: &str) -> String {
        s.split_whitespace().rev().collect::<Vec<&str>>().join(" ")
    }

    pub fn reverse_words(s: String) -> String {
        let mut chars: Vec<char> = s.trim().chars().collect();
        chars.reverse();

        let mut i = 0;
        while i < chars.len() {
            // find word start
            while i < chars.len() && chars[i] == ' ' {
                i += 1;
            }

            let mut j = i;
            while j < chars.len() && chars[j] != ' ' {
                j += 1;
            }
            chars[i..j].reverse();
            i = j + 1;
        }

        let (mut read_idx, mut write_idx) = (0, 0);
        while read_idx < chars.len() {
            if chars[read_idx] != ' ' {
                chars[write_idx] = chars[read_idx];
                write_idx += 1;
                read_idx += 1;
            } else {
                while chars[read_idx] == ' ' {
                    read_idx += 1;
                }
                if read_idx < chars.len() {
                    chars[write_idx] = ' ';
                    write_idx += 1;
                }
            }
        }
        chars[..write_idx].iter().collect()
    }
}
