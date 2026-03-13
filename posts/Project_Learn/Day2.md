---
title: "Day 2"
date: "2026-02-20"
author: "You"
tags: ["rust", "python", "practical_learning", "2","day2"]
description: "A Learning Day with ChatGPT Project_Learn/Day-2."
---







# Project Dump: ./

## Project Structure

```text
./
└── 1.rs

1 directory, 1 file
```

## File Contents

### ./1.rs

```rust
fn main() {
    let num = -5;
    let classification = classify_number(num);
    println!("{}", classification);
}

fn classify_number(n: i32) -> &'static str {
    if n < 0 {
        "negative"
    } else if n > 0 {
        "positive"
    } else {
        "zero"
    }
}
```



