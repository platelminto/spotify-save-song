Easily save songs currently playing from Spotify to your library using a hotkey or key combo. (Currently only f8, will make this easily editable). Has to be run as sudo on macOS to be able to access raw keyboard inputs.

Make a keys.txt file in the src/ directory, with client_id & secret obtained from making an API application [here](https://beta.developer.spotify.com/dashboard/applications), putting them on the first and second line of the file, respectively. In the application dashboard, go to 'Edit Settings', and set the redirect URI to 'http://localhost:8888/callback'

On first run, a browser window should open and the url should point to localhost, with a single `code` paramater: copy its value into the commandline (which should be awaiting input). From then on, nothing other than starting up the script should be required by the user.

This branch also saves the songs to a monthly playlist (for example, 'March 2018'), and creates one if there isn't one available.
