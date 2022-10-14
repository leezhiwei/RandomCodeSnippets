use std::io;
use try_catch::catch;
fn menu(c: i32) {
    if c == 1 {
        println!("Welcome to Calculator");
        println!("1. Addition");
        println!("2. Subtraction");
        println!("3. Division");
        println!("4. Multiplication");
        println!("Please enter your option: ")
    } else if c == 2 {
        println!("Please enter the first number: ");
    } else if c == 3 {
        println!("Please enter the second number: ");
    } else {
        println!("Check function input");
    }
}
fn main() {
    let mut input = "".to_string();
    let stdin = io::stdin();
    menu(1);
    stdin.read_line(&mut input).ok();
    catch!{
        try {
            let c: i32 = input.parse().unwrap();
        }
    }
    if c == 1 {
        menu(2);
        stdin.read_line(&mut input).ok();
        let c2: i32 = input.parse().unwrap();
        menu(3);
        stdin.read_line(&mut input).ok();
        let c3: i32 = input.parse().unwrap();
        let result = c2 + c3;
        println!("The result is {}", result);
    } else if c == 2 {
        menu(2);
        stdin.read_line(&mut input).ok();
        let c2: i32 = input.parse().unwrap();
        menu(3);
        stdin.read_line(&mut input).ok();
        let c3: i32 = input.parse().unwrap();
        let result = c2 - c3;
        println!("The result is {}", result);
    } else if c == 3 {
        menu(2);
        stdin.read_line(&mut input).ok();
        let c2: i32 = input.parse().unwrap();
        menu(3);
        stdin.read_line(&mut input).ok();
        let c3: i32 = input.parse().unwrap();
        let result = c2 / c3;
        println!("The result is {}", result);
    } else if c == 4 {
        menu(2);
        stdin.read_line(&mut input).ok();
        let c2: i32 = input.parse().unwrap();
        menu(3);
        stdin.read_line(&mut input).ok();
        let c3: i32 = input.parse().unwrap();
        let result = c2 * c3;
        println!("The result is {}", result);
    } else {
        println!("Invalid input.")
    }
}

