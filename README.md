# LibreNMS integration pack

> Early development stage, use at your own risks for now.

## Installation

No special dependencies are required, just install the pack with 

``` bash
st2 pack install https://github.com/kedare/stackstorm-librenms.git
```

(Until this has been pushed to StackStorm Exchange)

Then you need to define in a `/opt/stackstorm/config/librenms.yaml` the proper variables

``` yaml
api_key: xxxxx
api_root: https://librenms.example.com/api/v0
```

## Sensors

You have sensors to trigger event when new entries are detected in `eventlog` and `alertlog`

## Actions

- `get_bgp_sessions` : Get BGP sessions matching criteria 
- `get_devices` : Get devices matching criteria (will also return more data depending of the search type, for example the port data for a search by ipv4/ipv6)
- `get_port`: Get data about a port
- `get_ip_arp`: Get ARP binding for a specific IP