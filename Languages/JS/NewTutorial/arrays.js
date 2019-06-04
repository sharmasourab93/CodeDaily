var ourArray = ["John", 23]

var myArray = ["Quincy", 1];

// Nested Arrays

var theyArrays = [["The universe", 42], ["everything", 101010]];
var myTheyArrays = [["Bulls", 23], ["White", 32]];

// Index

var ourData = ourArray[0];

var myData = myArray[1];

console.log(myData, ourData)

// Modifying array with indexes

theyArrays[1][0] = 45;

console.log(theyArrays[1][0])


var myArr = [18, 64, 99];
myArr[1] = 69;
console.log(myArr)

// Using Push to manipulate array

myArr.push(["Happy", "joy"]);
myArr.push(1, 2, 3);
console.log(myArr);

// Using Pop to remove elements

myArr.pop();
console.log(myArr);

// Using Shift & unshift

myArr.shift();
myArr.unshift("Bola");
console.log(myArr);
