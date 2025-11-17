import os
import time
import argparse
import requests
import readline
#crear funcion para descubrir subdominios
version = "1.0.2"

def function_lines(index):
    try:
        os.system(f"wc -l {index}");
    except OSError as error:
        print(error);

def function_println_http(address, dicc, ignorethem):
    try:
        res = requests.get(f"{address}{dicc}");
        if res.status_code != ignorethem and res.status_code == 200:
            #print_at(1361, 94, "[try] {}{}".format(address, dicc))
            msg = f"Report: Code({res.status_code}) ok {address}{dicc}"
            print(msg)
            return res.status_code
    except OSError as error:    
        print(error);
def print_starting(target, modo, wordlist, ignore, cantidad):
    try:
        os.system("clear");
        print("####################################################")
        print("Starting LoopFuzz 1.0.1 (https://loopfuzz.github.io)")
        print("Target: {}".format(target));
        print("Wordlist: {}".format(wordlist));
        print("Attempts: {}".format(cantidad))
        print("Mode: {}".format(modo));
        print("Ignore: {}".format(ignore));
        print("####################################################")
    except OSError as error:
        print(error);


parse = argparse.ArgumentParser("LoopFuzz {}".format(version));
parse.add_argument("-m", "--mode", help="BFUZZ, DFUZZ");
parse.add_argument("-t", "--target", help="url");
parse.add_argument("-w", "--wordlist", help="wordlist example common.txt");
parse.add_argument("-i", "--ignore", type=int, help="statuscode ignore");
args = parse.parse_args();

if args.mode == "bfuzz":
    if args.target:
        if args.wordlist:
            if args.ignore:
                file = open(f"{args.wordlist}", "r");
                more = file.readlines();
                print_starting(args.target, args.mode, args.wordlist, args.ignore, len(more));
                for x in more:
                    local = x.strip();
                    #print(term.move_xy(10, 10) + f"{args.target}{x}");
                    function_println_http(args.target, local, args.ignore);
                log = len(more)
                print(f"Wordlist completed, {log} requests were made");
