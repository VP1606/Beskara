# WSS Blueprint

## Commands
**Marked by "cmd"**

| Flag               	| Meaning                          	| Used By                                             	| Sub-Flags                               	|
|--------------------	|----------------------------------	|-----------------------------------------------------	|-----------------------------------------	|
| beskara_mlds       	| Machine live data stream         	| Beskara Machine (threaded zone controller)          	| Zone ID's as int dict_keys (same level) 	|
| beskara_mstat      	| Machine status (running or not)  	| Beskara Machine (thread launcher in sys controller) 	| 'running' as Bool (same level)          	|
| bclient_req_config 	| Requests contents of config.json 	| Beskara Client                                      	| -                                       	|
| bclient_set_config 	| Sets contents of config.json     	| Beskara Client                                      	| 'data' as json dict (in {})             	|