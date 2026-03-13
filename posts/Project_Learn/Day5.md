---
title: "Day 5"
date: "2026-02-23"
author: "You"
tags: ["rust", "python", "practical_learning", "5","day5"]
description: "A Learning Day with ChatGPT Project_Learn/Day-5."
---

# Project Dump: ./05_day/

## Project Structure

```text
./05_day/
├── 1_1.rs
├── 1_2.rs
├── 1.rs
├── 2.rs
├── 3.rs
├── 4.rs
├── 5_1.rs
├── 5_2.rs
├── 5.rs
├── 6.rs
├── 7.rs
├── 8.rs
└── rust_day5
    ├── Cargo.toml
    ├── .gitignore
    └── src
        ├── main.rs
        ├── operations
        │   ├── add.rs
        │   ├── mod.rs
        │   └── multiply.rs
        └── traits.rs

4 directories, 19 files
```

## File Contents

### ./05_day/1.rs

```rust
// An attribute to hide warnings for unused code.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// A unit struct
struct Unit;

// A tuple struct
struct Pair(i32, f32);

// A struct with two fields
struct Point {
    x: f32,
    y: f32,
}

struct rect_area {
    x: f32,
    y: f32,
    x*y
}
// Structs can be reused as fields of another struct
struct Rectangle {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    top_left: Point,
    bottom_right: Point,

}

fn main() {
    // Create struct with field init shorthand
    let name= String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Print debug struct
    println!("{:?}", peter);

    // Instantiate a `Point`
    let point: Point = Point { x: 5.2, y: 0.4 };
    let another_point: Point = Point { x: 10.3, y: 0.2 };

    // Access the fields of the point
    println!("point coordinates: ({}, {})", point.x, point.y);

    // Make a new point by using struct update syntax to use the fields of our
    // other one
    let bottom_right: Point = Point { x: 10.3, ..another_point };

    // `bottom_right.y` will be the same as `another_point.y` because we used that field
    // from `another_point`
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // Destructure the point using a `let` binding
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // struct instantiation is an expression too
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Instantiate a unit struct
    let _unit = Unit;

    // Instantiate a tuple struct
    let pair = Pair(1, 0.2);

    // Access the fields of a tuple struct
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // Destructure a tuple struct
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

### ./05_day/1_1.rs

```rust
// An attribute to hide warnings for unused code.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// A unit struct
struct Unit;

// A tuple struct
struct Pair(i32, f32);

// A struct with two fields
#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
}

#[derive(Debug)]
// Structs can be reused as fields of another struct
struct Rectangle {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    top_left: Point,
    bottom_right: Point,

}

fn rect_area(rect: Rectangle) -> f32 {
    let x1 = rect.top_left.x;
    let y1 = rect.top_left.y;
    let x2 = rect.bottom_right.x;
    let y2 = rect.bottom_right.y;
   let result = (x2 - x1)*(y2 -y1);
       if result < 0.0 {
           result * -1.0
       } else {
           result
       }
}

fn main() {
    // Create struct with field init shorthand
    let name= String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Print debug struct
    println!("{:?}", peter);

    // Instantiate a `Point`
    let point: Point = Point { x: 5.2, y: 0.4 };
    let another_point: Point = Point { x: 10.3, y: 0.2 };

    // Access the fields of the point
    println!("point coordinates: ({}, {})", point.x, point.y);

    // Make a new point by using struct update syntax to use the fields of our
    // other one
    let bottom_right: Point = Point { x: 10.3, ..another_point };

    // `bottom_right.y` will be the same as `another_point.y` because we used that field
    // from `another_point`
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // Destructure the point using a `let` binding
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // struct instantiation is an expression too
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };
    println!("{:?}", _rectangle);
    println!("The area of the rectangle is: {}", rect_area(_rectangle));

    // Instantiate a unit struct
    let _unit = Unit;

    // Instantiate a tuple struct
    let pair = Pair(1, 0.2);

    // Access the fields of a tuple struct
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // Destructure a tuple struct
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

### ./05_day/1_2.rs

```rust
// An attribute to hide warnings for unused code.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// A unit struct
struct Unit;

// A tuple struct
struct Pair(i32, f32);

// A struct with two fields
#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
}

// Structs can be reused as fields of another struct
#[derive(Debug)]
struct Rectangle {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    top_left: Point,
    bottom_right: Point,
}

fn Square(p: Point, a: f32)  -> Rectangle {

    let point2 = Point {x: p.x + a, y: p.y + a};
    let rect = Rectangle {
        top_left: p,
        bottom_right: point2,
    };
    rect
    
}


fn main() {
    // Create struct with field init shorthand
    let name= String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Print debug struct

    // Instantiate a `Point`
    let point: Point = Point { x: 5.2, y: 0.4 };
    let another_point: Point = Point { x: 10.3, y: 0.2 };

    // Access the fields of the point

    // Make a new point by using struct update syntax to use the fields of our
    // other one
    let bottom_right: Point = Point { x: 10.3, ..another_point };

    // `bottom_right.y` will be the same as `another_point.y` because we used that field
    // from `another_point`

    // Destructure the point using a `let` binding
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // struct instantiation is an expression too
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    let square  = Square(point, 10.0);
    println!("{:?}", square);

    // Instantiate a unit struct
    let _unit = Unit;

    // Instantiate a tuple struct
    let pair = Pair(1, 0.2);

    // Access the fields of a tuple struct

    // Destructure a tuple struct
    let Pair(integer, decimal) = pair;

}
```

### ./05_day/2.rs

```rust
// Globals are declared outside all other scopes.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Access constant in some function
    n > THRESHOLD
}

fn main() {
    let n = 16;
    let name = "Alice";
    // Access constant in the main thread
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });
    
    println!("{}", name);
    
    some(name);

    // Error! Cannot modify a `const`.
    // THRESHOLD = 5;
    // FIXME ^ Comment out this line
}
fn some(name: &'static str){
     println!("{}", name);
}
```

### ./05_day/3.rs

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // copy `an_integer` into `copied_integer`
    let copied_integer = an_integer;

    println!("An integer: {:?}", copied_integer);
    println!("A boolean: {:?}", a_boolean);
    println!("Meet the unit value: {:?}", unit);

    // The compiler warns about unused variable bindings; these warnings can
    // be silenced by prefixing the variable name with an underscore
    let _unused_variable = 3u32;

    let _noisy_unused_variable = 2u32;
    // FIXME ^ Prefix with an underscore to suppress the warning
    // Please note that warnings may not be shown in a browser
}
```

### ./05_day/4.rs

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // Error! Cannot assign a new value to an immutable variable
    // _immutable_binding += 21;
}
```

### ./05_day/5.rs

```rust
fn main() {
    // This binding lives in the main function
    let long_lived_binding = 1;

    // This is a block, and has a smaller scope than the main function
    {
        // This binding only exists in this block
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);
        println!("inner long: {}", long_lived_binding);
    }
    // End of the block

    // Error! `short_lived_binding` doesn't exist in this scope
    println!("outer short: {}", short_lived_binding);
    // FIXME ^ Comment out this line

    println!("outer long: {}", long_lived_binding);
}
```

### ./05_day/5_1.rs

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("before being shadowed: {}", shadowed_binding);

        // This binding *shadows* the outer one
        let shadowed_binding = "abc";

        println!("shadowed in inner block: {}", shadowed_binding);
    }
    println!("outside inner block: {}", shadowed_binding);

    // This binding *shadows* the previous binding
    let shadowed_binding = 2;
    println!("shadowed in outer block: {}", shadowed_binding);
}
```

### ./05_day/5_2.rs

```rust
fn main() {
    // Declare a variable binding
    let a_binding;

    {
        let x = 2;

        // Initialize the binding
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Error! Use of uninitialized binding
    // println!("another binding: {}", another_binding);
    // FIXME ^ Comment out this line

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

### ./05_day/6.rs

```rust
#![allow(overflowing_literals)]
fn main() {
    let decimal = 65.4321_f32;
    println!("Decimal: {}", decimal);

    let integer = decimal as u8;
    println!("Integer: {}", integer);

    let character = integer as char;
    println!("Character: {}", character);

    // Error! There are limitations in conversion rules.
    // A float cannot be directly converted to a char.
    // let character = decimal as char;
    // FIXME ^ Comment out this line

    println!("Casting: {} -> {} -> {}", decimal, integer, character);

    // when casting any value to an unsigned type, T,
    // T::MAX + 1 is added or subtracted until the value
    // fits into the new type

    // 1000 already fits in a u16
    println!("1000 as a u16 is: {}", 1000 as u16); // reamin 1000

    // Under the hood, the first 8 least significant bits (LSB) are kept,
    // while the rest towards the most significant bit (MSB) get truncated.
    println!("1000 as a u8 is : {}", 1000 as u8); // becomes 232-> 1000 -256 *3

    println!(" -1 as a u8 is: {}", (-1i8) as u8); // becomes 255 in u8

    println!(" 1000 mod 256: {}", 1000 % 256);

    println!("128 as i8 is: {}", 128 as i8);

    // repeating the example above
    // 1000 as u8 -> 232
    println!("1000 as a u8 is : {}", 1000 as u8);
    // and the value of 232 in 8-bit two's complement representation is -24
    println!(" 232 as a i8 is : {}", 232 as i8);

    // 300.0 as u8 is 255
    println!(" 300.0 as u8 is : {}", 300.0_f32 as u8);
    // -100.0 as u8 is 0
    println!("-100.0 as u8 is : {}", -100.0_f32 as u8);
    // nan as u8 is 0
    println!("   nan as u8 is : {}", f32::NAN as u8);

    unsafe {
        // 300.0 as u8 is 44
        println!(" 300.0 as u8 is : {}", 300.0_f32.to_int_unchecked::<u8>());
        // -100.0 as u8 is 156
        println!(
            "-100.0 as u8 is : {}",
            (-100.0_f32).to_int_unchecked::<u8>()
        );
        // nan as u8 is 0
        println!("   nan as u8 is : {}", f32::NAN.to_int_unchecked::<u8>());
    }
}
```

### ./05_day/7.rs

```rust
fn main() {
    // Suffixed literals, their types are known at initialization
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Unsuffixed literals, their types depend on how they are used
    let i = 1;
    let f = 1.0;

    // `size_of_val` returns the size of a variable in bytes
    println!("size of `x` in bytes: {}", std::mem::size_of_val(&x));
    println!("size of `y` in bytes: {}", std::mem::size_of_val(&y));
    println!("size of `z` in bytes: {}", std::mem::size_of_val(&z));
    println!("size of `i` in bytes: {}", std::mem::size_of_val(&i));
    println!("size of `f` in bytes: {}", std::mem::size_of_val(&f));
}
```

### ./05_day/8.rs

```rust
fn main() {
    // Because of the annotation, the compiler knows that `elem` has type u8.
    let elem = 5u8;

    // Create an empty vector (a growable array).
    let mut vec: Vec<u16> = Vec::new();
    // At this point the compiler doesn't know the exact type of `vec`, it
    // just knows that it's a vector of something (`Vec<_>`).

    // Insert `elem` in the vector.
    vec.push(elem as u16);
    // Aha! Now the compiler knows that `vec` is a vector of `u8`s (`Vec<u8>`)
    // TODO ^ Try commenting out the `vec.push(elem)` line

    println!("{:?}", vec);
}
```

### ./05_day/rust_day5/src/operations/add.rs

```rust
use crate::traits::Operation;

pub struct Add;

impl Operation for Add {
    fn compute(&self, a: f64, b: f64) -> f64 {
        a + b
    }
}
```

### ./05_day/rust_day5/src/operations/multiply.rs

```rust
use crate::traits::Operation;

pub struct Multiply;

impl Operation for Multiply {
    fn compute(&self, a: f64, b: f64) -> f64 {
        a * b
    }
}
```

### ./05_day/rust_day5/src/operations/mod.rs

```rust
pub mod add;
pub mod multiply;

pub use add::Add;
pub use multiply::Multiply;
```

### ./05_day/rust_day5/src/traits.rs

```rust
pub trait Operation {
    fn compute(&self, a: f64, b: f64) -> f64;
}
```

### ./05_day/rust_day5/src/main.rs

```rust
mod operations;
mod traits;

use operations::{Add, Multiply};
use traits::Operation;

fn main() {
    let add = Add;
    let multiply = Multiply;

    // Static dispatch
    let result_execute_add = execute_static(add, 2.0, 3.0);
    let result_execute_mul = execute_static(multiply, 2.0, 3.0);

    println!("Static Add: {}", result_execute_add);
    println!("Static Multiply: {}", result_execute_mul);

    // Dynamic dispatch with heterogeneous vector
    let ops: Vec<Box<dyn Operation>> = vec![Box::new(Add), Box::new(Multiply)];
    for op in ops.iter() {
        let result = execute_dynamic(op.as_ref(), 4.0, 5.0);
        println!("Dynamic Result: {}", result)
    }
}

fn execute_static<T: Operation>(op: T, a: f64, b: f64) -> f64 {
    op.compute(a, b)
}

fn execute_dynamic(op: &dyn Operation, a: f64, b: f64) -> f64 {
    op.compute(a, b)
}
```


