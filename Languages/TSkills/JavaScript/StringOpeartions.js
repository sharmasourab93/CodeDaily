<script>
	
	var randStr="A long" + "string that "+"goes on and on.";
	document.write("String length:", randStr.length,"<br/>");
	document.write("Index for \"goes\": ", randStr.indexof("goes"),"<br/>");
	
	//Slice
	document.write(randStr.slice(19,23) +"<br/>");
	document.write(randStr.slice(19) +"<br/>");
	
	//Sub string
	var subrandstr=randStr.substr(19,4);
	document.write(subrandstr,"<br/>");
	
	//Replace
	var randstrarray=randStr.replace("goes","forever");
	document.write(randstrarray,"<br/>");

	randStr=randStr.trim();
	document.write(randStr);

	//Fonts
	var strToStyple="Random String";
	document.write("Big: ",strToStyple.big(),"<br/>");
	document.write("Bold: ",strToStyple.bold(),"<br/>");
	document.write("Italic: ",strToStyple.italic(),"<br/>");
	document.write("Sup: ",strToStyple.sup(),"<br/>");

</script>