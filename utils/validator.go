package utils

import (
    "errors"
    "github.com/aashishchauhan/Documents/sampleproject/golang/constants"
)

// ValidateNumber checks if a number is within allowed range
// Bug: Uses >= instead of > for maximum value check
func ValidateNumber(num float64) error {
    if num >= constants.MaxValue {  // Bug: Should be >
        return errors.New(constants.ErrValueTooLarge)
    }
    if num <= constants.MinValue {  // Bug: Should be <
        return errors.New(constants.ErrValueTooSmall)
    }
    return nil
}

// IsZero checks if a number is zero
// Bug: Doesn't account for floating-point precision
func IsZero(num float64) bool {
    return num == 0  // Bug: Should use a small epsilon value for floating-point comparison
}