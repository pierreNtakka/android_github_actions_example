import os
import argparse
from gradle_utils import read_gradle_properties
from gradle_utils import update_gradle_properties

def main():
    parser = argparse.ArgumentParser(description='Print Gradle Properties')
    parser.add_argument('--gradleFileName', type=str, help='The gradle file name')
    args = parser.parse_args()

    gradle_file_name = args.gradleFileName
    properties = read_gradle_properties(gradle_file_name)
        
    isFirstRelease = properties.get('IS_FIRST_RELEASE', 'false') == 'true'
    isFirstMavenRelease = properties.get('IS_FIRST_MAVEN_RELEASE', 'false')== 'true'
    releaseVersionName = properties.get('RELEASE_VERSION_NAME', '0.0.0')
    appDemoVersionCode = int(properties.get('APP_DEMO_VERSION_CODE', '0'))
    buildMavenSdkVersion = properties.get('BUILD_MAVEN_SDK_VERSION', '0.0.0')

    if not isFirstRelease:
        newAppDemoVersionCode = appDemoVersionCode + 1
        properties['APP_DEMO_VERSION_CODE'] = str(newAppDemoVersionCode)
        appDemoVersionCode = newAppDemoVersionCode
        print(f"Nuovo APP_DEMO_VERSION_CODE: {appDemoVersionCode}")

    if not isFirstMavenRelease:
        prefix = '.'.join(buildMavenSdkVersion.split('.')[:-1])
        lastNumber = int(buildMavenSdkVersion.split('.')[-1])
        newLastNumber = lastNumber + 1
        newBuildMavenSdkVersion = f"{prefix}.{newLastNumber}"
        properties['BUILD_MAVEN_SDK_VERSION'] = newBuildMavenSdkVersion
        buildMavenSdkVersion = newBuildMavenSdkVersion
        print(f"Nuovo BUILD_MAVEN_SDK_VERSION: {buildMavenSdkVersion}")

    update_gradle_properties(gradle_file_name, properties)

    commit_message=f"chore: Update app versionCode to: {appDemoVersionCode} and versionName: {releaseVersionName} and maven version {buildMavenSdkVersion}"
    
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as output_file:
        output_file.write(f"commit_message={commit_message}\n")

if __name__ == "__main__":
    main()