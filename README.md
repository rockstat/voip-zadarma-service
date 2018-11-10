# Zadarma VOIP service

In this example was used Zadarma VOIP service provider

## Guide

### Fetch code

Open Theia IDE terminal

```
cd my_images
git clone https://github.com/rockstat/voip-zadarma-service.git ztrack
```


### Configuration


#### Webhook

1. Configure Webhook at API section of member area to

```
https://YOURDOMAIN/ztrack/main/99
```

where `99` is an arbitary project identifier, `ztrack` is a service name, `main` method/event name

#### Storage

Create file in theia `config/custom/chwriter/zadarma.yml` with content. It create new table based on webhooks.
Restart CHWriter using dashboard.


```yml
---
clickhouse:
  destinations:
    ztrack/main: wh_ztrack

  tables:
    wh_ztrack:
      ztrack_extra.key: Array(String)
      ztrack_extra.value: Array(String)
      ztrack_uid: UInt64
      ztrack_sess_no: UInt16
      event: String
      call_start: DateTime
      pbx_call_id: String
      caller_id: String
      called_did: String
      duration: String
      disposition: String
      status_code: String
      is_recorded: String
      _options:
        extend: webhooks
```

Now you cat try to call.

### Run

```
cd ztrack
make start-dev
```

## License

```
Copyright 2018 Dmitry Rodin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
