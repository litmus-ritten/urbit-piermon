# urbit-piermon
Simple logger for Urbit pier size, with systemd timer template.

## Syntax

`piermon.py -i [PATH TO PIER] -o [PATH TO OUTPUT CSV]`

## systemd service

Edit the fields in the `.timer` and `.service` files, install the service using `systemd enable` and `systemd start`.
