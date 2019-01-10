const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
	window = new BrowserWindow({
		width: 625, height: 625, webPreferences: {
			devTools: false
		}
	});
	window.loadFile('index.html');
}

app.on('ready', createWindow);
app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') {
		app.quit()
	}
});






