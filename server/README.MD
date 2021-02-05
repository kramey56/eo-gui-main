### Furlough comments by Ken Ramey
The server codebase provides a Flask API for controlling the HiRACS focusing unit. The client code
makes API calls to the server, which has endpoints for the basic focusing unit commands. There are
commands for:
    home_focuser()
    center_focuser()
    zero_focuser()
    move_focuser()
    focuser_status()

Each command makes a network connection to the Payload computer and the HiRACS executable. The command
is translated to a Lynx Focuser command in the ASCII format defined by the Lynx command language. In most
commands the focusing unit responds with an exclamation point (!) followed by a single word acknowledgment.
The status command, at the Lynx level, responds with a list of status items and their values. The Flask API
converts the status results to a Python dictionary and stores it locally in order to respond to individual
status queries from the client.
