# BeetleLang

Beetle is simple language written in two digit hex pairs.

## Installation


## Usage

### Hello World
Printing "Hello World!" in Beetle is the following

`ff 02 0c 48 65 6c 6c 6f 20 57 6f 72 6c 64 21`


## Syntax Rules

### Printing
`ff <expression>`

Outputs the object or expression.


**Example**
`ff 01 02 10 00`

Prints `4096` because `1000` in base 16 in `4096` in base 10..


### Integers
`01 <pair_digit_count> <pair_digit_one> <pair_digit_two> ... <final_digit>`

Creates an integer object out of hex pair digits

**Example**
`01 02 a1 01`

An integer with two pairs interpreted as `a101`.
First hex pair, marks this as an integer expression. 
Second pair, tells beetle how many more hex pairs to interpret as digits after it.
Third and fourth pairs, are concatenated into a hex number and intepreted in base 16.

### Operations

#### Adding
`10 <expression> <expression>`

Returns the first expression added with the second expression

#### Subtraction
`11 <expression> <expression>`

Returns the first expression minus the second expression

#### Multiplication
`12 <expression> <expression>`

Returns the first expression multiplied by the second expression

#### Dividing
`13 <expression> <expression>`

Returns the first expression divided by the second expression

