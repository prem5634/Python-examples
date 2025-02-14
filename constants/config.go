package constants

// Configuration constants for the calculator
const (
    MaxValue     = 1000000  // Maximum allowed value for calculations
    MinValue     = -1000000 // Minimum allowed value for calculations
    DecimalPlace = 2        // Number of decimal places for results
)

// Error messages
const (
    ErrValueTooLarge  = "value exceeds maximum allowed"
    ErrValueTooSmall  = "value below minimum allowed"
    ErrDivideByZero   = "division by zero is not allowed"
    ErrInvalidNumber  = "invalid number provided"
)