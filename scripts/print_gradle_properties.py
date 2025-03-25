import argparse
from gradle_utils import read_gradle_properties


def main():
    parser = argparse.ArgumentParser(description='Print Gradle Properties')
    parser.add_argument('--gradleFileName', type=str, help='The gradle file name')
    
    args = parser.parse_args()

    gradle_file_name = args.gradleFileName
   
    properties = read_gradle_properties(gradle_file_name)
    
    app_demo_version_code = properties.get('APP_DEMO_VERSION_CODE', 'N/A')
    release_version_name = properties.get('RELEASE_VERSION_NAME', 'N/A')
    build_maven_sdk_version = properties.get('BUILD_MAVEN_SDK_VERSION', 'N/A')
    enable_local_impl = properties.get('ENABLE_LOCAL_IMPLEMENTATION', 'N/A')
    
    print(f"APP_DEMO_VERSION_CODE={app_demo_version_code}")
    print(f"RELEASE_VERSION_NAME={release_version_name}")
    print(f"BUILD_MAVEN_SDK_VERSION={build_maven_sdk_version}")
    print(f"ENABLE_LOCAL_IMPLEMENTATION={enable_local_impl}")

if __name__ == "__main__":
    main()