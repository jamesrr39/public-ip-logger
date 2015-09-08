# public IP logger

Script to log your public IP address to a file, in order that you know what it is/they are to whitelist IP addresses on remote resources.

It logs to `./logs/ip_address.log` and logs in the format:

> {datetime}|{timestamp}|{public ip address}|{Network SSID (None if not applicable)}

## Licence

MIT, and it uses the dyndns checkip tool, so abide by [their policies](https://help.dyn.com/remote-access-api/checkip-tool/)

## Install

    pip install -r requirements.txt

## Run

    python log-ip.py
