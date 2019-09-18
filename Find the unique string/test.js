/*There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings*/
function findUniq(arr) {
  narr = arr.sort(function(a, b){
  return a.length - b.length;
});
  function contains(where, what){
    for(var i=0; i<what.length; i++){
        if(where.indexOf(what[i]) == -1) return false;
    }
    return true;
  }
  var ls = narr[arr.length-1];
  if(arr[0].length == ls.length && ls.length==1){
	  narr.sort();
	  if(narr[0] === narr[1]){
		  return narr[narr.length-1];
	  }else{
		  return narr[0];
	  }
  }
  
  if(narr[0].length == ls.length && !contains(ls.toUpperCase(), narr[0].toUpperCase()))
      {
        return ls;
      }
  
    for (var s in narr){
      if(!contains(ls.toUpperCase(), narr[s].toUpperCase()))
      {
        return narr[s];
      }
    }
    return ls;
}