package calculator

import (
    "fmt"
    "github.com/aashishchauhan/Documents/sampleproject/golang/constants"
    "github.com/aashishchauhan/Documents/sampleproject/golang/utils"
)

// Add adds two numbers
func Add(a, b float64) (float64, error) {
    if err := utils.ValidateNumber(a); err != nil {
        return 0, err
    }
    if err := utils.ValidateNumber(b); err != nil {
        return 0, err
    }
    
    result := a + b
    // Bug: No validation on the result
    return result, nil
}

// Subtract subtracts two numbers
// Bug: Wrong order of operands
func Subtract(a, b float64) (float64, error) {
    if err := utils.ValidateNumber(a); err != nil {
        return 0, err
    }
    if err := utils.ValidateNumber(b); err != nil {
        return 0, err
    }
    
    result := b - a  // Bug: Wrong order, should be a - b
    return result, nil
}

// Multiply multiplies two numbers
func Multiply(a, b float64) (float64, error) {
    if err := utils.ValidateNumber(a); err != nil {
        return 0, err
    }
    if err := utils.ValidateNumber(b); err != nil {
        return 0, err
    }
    
    result := a * b
    return result, nil
}

// Divide divides two numbers
// Bug: Insufficient division by zero check
func Divide(a, b float64) (float64, error) {
    if err := utils.ValidateNumber(a); err != nil {
        return 0, err
    }
    if err := utils.ValidateNumber(b); err != nil {
        return 0, err
    }
    
    if utils.IsZero(b) {  // Bug: Uses problematic zero check
        return 0, fmt.Errorf(constants.ErrDivideByZero)
    }
    
    result := a / b
    return result, nil
}