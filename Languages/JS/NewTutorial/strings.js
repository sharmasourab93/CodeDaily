var firstName = "Alan";
var lastName =  "Turing";

var myFirstName = "Sourab";
var myLastName = "Sharma";

var myStr = "I am a \"Double quoted\" string inside \"double quotes\"";
console.log(myStr)

// Escape Sequences
/*****
CODE OUTPUT
\' single quote
\" double quote
\\ backslash
\n newline
\r carriage return
\t tab
\b backspace
\f form feed

******/

var myString = "FirstLine\n\t\\SecondLine\nThirdLine"

/* Concatenating Strings */

var outStr = "I come first. " + "I come second. ";
var myAStr =  "This is the start. "
console.log(myAStr)

// Appending Strings
myAStr += "This is the end."
console.log(myAStr)


//Constructing Strings

var myName = "Beau";
var myNStr = "My name is " + myName + " and I am well!";
console.log(myNStr)

// Find length of the string
var fname = "Ada";
var firstNameLength = firstName.length;

var lastNameLength = 0;
var lastName = "LoveLace";

lastNameLength = lastName.length;
console.log(lastNameLength)

// Bracket Notation

var f1Name = "Ada";

firstLetterOfFirstName = f1Name[0]; // A

firstLetterOfLastName = "";
var lastName = "Lovelace";

firstLetterOfLastName = lastName[0];
console.log (firstLetterOfLastName) // L


// Strings are immutable
var myIStr = "JelloWorld";
//myIStr[0]="H"; //Fix me

// Indexing using Brackets
var secondLetterOfFirstName = firstName[1];
var lastLetterOfFirstName = firstName[firstName.length - 1]
var rangeOfFirstName = firstName[firstName.length -2];



