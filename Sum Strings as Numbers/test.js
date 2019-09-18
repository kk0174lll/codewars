/*Given the string representations of two integers, return the string representation of the sum of those integers.
For example:
sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".*/
function main() {
	var r = sumStrings('00103', '08567')
	console.log(r);
	console.log('8670');
}

function sumStrings(a, b) {
	console.log('a= ' + a + ' b=' + b);
	function prepare(str) {
		while (str.startsWith('0')) {
			str = str.slice(1);
		}
		return str;
	}
	a = prepare(a);
	b = prepare(b);
	var max;
	var min;
	if (a.length > b.length) {
		max = a;
		min = b;
	} else {
		max = b;
		min = a;
	}
	max = max.split("").reverse().map(Number);
	min = min.split("").reverse().map(Number);
	result = [];
	var n = 0;
	for (var i = 0; i < max.length; i++) {
		var sum = max[i] + n;
		if (i < min.length) {
			sum = sum + min[i];
		}
		if (sum >= 10) {
			result.push(sum % 10);
			n = Math.floor(sum / 10)
		} else {
			result.push(sum);
			n = 0;
		}
	}
	if (n > 0) {
		result.push(n);
	}

	return result.reverse().join("");
}

