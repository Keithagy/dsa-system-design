pub struct Solution {}
impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        match str1.to_owned() + &str2 != str2.to_owned() + &str1 {
            true => String::new(),
            false => {
                let gcd_len = Self::gcd(str1.len(), str2.len());
                str1[..gcd_len].to_string()
            }
        }
    }
    pub fn gcd(mut a: usize, mut b: usize) -> usize {
        while b != 0 {
            let t = b;
            b = a % b;
            a = t;
        }
        a
    }
}
