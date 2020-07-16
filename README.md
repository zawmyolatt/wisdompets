<h3 align="center">Django Application for Pets</h3>

## Setup
- Install Python3 and Virtual Env in your Machine

## Installation
- Download Pets App
```
git clone https://github.com/zawmyolatt/wisdompets
cd wisdompets/
```
- Install latest django and it's requirement
```
pip3 install --no-cache-dir -r ./requirements.txt
```
- Migrating data
```
cd wisdompets/ #no need to run if already in this folder
python3 manage.py migrate
python3 manage.py createsuperuser #create user super for you login
```

## Todo
- Unit Testing
- CI/CD Setup

## License

This Pets App is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).