function main() {
	testMap(new Node(1, new Node(2, new Node(3))), x => x * 2, new Node(2, new Node(4, new Node(6))));
	console.log('8670');
}
function Node(data, next) {

	return {
		data: data,
		next: next
	}

}
function testMap(head, f, expected) {
	console.log(listToArray(map(head, f)));
	console.log(listToArray(expected));
};

function listToArray(head) {
	return !head ? [] : [head.data].concat(listToArray(head.next));
};

function map(head, f) {
	if (!head) {
		return null;
	}
	function Node(data, next) {
		return {
			data: data,
			next: next
		}

	}
	var current = head;
	var newList = Node('', null);
	var newCurrent = newList
	while (current.next) {
		newCurrent.data = f(current.data);
		current = current.next
		newCurrent.next = Node('', null);
		newCurrent = newCurrent.next
	}
	newCurrent.data = f(current.data);
	return newList;
}