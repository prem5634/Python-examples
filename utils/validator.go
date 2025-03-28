package utils

import (
    "errors"
    "github.com/aashishchauhan/Documents/sampleproject/golang/constants"
)

// ValidateNumber checks if a number is within allowed range
func ValidateNumber(num float64) error {
    if num >= constants.MaxValue {  
        return errors.New(constants.ErrValueTooLarge)
    }
    if num <= constants.MinValue {  
        return errors.New(constants.ErrValueTooSmall)
    }
    return nil
}

// IsZero checks if a number is zero
// Bug: Doesn't account for floating-point precision
func IsZero(num float64) bool {
    return num == 0 
}
