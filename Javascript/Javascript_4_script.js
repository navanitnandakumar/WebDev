// 'While' loop :-

// while (condition) {
//     Code to be exectuted as long as condition holds
// }

var x = 0;
while (x < 10) {
    console.log(x);
    x = x + 1;
}

// 'break' allows us to exit the loop prematurely

x = 0;
while (x < 10) {
    if (x == 5) {
        console.log("x is 5");
        break;
    } else {
        console.log("x is not 5");
    }
    x = x + 1;
}

x = 1;
while (x <= 10) {
    if (x % 2 == 0) {
        console.log(x);
    }
    x++;
}

x = 2;
while (x <= 10) {
    console.log(x);
    x += 2;
}

// 'For' loop :-

// for (statement 1; statement 2; statement 3) {
//     Code to be exectuted as long as condition holds
// }

// 'statement 1' is executed before the loop even begins (eg: var i = 0)
// 'statement 2' is the condition for the loop (eg: i<5)
// 'statement 3' is executed each time after the loop cycles through (eg: i++)

for (var i = 0; i < 5; i++) {
    console.log("Number is " + i);
}

var word = 'ABCDEFGHIJK'
for (let i = 0; i < word.length; i++) {
    console.log(word[i]);
}

for (let i = 0; i < word.length; i += 2) {
    console.log(word[i]);
}