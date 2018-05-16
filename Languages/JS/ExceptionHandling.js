<script>
//Exception Handling
var custArray=["Tom","Bob","Sally","Sue"];
var getCust=function(index){
	if(index>custArray.length){
		throw new RangeError("Index must be >=0 and <="+custArray.length);
	}else{
		return custArray[index];
	}
}
try{
	document.write("Customer: ",getCust(5),"<br/>");
}
catch(ex){
	if(ex instanceof RangeError){
		document.write(ex.message +" <br/>");
	}
}
</script>