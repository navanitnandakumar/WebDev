// 'If' statement :-

// if (condition){
//     Code to be executed if condition is true
// }

if (true) {
    console.log("Executed");
}

var hot = false;
var temp = 60;
if (temp > 80) {
    hot = true;
}
console.log(hot);

temp = 100;
if (temp > 80) {
    hot = true;
}
console.log(hot);

// 'If-else' statement :-

// if (condition){
//     Code to be executed if condition is true
// }else{
//     Code to be executed otherwise
// }

temp = 60;
if (temp > 80) {
    console.log("Hot");
} else {
    console.log("Not hot");
}

temp = 100;
if (temp > 80) {
    console.log("Hot");
} else {
    console.log("Not hot");
}

// 'If-else if-else' statement :-

// if (condition 1){
//     Code to be executed if condition 1 is true
// }else if(condition 2){
//     Code to be executed if condition 2 is true
// }else{
//     Code to be executed otherwise
// }

temp = 60;
if (temp >= 80) {
    console.log("Very hot");
} else if (temp >= 50) {
    console.log("Hot");
} else {
    console.log("Not hot");
}

temp = 100;
if (temp >= 80) {
    console.log("Very hot");
} else if (temp >= 50) {
    console.log("Hot");
} else {
    console.log("Not hot");
}

temp = 30;
if (temp >= 80) {
    console.log("Very hot");
} else if (temp >= 50) {
    console.log("Hot");
} else {
    console.log("Not hot");
}

var marks = prompt("Enter your marks :-");
var grade;
if (marks >= 90) {
    grade = 'A';
} else if (marks >= 80 && marks < 90) {
    grade = 'B';
} else if (marks >= 70 && marks < 80) {
    grade = 'C';
} else if (marks >= 60 && marks < 70) {
    grade = 'D';
} else if (marks >= 50 && marks < 60) {
    grade = 'E';
} else {
    grade = 'F';
}
alert(grade);

if (grade == 'A' || grade == 'B') {
    alert("Good job!");
} else if (grade == 'C' || grade == 'D') {
    alert("Average...");
} else if (grade == 'E') {
    alert("Poor performance!");
} else {
    alert("Failed!");
}