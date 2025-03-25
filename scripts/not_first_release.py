import argparse
from gradle_utils import read_gradle_properties
from gradle_utils import update_gradle_properties

def main():
    parser = argparse.ArgumentParser(description='Print Gradle Properties')
    parser.add_argument('--gradleFileName', type=str, help='The gradle file name')
    
    args = parser.parse_args()

    gradle_file_name = args.gradleFileName
    properties = read_gradle_properties(gradle_file_name)
    
    properties['IS_FIRST_RELEASE'] = 'false'
    properties['IS_FIRST_MAVEN_RELEASE'] = 'false'
    
    update_gradle_properties(gradle_file_name, properties)



if __name__ == "__main__":
    main()