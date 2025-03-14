# victronvenusclient

[![PyPI - Version](https://img.shields.io/pypi/v/victronvenusclient.svg)](https://pypi.org/project/victronvenusclient)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/victronvenusclient.svg)](https://pypi.org/project/victronvenusclient)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Introduction

VenusVictronClient is a an asynchronous library that uses MQTT to communicate with devices running Victron's Venus OS,
including the Victron CCGX, Cerbo GX and Ekrano GX.

The source code is available on [GitHub](https://github.com/JohansLab/victronvenusclient).

DISCLAIMER: This is a third-party library and not a product of Victron.

## Installation

```bash
pip install victronvenusclient
```


## Viewer

The package has a viewer application written using Tk that allows you to inspect the various metrics and devices. To 
run the viewer:

```bash
python3 -m victronvenusclient.utils.view_metrics
```

The viewer should also provide a good example of how to use the library.

## Limitations and Known Issues

- The current library has been tested with only a single configuration of a Victron installation. It might not have all the metrics
that are relevant to other installations - please see [Logging Issues] on how to get your installation supported.

- The library also only supports retrieving data, changing settings has not yet been implemented.


## Logging Issues

Issues can be logged on [GitHub](https://github.com/JohansLab/victronvenusclient/issues).

If you need support for your configuration or additional metrics you can dump the full mqtt structure from your device 
using the included dump_mqtt utility and attach the file to the issue:
```bash
# Dumps a full MQTT structure into fullvictrondump.txt
python3 -m victronvenusclient.utils.dump_mqtt > fullvictrondump.txt.

# If you need to specify the connection details command line help is available:
python3 -m victronvenusclient.utils.dump_mqtt --help
```



## License

`victronvenusclient` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
