---
title: "Day 1"
date: "2026-02-19"
author: "You"
tags: ["rust", "python", "practical_learning", "1","day1"]
description: "A Learning Day with ChatGPT Project_Learn/Day-1."
---

# Project Dump: ./01_day/

## Project Structure

```text
./01_day/
├── 1.rs
├── 2.rs
├── 3.rs
├── 4.rs
├── 5.rs
└── 6.rs

1 directory, 6 files
```

## File Contents

### ./01_day/1.rs

```rust
fn main(){

let x  = 5;// immutable by default
let mut y = 0; // mutable variable
// NOTE y++ doesn't exist in rust.
y += 1;    // i guess so
y = y + 1;
// I have never written rust in my life so this is my best assumption of how it works.
println!("{}", x);
println!("{}", y);
// I also dont know what a macro is.
}
```

### ./01_day/2.rs

```rust
fn main(){
    let x = 5;
    let mut y = x ;
    y += 5;
    println!("{}", x);
    println!("{}", y);
}
```

### ./01_day/3.rs

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; //transfers the ownership.

    println!("{}", s2); // as s1 becomes invalid.
}
```

### ./01_day/4.rs

```rust
fn main() {
    let s = String::from("Hello, World");
    let length = length(&s);
    println!("{}", length);
}

fn length(s: &String) -> usize {
    s.len()
}
/*
1️⃣ Explicit return (like C)
return s.len();

2️⃣ Implicit return (preferred style)
s.len()


Semicolon controls this behavior.

Semicolon = statement
No semicolon = expression returned

This is fundamental.

## What is usize?

usize = unsigned size integer.

It is:

Unsigned (no negative)

Platform dependent size

64-bit machine → 64 bits

32-bit machine → 32 bits

Used for:

Indexing

Lengths

Memory sizes

Why not i32?

Because sizes cannot be negative.

Is .len() default in Rust?

Yes.

It is a method defined on:

String

Vec

Slices

Arrays

It returns usize.

Now we evaluate your borrowing answers.What is usize?

usize = unsigned size integer.

It is:

Unsigned (no negative)

Platform dependent size

64-bit machine → 64 bits

32-bit machine → 32 bits

Used for:

Indexing

Lengths

Memory sizes

Why not i32?

Because sizes cannot be negative.

Is .len() default in Rust?

Yes.

It is a method defined on:

String

Vec

Slices

Arrays

It returns usize.

Now we evaluate your borrowing answers.
 */
```

### ./01_day/5.rs

```rust
fn main() {
    let mut s = String::from("Hello");
    append_exclamation(& mut s);
    println!{"{}", s};
}
fn append_exclamation(s: &mut String) {
    s.push('!');
    // I dont know how to appen ! to a string
}
```

### ./01_day/6.rs

```rust
fn main() {
    let mut s = String::from("Hello");
    add_suffix(&mut s);

    println!("{}", s);
}

fn add_suffix(s: & mut String) {
    s.push_str(" World");
}
```


