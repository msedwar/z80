# Z80 Homebrew

<table>
  <tr><td>Author:</td><td>Matthew Edwards</td></tr>
  <tr><td>License:</td><td><a href="https://opensource.org/licenses/MIT">MIT License</a></td></tr>
  <tr><td>Created:</td><td>November 24, 2021</td></tr>
</table>

A Zilog Z80 homebrew project by Matthew Edwards.

## Tooling Dependencies

- Python <= 3.9 [ [Website](https://www.python.org/), [Installation](https://www.python.org/downloads/), [License](https://docs.python.org/3/license.html) ]
- CMake [ [Website](https://cmake.org/), [Installation](https://cmake.org/download/), [License](https://cmake.org/licensing/) ]
- Pyre [ [Website](https://github.com/facebook/pyre-check), [Installation](https://pyre-check.org/docs/installation/), [License](https://github.com/facebook/pyre-check/blob/main/LICENSE) ]
- Black [ [GitHub](https://github.com/psf/black), [Installation](https://github.com/psf/black#installation-and-usage), [License](https://github.com/psf/black/blob/main/LICENSE) ]
- Arduino CLI [ [GitHub](https://github.com/arduino/arduino-cli), [Installation](https://arduino.github.io/arduino-cli/0.20/installation/), [License](https://github.com/arduino/arduino-cli/blob/master/LICENSE.txt) ]
- vasm [ [Website](http://sun.hasenbraten.de/vasm/), [Installation](http://sun.hasenbraten.de/vasm/release/vasm.html), [License](http://sun.hasenbraten.de/vasm/release/vasm.html) ]

To check that dependencies are properly installed, run:
```
$ python3 scripts/check_dependencies.py
```

## Linting and Formatting
To lint project:
```
$ python3 scripts/lint.py
```

To check project Python typing:
```
$ pyre check
```
