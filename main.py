from aiohttp import web
import requests
import asyncio
import argparse


class server():
    def __init__(self, name):
        print(213)
        self.name = name
    def sit(self):
        print(self.name)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--usd')
