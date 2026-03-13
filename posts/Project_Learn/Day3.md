---
title: "Day 3"
date: "2026-02-21"
author: "You"
tags: ["rust", "python", "practical_learning", "3","day3"]
description: "A Learning Day with ChatGPT Project_Learn/Day-3."
---

# Project Dump: ./03_day/

## Project Structure

```text
./03_day/
├── 10.rs
├── 11.rs
├── 12.rs
├── 1.rs
├── 2_1.rs
├── 2.rs
├── 3_1.rs
├── 3.rs
├── 4_1.rs
├── 4_2.rs
├── 4_3.rs
├── 4.rs
├── 5_1.rs
├── 5.rs
├── 6_1.rs
├── 6.rs
├── 7.rs
├── 8.rs
├── 9.rs
└── mini_calculator_cli
    ├── Cargo.toml
    ├── .gitignore
    └── src
        └── main.rs

3 directories, 22 files
```

## File Contents

### ./03_day/1.rs

```rust
fn main() {
    // This is an example of a line comment.
    // There are two slashes at the beginning of the line.
    // And nothing written after these will be read by the compiler.

    // println!("Hello, world!");

    // Run it. See? Now try deleting the two slashes, and run it again.

    /*
     * This is another type of comment, a block comment. In general,
     * line comments are the recommended comment style. But block comments
     * are extremely useful for temporarily disabling chunks of code.
     * /* Block comments can be /* nested, */ */ so it takes only a few
     * keystrokes to comment out everything in this main() function.
     * /*/*/* Try it yourself! */*/*/
     */

    /*
    Note: The previous column of `*` was entirely for style. There's
    no actual need for it.
    */

    // Here's another powerful use of block comments: you can uncomment
    // and comment a whole block by simply adding or removing a single
    // '/' character:

    //* <- add another '/' before the 1st one to uncomment the whole block

    println!("Now");
    println!("everything");
    println!("executes!");
    // line comments inside are not affected by either state

    // */

    // You can manipulate expressions more easily with block comments
    // than with line comments. Try deleting the comment delimiters
    // to change the result:
    let x = 5 +  90 +  5;
    println!("Is `x` 10 or 100? x = {}", x);
}
```

### ./03_day/2.rs

```rust
fn main() {

    println!("{} days", 31);

    // Positional arguments can be used. Specifying an integer inside `{}`
    // determines which additional argument will be replaced. Arguments start
    // at 0 immediately after the format string.
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
/*
    // As can named arguments.
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

    // Different formatting can be invoked by specifying the format character
    // after a `:`.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c

    // You can right-justify text with a specified width. This will
    // output "    1". (Four white spaces and a "1", for a total width of 5.)
    println!("{number:>5}", number=1);

    // You can pad numbers with extra zeroes,
    println!("{number:0>5}", number=1); // 00001
    // and left-adjust by flipping the sign. This will output "10000".
    println!("{number:0<5}", number=1); // 10000

    // You can use named arguments in the format specifier by appending a `$`.
    println!("{number:0>width$}", number=1, width=5);

    // Rust even checks to make sure the correct number of arguments are used.
    println!("My name is {0}, {1} {0}", "Bond");
    // FIXME ^ Add the missing argument: "James"
*/
    // Only types that implement fmt::Display can be formatted with `{}`. User-
    // defined types do not implement fmt::Display by default.

    #[allow(dead_code)] // disable `dead_code` which warn against unused module
    struct Structure(i32);

    // This will not compile because `Structure` does not implement
    // fmt::Display.
    // println!("This struct `{}` won't print...", Structure(3));
    // TODO ^ Try uncommenting this line

    // For Rust 1.58 and above, you can directly capture the argument from a
    // surrounding variable. Just like the above, this will output
    // "    1", 4 white spaces and a "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

### ./03_day/2_1.rs

```rust
fn main() {
    let pi: f64 = 3.141592;
    println!("Value of pi: {pi:.3}");
}
```

### ./03_day/3_1.rs

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Pretty print
    println!("{:#?}", peter);
}
```

### ./03_day/3.rs

```rust
// Derive the `fmt::Debug` implementation for `Structure`. `Structure`
// is a structure which contains a single `i32`.
#[derive(Debug)]
struct Structure(i32);

// Put a `Structure` inside of the structure `Deep`. Make it printable
// also.
#[derive(Debug)]
struct Deep(Structure);
fn main() {
    // Printing with `{:?}` is similar to with `{}`.
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` is printable!
    println!("Now {:#?} will print!", Structure(3));

    // The problem with `derive` is there is no control over how
    // the results look. What if I want this to just show a `7`?
    println!("Now {:#?} will print!", Deep(Structure(7)));
}
```

### ./03_day/4.rs

```rust
// Import (via `use`) the `fmt` module to make it available.
use std::fmt;

// Define a structure for which `fmt::Display` will be implemented. This is
// a tuple struct named `Structure` that contains an `i32`.
struct Structure(i32);

// To use the `{}` marker, the trait `fmt::Display` must be implemented
// manually for the type.
impl fmt::Display for Structure {
    // This trait requires `fmt` with this exact signature.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Write strictly the first element into the supplied output
        // stream: `f`. Returns `fmt::Result` which indicates whether the
        // operation succeeded or failed. Note that `write!` uses syntax which
        // is very similar to `println!`.
        write!(f, "{}", self.0)
    }
}

```

### ./03_day/4_1.rs

```rust
use std::fmt; // Import `fmt`

// A structure holding two numbers. `Debug` will be derived so the results can
// be contrasted with `Display`.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implement `Display` for `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Use `self.number` to refer to each positional data point.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Define a structure where the fields are nameable for comparison.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// Similarly, implement `Display` for `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Customize so only `x` and `y` are denoted.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Compare structures:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("The big range is {big:?} and the small is {small:?}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    // Error. Both `Debug` and `Display` were implemented, but `{:b}`
    // requires `fmt::Binary` to be implemented. This will not work.
    // println!("What does Point2D look like in binary: {:b}?", point);
}
```

### ./03_day/4_2.rs

```rust
/*
 After checking the output of the above example, use the Point2D struct as a guide to add a Complex struct to the example. When printed in the same way, the output should be:

Display: 3.3 +7.2i
Debug: Complex { real: 3.3, imag: 7.2 }

Display: 4.7 -2.3i
Debug: Complex { real: 4.7, imag: -2.3 }
Bonus: Add a space before the +/- signs.
 * */

use std::fmt;

#[derive(Debug)]
struct Complex{
    real: f64,
    imag: f64 ,
}

impl fmt::Display for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, " {0} {1:+}i", self.real, self.imag)
    }
}
fn main() {
		let comp1 = Complex {real: 3.3, imag: 7.2,};
		// println!("Debug: real {0:}, imag: {1:+}i", comp.real, comp.imag);
    println!("Display: {}", comp1);
		println!("Debug: {:?}", comp1);

		let comp2 = Complex {real: 4.7, imag: -2.3,};
		// println!("Debug: real {0:}, imag: {1:+}i", comp.real, comp.imag);
    println!("Display: {}", comp2);
		println!("Debug: {:?}", comp2);
}
```

### ./03_day/4_3.rs

```rust
// Import (via `use`) the `fmt` module to make it available.
use std::fmt;

// Define a structure for which `fmt::Display` will be implemented. This is
// a tuple struct named `Structure` that contains an `i32`.
#[derive(Debug)]
struct Structure(i32);

// To use the `{}` marker, the trait `fmt::Display` must be implemented
// manually for the type.
impl fmt::Display for Structure {
    // This trait requires `fmt` with this exact signature.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Write strictly the first element into the supplied output
        // stream: `f`. Returns `fmt::Result` which indicates whether the
        // operation succeeded or failed. Note that `write!` uses syntax which
        // is very similar to `println!`.
        write!(f, "{}", self.0)
    }
}
fn main() {
    let t = Structure(32);
    println!("Display: {}", t);
    println!("Debug: {:#?}", t);
}
```

### ./03_day/5.rs

```rust
use std::fmt; // Import the `fmt` module.

// Define a structure named `List` containing a `Vec`.
#[derive(Debug)]
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extract the value using tuple indexing,
        // and create a reference to `vec`.
        let vec = &self.0;

        write!(f, "[")?;

        // Iterate over `v` in `vec` while enumerating the iteration
        // index in `index`.
        for (index, v) in vec.iter().enumerate() {
            // For every element except the first, add a comma.
            // Use the ? operator to return on errors.
            if index != 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // Close the opened bracket and return a fmt::Result value.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3, 6, 9]);
    println!("{}", v);
    println!("{:?}", v);
}

/*
Try `write!` to see if it errors. If it errors, return
the error. Otherwise continue.
write!(f, "{}", value)?;
*/

```

### ./03_day/5_1.rs

```rust
use std::fmt;

#[derive(Debug)]
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let vec = &self.0;

        write!(f, "[")?;

        for (index, v) in vec.iter().enumerate() {
            if index != 0 {
                write!(f, ", ")?;
            }
            write!(f, "{index}: {v}")?;
        }

        write!(f, "]")
    }
}

fn main() {
    let x = List(vec![1, 2, 3]);
    println!("Display: {}", x);
    println!("Debug: {:?}", x);
}
```

### ./03_day/6_1.rs

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitude
    lat: f32,
    // Longitude
    lon: f32,
}

impl Display for City {
    // `f` is a buffer, and this method must write the formatted string into it.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` is like `format!`, but it will write the formatted string
        // into a buffer (the first argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{:?}", color);
    }
}
```

### ./03_day/6.rs

```rust
use std::fmt::{self, Formatter, Display};

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

impl Display for Color {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let hex_code = format!("0x{:0>2.2X}{:0>2.2X}{:0>2.2X}", self.red, self.green, self.blue);
        write!(f, "RGB ({}, {}, {}) {}", self.red, self.green, self.blue, hex_code)
    }

}

fn main() {
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{}", color);
    }
}
```

### ./03_day/7.rs

```rust
fn main(){
    let number = 10;
    println!("The number {} is {}", number, classify_number(number));

    let number = -5;
    println!("The number {} is {}", number, classify_number(number));

    let number = 0;
    println!("The number {} is {}", number, classify_number(number));
}

fn classify_number(n: i32) -> &'static str{
    if n > 0{
        "positive"
    } else if n < 0{
        "negative"
    } else {
        "zero"
    }
}

```

### ./03_day/8.rs

```rust
fn main() {
    assert_eq!(sum_loop(100), sum_for(100));
    assert_eq!(sum_loop(100), sum_while(100));
    let n = 10;
    println!("Sum using loop: {}", sum_loop(n));
    println!("Sum using while: {}", sum_while(n));
    println!("Sum using for: {}", sum_for(n));
}


fn sum_loop(n: u32) -> u32{
    let mut sum = 0;
    let mut i = 1;
    loop {
        if i > n {
            break sum;
        }
        sum += i;
        i += 1;
    }
}

fn sum_while(n: u32) -> u32{
    let mut sum = 0;
    let mut i = 1;
    while i <= n{
        sum += i;
        i += 1;
    }
    sum
}
fn sum_for(n: u32) -> u32{
    let mut sum = 0;
    for i in 1..=n {
        sum += i;
    }
    sum
}
```

### ./03_day/9.rs

```rust
fn main() {
    let n = 5;
    println!("{} is {}", n, number_kind(n));
}

fn number_kind(n: i32) -> &'static str {
    match n {
        ..=-1 => "negative",
        0 => "zero",
        1..=10 => "one to ten",
        _ => "catch all",
    }
}
```

### ./03_day/10.rs

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main(){
    assert_eq!(describe_point(Point {x:0, y:0}), "origin");
    assert_eq!(describe_point(Point {x:1, y:0}), "x axis");
    assert_eq!(describe_point(Point {x:0, y:1}), "y axis");
    assert_eq!(describe_point(Point {x:1, y:1}), "somewhere else");
}

fn describe_point(p: Point) -> &'static str {
    match p {
        Point {x: 0, y:0} => "origin",
        Point {x, y:0} => "x axis",
        Point {x:0, y} => "y axis",
        Point {x, y} => "somewhere else",
    }
}
```

### ./03_day/11.rs

```rust
fn main() {
    assert_eq!(safe_div(1.0, 2.0), Some(0.5));
    assert_eq!(safe_div(5.0, 0.0), None);

    assert_eq!(safe_div_match(1.0, 2.0), Some(0.5));
    assert_eq!(safe_div_match(5.0, 0.0), None);

    assert_eq!(safe_div_result(1.0, 2.0), Ok(0.5));
    assert!(safe_div_result(1.0, 0.0).is_err());
}

fn safe_div(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 {
        None
    } else{
        Some(a / b)
    }
}
 
fn safe_div_match(a: f64, b: f64) -> Option<f64> {
    match b{
        0.0 => None,
        _ => Some(a/b)
    }
}

fn safe_div_result(a: f64, b: f64) -> Result<f64, String> {
    match b{
        0.0 => Err("Division by zero".to_string()),
        _ => Ok(a / b)
    }
}
```

### ./03_day/12.rs

```rust
fn main() {
    crash_example();
}

fn crash_example() {
    let x: Option<i32> = None;
    x.unwrap();
}
```

### ./03_day/mini_calculator_cli/src/main.rs

```rust
fn main() {
    let mut args = std::env::args();
    args.next(); // skip program name

    let a = args.next();
    let o = args.next();
    let b = args.next();

    match calculate(a, o, b) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => eprintln!("Error: {}", error),
    }
}

fn calculate(
    a: Option<String>,
    o: Option<String>,
    b: Option<String>,
) -> Result<f64, String> {

    let a_str = a.ok_or("Missing first number")?;
    let op = o.ok_or("Missing operator")?;
    let b_str = b.ok_or("Missing second number")?;

    let a: f64 = a_str.parse().map_err(|_| "Invalid first number")?;
    let b: f64 = b_str.parse().map_err(|_| "Invalid second number")?;

    match op.as_str() {
        "+" => Ok(a + b),
        "-" => Ok(a - b),
        "*" => Ok(a * b),
        "/" => {
            if b == 0.0 {
                Err("Division by zero".into())
            } else {
                Ok(a / b)
            }
        }
        _ => Err("Invalid operator".into()),
    }
}
```


