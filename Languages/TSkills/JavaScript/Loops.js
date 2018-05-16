<script>

	var i=1;
	//While Loop 
	while(i<=10){
		document.write(i+"<br/>");
		i++;
	}
	
	//Do While Loop
	do{
		var guess =prompt("Enter a number under 15");
		
	}while(guess!=15);
	
	//For Loop with Break & Continue
	for(j=0;j<=10;j++){
		if((j%2==0)){
			continue;
		}
		if(j===7){
			break;
		}
		document.write(j,"<br/>");
	}
	
	
	var customer={name:"Bob thomas",addres:"123 Main", balance:50.50};
	//For Each Loop
	for(k in customer){
		document.write(customer[k]+"<br/>")
	}
</script>