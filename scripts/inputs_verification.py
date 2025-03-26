import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Print Gradle Properties')
    parser.add_argument('--uploadAppDemo', type=str, choices=['true', 'false'], help='Upload app demo')
    parser.add_argument('--uploadSdk', type=str, choices=['true', 'false'], help='Upload sdk')
    parser.add_argument('--incrementVersion', type=str, choices=['true', 'false'], help='Increment version')

    args = parser.parse_args()
    uploadAppDemo = args.uploadAppDemo.lower() == 'true'
    uploadSdk = args.uploadSdk.lower() == 'true'
    incrementVersion = args.incrementVersion.lower() == 'true'
    
    if not incrementVersion and not uploadAppDemo and not uploadSdk:
        print("Errore: Non è possibile NON incrementare la versione dell'app e non effettuare nemmeno un upload")
        sys.exit(1)
    
    if incrementVersion and not uploadAppDemo and not uploadSdk:
        print("Errore: Non è possibile incrementare la versione dell'app e non effettuare nemmeno un upload")
        sys.exit(1)

if __name__ == "__main__":
    main()