// partition the items array so that all values for which pred returns true are
// at the end, returning the index of the first true value
function partitionOn(pred, items) {
	var left = [];
	var right = [];
	for (var i in items){
		if (pred(items[i])){
			right.push(items[i]);
		}else{
			left.push(items[i]);
		}
	}	
	function forEach(element){		
		items.shift()
		items.push(element);
	}
	left.forEach(forEach);
	right.forEach(forEach);	
	return left.length;
}