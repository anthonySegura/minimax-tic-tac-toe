const pyshell = require('python-shell');

let board = [
	['-', '-', '-'],
	['-', '-', '-'],
	['-', '-', '-']
]
let GAME_OVER = false;
let WAITING = false;

function move(position) {
	if (!WAITING) {
		if (GAME_OVER) {
			clear();
			return;
		}
		let pos = position.split('-');
		if (!positionIsValid(pos)) return;
		board[pos[0]][pos[1]] = 'O';
		document.getElementById(position).className = 'o';
		let options = { args: [boardToString()] };
		WAITING = true;
		pyshell.PythonShell.run('./python/game_api.py', options, (err, result) => {
			if (err) {
				console.error(err);
			}
			else {
				AI_move(result);
			}
		});
	}
}

function positionIsValid(pos) {
	return board[pos[0]][pos[1]] == '-';
}

function AI_move(result) {
	let position = eval(result[0]);
	if (position.length == 0) {
		GAME_OVER = true;
		WAITING = false;
		return;
	}
	board[position[0]][position[1]] = 'X';
	let pos = String(position[0]) + '-' + String(position[1]);
	document.getElementById(pos).className = 'x';
	if (result[1] == 'game_over') {
		let winner_pos = eval(result[2]);
		showWinners(winner_pos);
		GAME_OVER = true;
	}
	WAITING = false;
}

function boardToString() {
	str = "";
	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[i].length; j++) {
			str += board[i][j] + (j == 2 ? '' : ',');
		}
		str += (i == 2 ? '' : '/');
	}
	return str
}

function showWinners(winners) {
	winners.map(pos => {
		let id = String(pos[0]) + '-' + String(pos[1]);
		document.getElementById(id).className += ' blink';
	});
}

function clear() {
	board = board.map(_ => _.map(_ => '-'));
	let squares = document.getElementsByClassName('square');
	for (let idx in squares) {
		if (squares[idx].lastElementChild)
			squares[idx].lastElementChild.className = '';
	}
	GAME_OVER = false;
}

