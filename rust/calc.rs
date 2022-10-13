fn menu(c: i32){
    if c == 1 {
        println!("Welcome to Calculator");
        println!("1. Addition");
        println!("2. Subtraction");
        println!("3. Division");
        println!("4. Multiplication");
    }
    else if c == 2 {
        println!("Please enter the first number: ");
    }
    else if c == 3 {
        println!("Please enter the second number: ");
    }
    else{
        println!("Check function input");
    }
}
fn main() {
    menu(1);
}
