use std::fs;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let file_path = "sample_data_1.txt";
    println!("In file {}", file_path);

    if let Ok(calories) = read_lines("sample_data_1.txt") {
        // Consumes the iterator, returns an (Optional) String
        let elves: Vec<String> = Vec::new();
        let food: Vec<String> = Vec::new();

        for calorie in calories {
            if let Ok(ip) = calorie {
                food.push(&mut ip);
                // println!("{}", ip);
            } else {
                let newfood = food.to_vec();
                println!("{}", String::from_iter(newfood));
                // elves.push(newfood);
            }
        }
        for item in elves {
            println!("{}", item)
        // let s:String = String::from_iter(elves);
        // println!("{}", s);
        }
    }

    let _contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    // println!("With text:\n{_contents}");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
