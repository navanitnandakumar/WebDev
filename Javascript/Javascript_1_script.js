// 'alert()' causes an alert to pop-up in the webpage
alert("Welcome to the bank!");

// variables of any type are created using 'var'
// 'prompt' is used to get input from the user, which is stored as a string
var deposit = prompt("How much would you like to deposit today?");

// '+' sign can concatenate strings
alert("You've deposited " + deposit);

// 'console.log()' is used to display messages in the console 
console.log("You are a cool person!");
// access the console in the webpage by inspecting it 

// Data types in javascript :-

10
20.2
-13
-15.4
// Javascript considers all the above as just 'numbers' and there is no distinction between them

"Hello world"
"10"
"abc"
// etc are 'strings'

true
false
// are 'boolean'

undefined
null
// are some other data types

// 'clear()' is used to clear the console

// Operations in javascript :-

console.log(2 + 2); // Addition
console.log(5 - 1); // Subtraction
console.log(3 * 2); // Multiplication
console.log(10 / 2); // Division
console.log(2 / 5); // Javascript performs true division
console.log(2 ** 4); // Exponents
console.log(15 % 14); // Modulo

// '.length' gives length of a string
console.log("django".length);
console.log("x x".length);

// Escape sequences :-
console.log("This \n starts a new line."); // '\n' is used to start a new line
console.log("This \t inserts a tab."); // '\t' is used to tab
console.log("Hello \"Quotes\"!"); // '\"' is used for quotes 

// Indexing :-
console.log("hello"[0]);
console.log("hello"[4]);
console.log("hello"[2]);
console.log("Look at the dog"[12]);

// Variables :-
var varName = "value"; // Variable names are usually written in camel case in javascript

var bankAccount = 100;
var deposit = 50;
var total = bankAccount + deposit;
console.log(total);

var greeting = "Welcome back";
var myName = "Navanit";
alert(greeting + " " + myName + "!")