---
title: "Day 4"
date: "2026-02-22"
author: "You"
tags: ["rust", "python", "practical_learning", "4","day4"]
description: "A Learning Day with ChatGPT Project_Learn/Day-4."
---

# Project Dump: ./04_day/

## Project Structure

```text
./04_day/
├── 1_1.rs
├── 1.rs
├── 2.rs
├── 3_1.rs
├── 3.rs
├── 4.rs
├── 5_1
├── 5_1.rs
├── 5.rs
├── 6
├── 6.rs
├── 7
└── 7.rs

1 directory, 13 files
```

## File Contents

### ./04_day/1_1.rs

```rust
fn main() {
    // Variables can be type annotated.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // Regular annotation
    let an_integer   = 5i32; // Suffix annotation

    // Or a default will be used.
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    // A type can also be inferred from context.
    let mut inferred_type = 12; // Type i64 is inferred from another line.
    inferred_type = 4294967296i64;

    // A mutable variable's value can be changed.
    let mut mutable = 12; // Mutable `i32`
    mutable = 21;

    // Error! The type of a variable can't be changed.
    // mutable = true;

    // Variables can be overwritten with shadowing.
    let mutable = true;

    /* true;Compound types - Array and Tuple */

    // Array signature consists of Type T and length as [T; length].
    let my_array: [i32; 5] = [1, 2, 3, 4, 5];

    // Tuple is a collection of values of different types
    // and is constructed using parentheses ().
    let my_tuple = (5u32, 1u8, true, -5.04f32);
}
```

### ./04_day/1.rs

```rust
fn main() {
    // Integer addition
    println!("1 + 2 = {}", 1u32 + 2);

    // Integer subtraction
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Try changing `1i32` to `1u32` to see why the type is important

    // Scientific notation
    println!("1e4 is {}, -2.5e-3 is {}", 1e4, -2.5e-3);

    // Short-circuiting boolean logic
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Bitwise operations
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0OR011  0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // Use underscores to improve readability!
    println!("One ten lakh (million) is written as {}", 1_000_000u32);
}
```

### ./04_day/2.rs

```rust
// Tuples can be used as function arguments and as return values.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` can be used to bind the members of a tuple to variables.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// The following struct is for the activity.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // A tuple with a bunch of different types.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true, false, 'b', "hello");

    // Values can be extracted from the tuple using tuple indexing.
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);
    println!("Too long tuple: {}", long_tuple);
    // Tuples can be tuple members.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuples are printable.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // But long Tuples (more than 12 elements) cannot be printed.
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // To create one element tuples, the comma is required to tell them apart
    // from a literal surrounded by parentheses.
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // Tuples can be destructured to create bindings.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

### ./04_day/3.rs

```rust
use std::fmt;

// Tuples can be used as function arguments and as return values.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` can be used to bind the members of a tuple to variables.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// The following struct is for the activity.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result{
        write!(f, "({} {})\n({} {})", self.0, self.1, self.2, self.3)
    }
}


fn main() {
    // A tuple with a bunch of different types.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true, false, 'b', "hello");

    // Values can be extracted from the tuple using tuple indexing.
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);

    // Tuples can be tuple members.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuples are printable.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // But long Tuples (more than 12 elements) cannot be printed.
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // To create one element tuples, the comma is required to tell them apart
    // from a literal surrounded by parentheses.
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // Tuples can be destructured to create bindings.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{}", matrix);
    println!("{:?}", matrix);
}
```

### ./04_day/3_1.rs

```rust
use std::fmt;

// Tuples can be used as function arguments and as return values.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` can be used to bind the members of a tuple to variables.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// The following struct is for the activity.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result{
        write!(f, "({} {})\n({} {})", self.0, self.1, self.2, self.3)
    }
}


fn main() {
    // A tuple with a bunch of different types.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true, false, 'b', "hello");

    // Values can be extracted from the tuple using tuple indexing.
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);

    // Tuples can be tuple members.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuples are printable.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // But long Tuples (more than 12 elements) cannot be printed.
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // To create one element tuples, the comma is required to tell them apart
    // from a literal surrounded by parentheses.
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // Tuples can be destructured to create bindings.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{}", matrix);
    println!("{:?}", matrix);
    
    println!("{}", transpose(matrix));
    
}

fn transpose(matrix: Matrix) -> Matrix {
    
    Matrix(matrix.0, matrix.2, matrix.1, matrix.3)
}

```

### ./04_day/4.rs

```rust
enum Operation {
    Add,
    Sub,
    Mul,
    Div,
}

fn main() {
    let op = Operation::Add;

    match op{
        Operation::Add => println!("Addition"),
        Operation::Sub => println!("Subtraction"),
        Operation::Mul => println!("Multiplication"),
        Operation::Div => println!("Division"),
    }
}
```

### ./04_day/5.rs

```rust
#[derive(Debug)]
enum Operation{
    Add(f64, f64),
    Sub(f64, f64),
    Mul(f64, f64),
    Div(f64, f64),
}

fn main() {
    // assert_eq!("Operation::Add(3, 5)", 5);
    println!("{:?}", calculation(Operation::Add(3.0, 5.0)));
    assert_eq!(calculation(Operation::Sub(5.0, 3.0)), Ok(2.0));
    assert_eq!(calculation(Operation::Div(10.0, 0.0)), Err("Cannot divide by zero".to_string()));
    println!("{:?}", calculation(Operation::Div(10.0, 0.0)));
    
}

fn calculation(op: Operation) -> Result<f64, String> {
    match op{
        Operation::Add(a, b) => Ok(a + b),
        Operation::Sub(a, b) => Ok(a - b),
        Operation::Mul(a, b) => Ok(a * b),
        Operation::Div(a, b) => {
            if b == 0.0 {
                Err("Cannot divide by zero".to_string())
            } else {
                Ok(a / b)
            }
        }
    }
}
```

### ./04_day/5_1.rs

```rust
enum Operation{
    Add(f64, f64),
    Sub(f64, f64),
    Mul(f64, f64),
    Div(f64, f64),
}

fn main() {
    assert_eq!(calculation(&Operation::Add(3.0, 5.0)), Ok(8.0));
}

fn calculation(op: &Operation) -> Result<f64, String> {
    match op {
        Operation::Add(a, b) => Ok(*a + *b),
        Operation::Sub(a, b) => Ok(*a - *b),
        Operation::Mul(a, b) => Ok(*a * *b),
        Operation::Div(a, b) => {
            if *b == 0.0 {
                Err("Cannot divide by zero".to_string())
            } else {
                Ok(*a / *b)
            }
        }
    }
}
```

### ./04_day/6.rs

```rust
#[derive(Debug)]
struct User{
    name: String,
    age: u32,
}

fn main() {
    let user = User {
        name: String::from("Alice"),
        // why not this: "Alice".to_string() instead of String::from("Alice") 
        age: 25,
    };
    /*
    let name = user.name;
    println!("{}", user);
    This does not complied and thats what we expexted because the user is in partial move form right now.

    */
    let name = &user.name;
    println!("{:?}", user);

}
/*
 Now We Separate 3 Cases Clearly
Case 1 — Borrow (Valid)
let name = &user.name;
println!("{:?}", user);

✔ Compiles
✔ No move
✔ user still valid

Case 2 — Partial Move (Field access allowed)
let name = user.name;
println!("{}", user.age);

✔ Compiles
✘ user as a whole unusable
✔ remaining field usable

Case 3 — Partial Move + Whole Struct Use (Error)
let name = user.name;
println!("{:?}", user);

✘ Does NOT compile

*/
```

### ./04_day/7.rs

```rust
trait Describable {
    fn describe(&self) -> String;

    fn short_name(&self) -> &str {
        "Generic"
    }
}

struct User {
    name: String,
    age: u32,
}

impl Describable for User {
    fn describe(&self) -> String {
        format!("User: {} ({})", self.name, self.age)
    }
    fn short_name(&self) -> &str {
        &self.name
    }
}

enum Operation {
    Add(f64, f64),
    Sub(f64, f64),
    // Mul(f64, f64),
    // Div(f64, f64),
}

impl Describable for Operation {
    fn describe(&self) -> String {
        match self {
            Operation::Add(a, b) => format!("Add {} and {}", a, b),
            Operation::Sub(a, b) => format!("Subtract {} and {}", b, a),
        }
    }
}

fn print_description<T: Describable>(item: &T) {
    println!("{}", item.describe());
    println!("{}", item.short_name());
}

fn main() {
    // println!("{}", user.short_name());
    // println!("{}", op.short_name());
    print_description(&User{name: "Alice".to_string(), age: 25});
    print_description(&Operation::Add(3.0, 4.0));
}
```


