/*
This is a simple string decoding algorithm. The idea is to take a string of of characters and decode it into an array. Each character is a single element in the result unless a backslash followed by a positive number is encountered.

When a backslash followed by a positive number is found, the number indicates how many of the next characters are grouped together as one element.

Example:

"abc\5defghi\2jkl" => ["a", "b", "c", "defgh", "i", "jk", "l"]
If the number is larger than the count of remaining character treat it as reading the remaining characters.

If you are reading characters, and you find an escape inside a string, they should be tallied into the string:

"\5ab\3cde" => ["ab\3c", "d", "e"]
 */

function main() {
	console.log(decode("abc"));
}


function decode(str) {
	if (!str || str.length == 0) {
		return [];
	}
	function isNumber(char) {
		return /\d/.test(char);
	}
	var result = [];
	var ricently = str[0]
	var count = 0;
	var countFlag = false;
	var tempStr = '';
	if (ricently !== "\\") {
		result.push(ricently);
	}
	for (var i = 1; i < str.length; i++) {
		var c = str[i];
		if (count > 0) {
			if (countFlag && isNumber(c)) {
				count = count * 10 + Number.parseInt(c);
			} else {
				countFlag = false;
				tempStr = tempStr + c;
				count--;
			}
		} else {
			if (tempStr.length > 0) {
				result.push(tempStr);
				tempStr = "";
			}
			if (c !== "\\") {
				if (ricently === "\\" && isNumber(c)) {
					count = Number.parseInt(c);
					countFlag = true;
				} else {
					result.push(c);
				}
			}
		}
		ricently = c;
	}
	if (tempStr.length > 0) {
		result.push(tempStr);
	}
	return result;
}