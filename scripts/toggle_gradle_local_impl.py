import argparse
from gradle_utils import read_gradle_properties
from gradle_utils import update_gradle_properties

def main():
    parser = argparse.ArgumentParser(description='Print Gradle Properties')
    parser.add_argument('--gradleFileName', type=str, help='The gradle file name')
    parser.add_argument('--enable', type=bool, default='false', help='The debug option is enabled')

    args = parser.parse_args()

    gradle_file_name = args.gradleFileName
    properties = read_gradle_properties(gradle_file_name)
    enabled = args.enable == 'true'

    print(enabled)

    if(enabled):
        properties['ENABLE_LOCAL_IMPLEMENTATION'] = 'true'
    else:
        properties['ENABLE_LOCAL_IMPLEMENTATION'] = 'false'
       

    update_gradle_properties(gradle_file_name, properties)



if __name__ == "__main__":
    main()