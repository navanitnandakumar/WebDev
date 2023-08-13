// 'While' loop :-

// while (condition){
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
    x = x + 1;
}

x = 2;
while (x <= 10) {
    console.log(x);
    x = x + 2;
}