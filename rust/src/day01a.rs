use std::fs;

pub fn get_result() -> i32 {
    let input = fs::read_to_string("../input/input_1.txt")
        .expect("Failed to read input");
   calculate_sum(&input)
}

fn calculate_sum(input: &str) -> i32 {
    input.lines()
        .filter_map(|line| get_number(line))
        .sum()
}

fn get_number(line: &str) -> Option<i32> {
    let first_digit = line.chars().find(|c| c.is_digit(10)).unwrap();
    let last_digit = line.chars().rev().find(|c| c.is_digit(10)).unwrap(); 
    format!("{}{}",first_digit, last_digit).parse::<i32>().ok()
}
