<script>
	var tomSmith=["Tom Smith","123 Main",120.50];
	tomSmith[3]="tsmith@123.com";
	document.write("1st Index", tomSmith[0],tomSmith[1],tomSmith[2],tomSmith[3],"<br/>");
	
	tomSmith.splice(2,1,"Pittsburg","PA");
	tomSmith.splice(4,1);
	
	document.write("Array: ",tomSmith.valueof(),"<br/>");
	document.write("Array: ",tomSmith.join(","),"<br/>");
	
	//Insert Delete Operation Similar to Stack
	tomSmith.pop();
	tomSmith.push("55-12332232");

	//TO delete first items
	tomSmith.shift();

	//To add the first 
	tomSmith.unshift("Tom Smith");

	//To Sort it in Alphabetical Ordering
	tomSmith.sort();
	
	//To Print the elements of the array
	for (i=1;i<tomSmith.length;i++){
		document.write(tomSmith[i],"<br/>");
	}
	
	//To Delete
	delete tomSmith[3];
	
	var numbers=[4,3,9,1,20,43];
	
	//Ascending Sort
	numbers.sort(function(x,y){ return x-y});
	document.write(numbers,"<br/>");
	
	//Descinding Sort
	numbers.sort(function(x,y){ return y-x});
	document.write("Num Array:",numbers.toString(),"<br/>");
	
	//Concat two or more arrays.
	var combinedArray=numbers.concat(tomSmith);
	

</script>