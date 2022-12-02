use std::env;
use std::fs;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let file_path = "sample_data_1.txt";
    println!("In file {}", file_path);

    if let Ok(calories = read_lines("sample_data_1.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut elves = Vec::new();
        let mut food = Vec::new();


        for calorie in calories {
            if let Ok(ip) = calorie {
                food.push(ip);
                println!("{}", ip);
            } else {
                elves.push(food);
            }
        }
        println!("{}", std::str::from_utf8(elves));

    }

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    // println!("With text:\n{contents}");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
