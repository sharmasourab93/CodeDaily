//Function to check
function inArray(arrayToCheck,value){
	for(i=0;i<arrayToCheck.length;i++){
		if(arrayToCheck[i]===value){
			return true;
		}
	}
	return false;
}
var randArray=[1,2,3,4,5,6];
document.write("In Array:",inArray(randArray,4),"<br/>");

//Scope of a function
	function times2(num){
		var var2=2;
		return num*var2;
	}
	document.write("var2",var2,"<br/>");
//end scope

function times3(num){
		return num*3;
	}
function multiply(func,num){
		return func(num);
}
document.write("2*15=",multiply(times2,15)+"<br/>");
document.write("3*15=",multiply(times3,15)+"<br/>");

//Function Expression
var triple=function(num){
		return num*3;
	}
document.write("3*45= ",triple(45)+"<br/>");
	
//Passing Multiple Arguments
function getSum(){
	var sum=0;
	for(i=0;i<arguments.length;i++){
		sum+=arguments[i];
	}
	return sum;
}
document.write(getSum(1,2,3,4,5),"<br/>");

function times2(theArray){
	var newArray=[];
	for(i=0;i<theArray.length;i++){
		newArray.push(theArray[i]*2);
	}
	return newArray;
}
document.write(" ",times2([1,2,3,4,5]).toString(),"<br/>");

//Recursive FUnction 
function fact(num){
	if (num<=1){
	   return 1;
	}
	return num*fact(num-1);
}
document.write("Factorial of 4= ",fact(4),"<br/>");