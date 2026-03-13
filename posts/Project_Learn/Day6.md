---
title: "Day 6"
date: "2026-02-24"
author: "You"
tags: ["rust", "python", "practical_learning", "6","day6"]
description: "A Learning Day with ChatGPT Project_Learn/Day-6."
---

---

# Day 6 — Systems-Level Engineering: Dispatch, Error Boundaries & Performance Reality

Day 6 was not about writing more features.

It was about understanding:

* What the compiler actually does
* How dispatch behaves under optimization
* How error boundaries should be designed
* How CPython memory layout impacts performance
* How to classify workloads correctly (CPU vs Memory vs I/O bound)

This was a systems day.

---

# Part 1 — Rust Dispatch Benchmarking (The Hard Way)

## Objective

Benchmark:

* Static dispatch (`T: Compute`)
* Dynamic dispatch (`dyn Compute`)
* In release mode
* With measurable workload

---

## Phase 1 — The Benchmark That Lied

Initial results:

```
Static Duration: 83ns
Dynamic Duration: 496µs
```

This is impossible for 10 million iterations.

The compiler eliminated the loop.

Why?

Because:

* Inputs were constant
* Computation was pure
* Static dispatch enabled inlining
* LLVM replaced the loop with a constant result

We were benchmarking algebraic simplification — not dispatch.

---

## Phase 2 — Fighting the Optimizer

We introduced:

* `std::hint::black_box`
* `#[inline(never)]`
* Removed constant inputs
* Disabled LTO
* Cleaned builds
* Increased iterations

We learned:

* LTO changes inlining behavior dramatically
* `black_box` alters register allocation
* Generics produce different code layout than monomorphic functions
* Code layout can matter more than dispatch

---

## Phase 3 — Proper Isolation

Final minimal benchmark:

```rust
pub trait Compute {
    fn compute(&self, a: i64, b: i64) -> i64;
}
```

Static:

```rust
pub fn run_static(engine: &Adder, iterations: u64) -> i64 {
    let mut acc = 0;
    for _ in 0..iterations {
        acc += engine.compute(2, 3);
    }
    acc
}
```

Dynamic:

```rust
pub fn run_dynamic(engine: &dyn Compute, iterations: u64) -> i64 {
    let mut acc = 0;
    for _ in 0..iterations {
        acc += engine.compute(2, 3);
    }
    acc
}
```

Run with 100 million iterations.

---

## Final Valid Result

```
Static Duration: 257ms
Dynamic Duration: 304ms
```

Dynamic dispatch ≈ 17–18% slower in a tight loop.

This is realistic.

---

## Key Takeaways

1. Dispatch overhead is tiny per call.
2. It only becomes measurable in extremely tight loops.
3. In real-world workloads, dynamic dispatch is usually negligible.
4. Microbenchmarks can lie if you don’t isolate variables.
5. Compiler behavior must be understood before drawing conclusions.

---

# Part 2 — Error Propagation Architecture (Production Discipline)

We rebuilt the compute engine correctly.

## Clean Project Structure

```
corrected_compute_engine/
├── compute.rs
├── error.rs
├── operations.rs
├── static_exec.rs
├── dynamic_exec.rs
└── bin/main.rs
```

---

## Trait Definition

```rust
pub trait Compute {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError>;
}
```

No `unwrap` inside library code.

---

## Error Type

```rust
#[derive(Debug)]
pub enum ComputeError {
    Overflow,
    DivisionByZero,
    InvalidInput,
}
```

We implemented:

```rust
impl std::fmt::Display for ComputeError { ... }
impl std::error::Error for ComputeError {}
```

---

## Why This Matters

### 1. `Result` Is Zero-Cost

The success path compiles to simple control flow.
No heap allocation.
No exceptions.

---

### 2. `?` Uses `From`

The `?` operator expands to:

```rust
Err(e) => return Err(From::from(e))
```

So conversion must exist.

---

### 3. `main` Can Return Custom Error

This is valid:

```rust
fn main() -> Result<(), ComputeError>
```

Only `Debug` is required.

You do NOT need `Box<dyn Error>` unless you want type erasure.

---

### 4. Public Enums Are API Contracts

Adding a new variant to:

```rust
pub enum ComputeError
```

is a **breaking change**.

Downstream exhaustive matches will fail to compile.

Use:

```rust
#[non_exhaustive]
```

if future extension is expected.

---

## Architectural Lessons

* Libraries must not panic.
* Errors must be explicit.
* Public error types define API surface.
* `Box<dyn Error>` is ergonomic for applications, not libraries.

---

# Part 3 — Python Performance Reality (CPython Internals)

We ran:

```python
N = 50_000_000
```

Measured:

* List creation
* NumPy creation
* List sum
* NumPy sum
* Memory usage

---

## Results

### Creation

```
List creation: 1.46 sec
NumPy creation: 0.106 sec
```

### Sum

```
List sum: 0.45 sec
NumPy sum: 0.036 sec
```

### Memory

* NumPy: ~400MB
* Python list container: ~400MB
* Estimated total list memory: ~1.8GB (including PyLong objects)

---

## Why Python List Is Slow & Heavy

Each integer is:

* A full `PyLongObject`
* Heap allocated
* Reference counted
* Accessed via pointer indirection

Memory layout:

```
List
  → array of PyObject*
      → PyLongObject
```

Two levels of indirection.
Massive object overhead.

---

## Why NumPy Is Fast

* Single contiguous buffer
* Raw `int64`
* Tight C loop
* No interpreter in inner loop
* Hardware prefetch friendly
* Vectorization possible

---

# CPU vs Memory vs I/O Bound (Sharpening Intuition)

We rigorously classified workloads.

### Memory-Bound

* `np.add` on large arrays
* `memcpy`
* Sequential array iteration

### CPU-Bound

* SHA256 hashing
* Recursive Fibonacci
* Ray tracing
* `np.sin` on large arrays
* Neural network training (compute heavy)

### I/O-Bound

* Reading from disk
* Network downloads
* Copying large files between drives

---

## Core Heuristic

If per-element operation is:

* Simple (add/mul) → Memory-bound
* Heavy math (sin/crypto) → CPU-bound
* Disk/network involved → I/O-bound

---

# Benchmarks Summary

## Rust Dispatch (100M ops)

| Metric   | Static | Dynamic |
| -------- | ------ | ------- |
| Time     | ~258ms | ~304ms  |
| Overhead | —      | ~17–18% |

---

## Python (50M elements)

| Operation      | Time   |
| -------------- | ------ |
| List creation  | 1.46s  |
| NumPy creation | 0.10s  |
| List sum       | 0.45s  |
| NumPy sum      | 0.036s |

Memory:

* NumPy ≈ 400MB
* Python list ≈ ~1.8GB total (estimated)

---

# What Day 6 Actually Built

* Compiler reasoning skills
* Benchmark discipline
* Error boundary architecture understanding
* Semver awareness
* CPython memory model intuition
* Hardware bottleneck classification

This was not a coding day.

It was a systems thinking day.

---

# Code and Trees
```
===== PROJECT TREE =====
./
├── compute_engine
│   ├── Cargo.lock
│   ├── Cargo.toml
│   └── src
│       ├── bin
│       │   └── dispatch_bench.rs
│       ├── compute.rs
│       ├── dynamic_exec.rs
│       ├── error.rs
│       ├── lib.rs
│       └── static_exec.rs
└── corrected_compute_engine
    ├── Cargo.lock
    ├── Cargo.toml
    └── src
        ├── bin
        │   └── main.rs
        ├── compute.rs
        ├── dynamic_exec.rs
        ├── error.rs
        ├── lib.rs
        ├── operations.rs
        └── static_exec.rs

```

```>>> ./compute_engine/src/bin/dispatch_bench.rs
//===== FILE CONTENTS =====
//-------------------------
use compute_engine::{Adder, dynamic_exec::run_dynamic, static_exec::run_static,};
use std::time::Instant;
use std::hint::black_box;

fn main() {
    let iterations = 100_000_000;
    let adder = Adder;

    // Static
    let start_s = Instant::now();
    let result_static = run_static(&adder, iterations);
    black_box(result_static);
    let duration_static = start_s.elapsed();

    // Dynamic
    let start_d = Instant::now();
    let result_dynamic = run_dynamic(&adder, iterations);
    black_box(result_dynamic);
    let duration_dynamic = start_d.elapsed();

    // println!("Static Result: {}", result_static);
    println!("Static Duration: {:?}", duration_static);

    // println!("Dynamic Result: {}", result_dynamic);
    println!("Dynamic Duration: {:?}", duration_dynamic);
}
```
```>>> ./compute_engine/src/error.rs
-------------------------
#[derive(Debug)]
pub enum ComputeError {
    Overflow,
    DivisionByZero,
    InvalidInput,
}
```
```>>> ./compute_engine/src/compute.rs
-------------------------
use crate::error::ComputeError;

pub trait Compute {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError>;
}
```

```>>> ./compute_engine/src/static_exec.rs
-------------------------
use crate::compute::Compute;
// use std::hint::black_box;
use crate::ComputeError;
// use crate::Adder;

pub fn run_static<T: Compute> (engine: &T, iterations: u64) -> Result<f64, ComputeError> {
    let mut acc: f64 = 0.0;
    for _i in 0..iterations {
        // let x = black_box(i as i64);
        acc += engine.compute(2.0, 3.0)?;
    }
    Ok(acc)
}
```

```>>> ./compute_engine/src/dynamic_exec.rs
-------------------------
use crate::compute::Compute;
// use std::hint::black_box;
use crate::error::ComputeError;
pub fn run_dynamic(engine: &dyn Compute, iterations: u64) -> Result<f64, ComputeError> {
    let mut acc: f64 = 0.0;
    for _i in 0..iterations {
        // let x = black_box(i as i64);
        acc += engine.compute(2.0, 3.0)?;
    }
    Ok(acc)
}
```

```>>> ./compute_engine/src/lib.rs
-------------------------
pub mod compute;
pub mod dynamic_exec;
pub mod static_exec;
pub mod error;

use compute::Compute;
use crate::error::ComputeError;


pub struct Adder;

impl Compute for Adder {
    #[inline(never)]
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError> {
        Ok(a + b)
    }
}

pub struct Divider;

impl Compute for Divider {
    #[inline(never)]
    fn compute(&self, a: f64, b:f64) -> Result<f64, ComputeError> {
        if b == 0.0 {
            Err(ComputeError::DivisionByZero)
        } else {
            Ok(a / b)
        }
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        let adder = Adder;
let result = adder.compute(2.0, 3.0).unwrap();
assert_eq!(result, 5.0);
        // let divider = Divider;
        // let result = divider.compute(9.0, 3.0);
        // assert_eq!(result, 3.0);
    }
}
```
```>>> ./corrected_compute_engine/src/bin/main.rs
-------------------------
// src/bin/main.rs

use corrected_compute_engine::{
    Adder, Divider, dynamic_exec::run_dynamic, static_exec::run_static,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let adder = Adder;
    let divider = Divider;

    let result1 = run_static(&adder, 5.0, 9.0)?;
    println!("Static Add: {}", result1);

    let result2 = run_dynamic(&divider, 25.0, 5.0)?;
    println!("Dynamic Divide: {}", result2);

    Ok(())
}
```

```>>> ./corrected_compute_engine/src/dynamic_exec.rs
-------------------------
// src/dynamic_exec.rs

use crate::compute::Compute;
use crate::error::ComputeError;

pub fn run_dynamic(engine: &dyn Compute, a: f64, b: f64) -> Result<f64, ComputeError> {
    engine.compute(a, b)
}
```
```>>> ./corrected_compute_engine/src/compute.rs
-------------------------
// src/compute.rs

use crate::error::ComputeError;

pub trait Compute {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError>;
}
```
```> ./corrected_compute_engine/src/static_exec.rs
-------------------------
// src/static_exec.rs

use crate::compute::Compute;
use crate::error::ComputeError;

pub fn run_static<T: Compute>(engine: &T, a: f64, b: f64) -> Result<f64, ComputeError> {
    engine.compute(a, b)
}
```
```> ./corrected_compute_engine/src/operations.rs
-------------------------
// src/operations.rs

use crate::compute::Compute;
use crate::error::ComputeError;

pub struct Adder;

impl Compute for Adder {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError> {
        Ok(a + b)
    }
}

pub struct Subtractor;

impl Compute for Subtractor {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError> {
        Ok(a - b)
    }
}

pub struct Multiplier;

impl Compute for Multiplier {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError> {
        Ok(a * b)
    }
}

pub struct Divider;

impl Compute for Divider {
    fn compute(&self, a: f64, b: f64) -> Result<f64, ComputeError> {
        if b == 0.0 {
            Err(ComputeError::DivisionByZero)
        } else {
            Ok(a / b)
        }
    }
}
```

```> ./corrected_compute_engine/src/lib.rs
-------------------------
// src/lib.rs

pub mod compute;
pub mod dynamic_exec;
pub mod error;
pub mod operations;
pub mod static_exec;

pub use compute::Compute;
pub use error::ComputeError;
pub use operations::*;

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_add() {
        let adder = Adder;
        let result = adder.compute(2.0, 3.0).unwrap();
        assert_eq!(result, 5.0);
    }

    #[test]
    fn test_divide_by_zero() {
        let divider = Divider;
        let result = divider.compute(5.0, 0.0);
        assert!(matches!(result, Err(ComputeError::DivisionByZero)));
    }

    #[test]
    fn test_static_execution() {
        let multiplier = Multiplier;
        let result = static_exec::run_static(&multiplier, 4.0, 5.0).unwrap();
        assert_eq!(result, 20.0);
    }

    #[test]
    fn test_dynamic_execution() {
        let subtractor = Subtractor;
        let result = dynamic_exec::run_dynamic(&subtractor, 10.0, 3.0).unwrap();
        assert_eq!(result, 7.0);
    }
}
```

```> ./corrected_compute_engine/src/error.rs
-------------------------
// src/error.rs
use std::fmt;

#[derive(Debug)]
pub enum ComputeError {
    Overflow,
    DivisionByZero,
    InvalidInput,
}

impl fmt::Display for ComputeError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ComputeError::Overflow => write!(f, "Overflow Occured"),
            ComputeError::DivisionByZero => write!(f, "Division By Zero"),
            ComputeError::InvalidInput => write!(f, "Invalid Input"),
        }
    }
}

impl std::error::Error for ComputeError {}
```
## Python

```memory_test.py

import time
import numpy as np
import sys

N = 50_000_000

print(f"Creating {N} elements...\n")

# Python list creation
start = time.perf_counter()
lst = list(range(N))
list_creation = time.perf_counter() - start
print(f"List creation time: {list_creation:.4f} sec")

# NumPy array creation
start = time.perf_counter()
arr = np.arange(N, dtype=np.int64) # Corrected: Use np.arange to create an array of N elements
array_creation = time.perf_counter() - start
print(f"Array creation time: {array_creation:.4f} sec")

# List sum
start = time.perf_counter()
sum(lst)
list_sum = time.perf_counter() - start
print(f"List sum time: {list_sum:.4f} sec")

# NumPy sum
start = time.perf_counter()
arr.sum()
array_sum = time.perf_counter() - start
print(f"NumPy sum time: {array_sum:.4f} sec")

# Memory Usage
print(f"\nMemory usage:")
print(f"List container size: {sys.getsizeof(lst)/ 1000000} Megabytes") # Corrected: Changed label to Megabytes
print(f"NumPy array container size: {arr.nbytes / 1000000} Megabytes") # Corrected: Divide by 1M and change label to Megabytes

```
``` output:

Creating 50000000 elements...

List creation time: 1.4612 sec
Array creation time: 0.1067 sec
List sum time: 0.4521 sec
NumPy sum time: 0.0367 sec

Memory usage:
List container size: 400.000056 Megabytes
NumPy array container size: 400.0 Megabytes
```
---

# Tomorrow

We move into:

* Lifetimes across module boundaries
* Borrowing discipline at architectural scale
* Zero-cost abstraction guarantees

Day 6 complete.

