# BARCO ICMP MESSAGE READER

This is a monitoring tool for your ICMP`s. (BIMR)

## Installation

Be sure to have python installed. Works on Python 3.7
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BIMR.

```bash
pip install -r requirements.txt
```

## Usage

Run the functions induvidualy:

Trigger:
```python
import trigger

trigger.executeSomething() # Starts the collection of data
```
Web-Server:
```python
import trigger

trigger.app() # Starts the Web-Server
```

It`s not recommended to run them this way. The recommended way is:
-Dubble click on triggers.py
-Dubble click on main.py

Don`t close the console Windows. If so the services will stop.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)