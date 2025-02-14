package main

import (
    "fmt"
    "log"
    "github.com/aashishchauhan/Documents/sampleproject/golang/calculator"
)

func main() {
    // Test calculations with some edge cases to demonstrate bugs
    
    // Bug 1: Will pass validation despite being at max value
    result1, err := calculator.Add(1000000, 5)
    if err != nil {
        log.Printf("Addition error: %v\n", err)
    } else {
        fmt.Printf("1000000 + 5 = %f\n", result1)
    }
    
    // Bug 2: Wrong subtraction order
    result2, err := calculator.Subtract(10, 5)
    if err != nil {
        log.Printf("Subtraction error: %v\n", err)
    } else {
        fmt.Printf("10 - 5 = %f (but will show -5 due to bug)\n", result2)
    }
    
    // Bug 3: Division by zero with problematic zero check
    result3, err := calculator.Divide(10, 0.0000001)
    if err != nil {
        log.Printf("Division error: %v\n", err)
    } else {
        fmt.Printf("10 / 0.0000001 = %f\n", result3)
    }
    
    // Normal calculation that should work
    result4, err := calculator.Multiply(4, 5)
    if err != nil {
        log.Printf("Multiplication error: %v\n", err)
    } else {
        fmt.Printf("4 * 5 = %f\n", result4)
    }
}