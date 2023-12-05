use std::fs;
use std::collections::HashMap;

pub fn get_result() -> i32 {
    let input = fs::read_to_string("../input/input_1.txt")
        .expect("Failed to read input");
   calculate_sum(&input)
}

fn calculate_sum(input: &str) -> i32 {
    let mut digits = HashMap::new();
    for i in 0..=9 {
        digits.insert(i.to_string(), i);
    }
    let words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for (i, &word) in words.iter().enumerate() {
        digits.insert(word.to_string(), i as i32);
    }

    input.lines()
       .filter_map(|line| get_number(line, &digits))
        .sum()
}

fn get_number(line: &str, digits: &HashMap<String, i32>) -> Option<i32> {
    let mut first_digit = -1;
    let mut last_digit = -1;
    for i in 0..line.len() {
        for (key, &value) in digits.iter() {
            if line[i..].starts_with(key) {
                if first_digit == -1 {
                    first_digit = value;
                }
                last_digit = value;
            }
        }
    }
    Some(first_digit * 10 + last_digit)
}