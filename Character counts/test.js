/*
Character counts
The object is to count the number of occurances of a specified character (or set of characters) in a string.

Instructions
Complete the placeholder function characterCount.

it should return the number of times a single character appears in the string, or
if multiple characters are specified (either by providing an array or string of length 2 or more), it should return an array of character counts
see the unit tests provided for a more comprehensive definition
NOTE: The tests assume that if no arguments are provided to the function (i.e. ''.characterCount()), then the result is undefined
 */

function main() {
	console.log(''.characterCount('ado'));
}


String.prototype.characterCount = function (charsToCount) {
	if (!this.length || this.length == 0) {
		return undefined;
	}
	var result = [];
	var count;
	for (i = 0; i < charsToCount.length; i++) {
		var c = charsToCount[i];
		count = 0;
		for (j = 0; j < this.length; j++) {
			if (c == this[j]) {
				count++;
			}
		}
		result.push(count);
	}
	if (result.length == 1) {
		return result[0];
	} else {
		return result;
	}
};