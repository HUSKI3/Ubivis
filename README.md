<br/>
<p align="center">
  <h3 align="center">Ubivis</h3>

  <p align="center">
    Making shared libraries easily accessible in Python 
    <br/>
    <br/>
    <a href="https://github.com/HUSKI3/Ubivis"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/HUSKI3/Ubivis">View Demo</a>
    .
    <a href="https://github.com/HUSKI3/Ubivis/issues">Report Bug</a>
    .
    <a href="https://github.com/HUSKI3/Ubivis/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/HUSKI3/Ubivis?color=dark-green) ![Forks](https://img.shields.io/github/forks/HUSKI3/Ubivis?style=social) ![Stargazers](https://img.shields.io/github/stars/HUSKI3/Ubivis?style=social) ![Issues](https://img.shields.io/github/issues/HUSKI3/Ubivis) ![License](https://img.shields.io/github/license/HUSKI3/Ubivis) 

## About The Project

![Screen Shot](images/screenshot.png)

This project was created to simplify the use of Rust and VLang libraries internally at TecTone23, but can also be used for your own projects.

It's currently able to:
- Vlang
-- Build your source
-- Compile it into a shared object
-- Import the library into your project
- Rust
-- Import the library into your project

## Built With

- Python!

## Getting Started

You can install and set up ubivis by using poetry

### Installation

1. Create a new project
1.1 Manually
```sh
poetry init
poetry add ubivis
touch main.py
mkdir built
```
1.2 Using Ubivis
```sh
ubivis new # Experimental
```
2. Make a source file in another language
```sh
echo "\
[export: 'add']\
fn add(ctext &char) &char {\
mut s := unsafe { cstring_to_vstring(ctext) }\
return s.str\
}" >> src/v/example.v
```

3. Include it in your Python project
```python
from ubivis import ici, CFunc, Types
from ubivis.languages import Vlang

vlib = ici(Vlang("src/v/example.v", auto_construct=True)).new()
```

## Usage

Declaring the function
```python
@CFunc(
    (Types.CharPtr,),
    Types.CharPtr,
    test.lib.add
)
def add(msg: str):
    return vlib.add(msg.encode()).decode()

print(vadd("VLang!"))
```

Congratz! it's done!

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/HUSKI3/Ubivis/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/HUSKI3/Ubivis/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Artur Z** - *Comp Sci Student* - [Artur Z](https://github.com/HUSKI3/) - *Made Ubivis*

## Acknowledgements

* []()
* []()
* [ImgShields](https://shields.io/)
