// Comparison operators :-

console.log(3 > 2); // Greater than
console.log(2 > 3);
console.log(1 < 2); // Less than
console.log(2 >= 2); // Greater than or equal to
console.log(1 <= 3); // Less thanor equal to
console.log(2 == 2); // Equal to
console.log("user" == "user");
console.log(2 != 3); // Not equal to
console.log("user" != "user");

console.log("2" == 2); // Javascript is going to say this is true, as it uses type conversion
console.log("2" === 2); // But this is going to be false, because here, no type conversion is used
console.log("5" != 5); // Type conversion occurs before comparison
console.log("5" !== 5); // No type conversion

// In javascript, 'true' is considered to be '1' and 'false' is considered to be '0'
console.log(true == 1);
console.log(true == 0);
console.log(true === 1); // This is going to be false
console.log(false == 0);
console.log(false == 1);
console.log(false === 0); // This is also going to be false

console.log(null == undefined); // This will give true
console.log(null === undefined); // But, this gives false
console.log(NaN == NaN); // This will give false

// Logical operators :-

console.log(1 == 1 && 2 == 2); // 'AND' operator
console.log(1 === 1 && 2 === 2 && 1 === 2);
console.log(1 === 1 || 1 === "1"); // 'OR' operator
console.log(!(2 === 2)); // 'NOT' operator
console.log(!!(2 === 2));
console.log(!(2 === '2'));