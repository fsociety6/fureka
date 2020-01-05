# Plant Pest and Disease Scrapper
A Scrapper built with Scrapy for downloading information of Plant Pest and Disease Details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need (python3.7,npm and pip) install on your machine



### Installing

A step by step series of examples that tell you how to get a development env running
1.Download http-server from npm and pipenv from pip

```
npm install -g http-server
pip install -g pipenv

```
2.Clone the Repository and install dependencies and setup the envoirmnent


```
git clone https://github.com/fsociety6/fureka.git 
cd fureka
pipenv install
pipenv shell
```
3.start the server on one shell
```
cd fureka/pestscrapper/pestscrapper/spiders
http-server
```
4.start crawler on other shell
```
cd fureka/pestscrapper
scrapy crawl -o pests.json
```
you can see output in pests.json at /fureka/pestscrapper

## Built With

* [scrapy](https://scrapy.org/)- An open source and collaborative framework for extracting the data you need from websites.
* [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) - Python Dev Workflow for Humans
* [http-server](https://www.npmjs.com/package/http-server) -http-server is a simple, zero-configuration command-line http server.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details




