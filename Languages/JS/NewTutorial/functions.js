function ourFunction(){
    console.log("Hello World");
}

ourFunction(); // Outputs  Hello World

function ourFunctionWithArgs(a, b){
    console.log(a - b);
}

ourFunctionWithArgs(10, 20); // Outputs -10

// Global Scope and Functions

var myGlobal = 10;

function fun1() {
    // Variables declared without var
    // becomes global automatically
    oopsGlobal = 5;
}

function fun2(){
    var output = " ";
    if (typeof myGlobal != "undefined"){
        output += "myGlobal: " + myGlobal;
    }

    if (typeof oopsGlobal != "undefined"){
        output += "oopsGlobal: "+ oopsGlobal;
    }
    console.log(output);
}

fun1();
fun2();