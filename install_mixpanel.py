import os
import subprocess
import yaml

def install_mixpanel_sdk():
    # Ask for folder location
    folder_path = input("Enter the folder location of your Flutter app codebase (press Enter for current folder): ")
    if not folder_path:
        folder_path = os.getcwd()

    # Find pubspec.yaml
    pubspec_path = os.path.join(folder_path, 'pubspec.yaml')
    if not os.path.exists(pubspec_path):
        print("Error: pubspec.yaml not found in the specified folder.")
        return

    # Read pubspec.yaml
    with open(pubspec_path, 'r') as file:
        pubspec = yaml.safe_load(file)

    # Check if Mixpanel is already installed
    if 'dependencies' in pubspec and 'mixpanel_flutter' in pubspec['dependencies']:
        print("Mixpanel is already installed in this project.")
        return

    # Add Mixpanel SDK to dependencies
    if 'dependencies' not in pubspec:
        pubspec['dependencies'] = {}
    pubspec['dependencies']['mixpanel_flutter'] = '^2.3.1'

    # Write updated pubspec.yaml
    with open(pubspec_path, 'w') as file:
        yaml.dump(pubspec, file, default_flow_style=False)

    # Run flutter pub get
    try:
        subprocess.run(['flutter', 'pub', 'get'], cwd=folder_path, check=True)
        print("Mixpanel SDK is installed correctly and now ready for implementation.")
        print("For next steps, please refer to: https://docs.mixpanel.com/docs/tracking-methods/sdks/flutter#getting-started")
    except subprocess.CalledProcessError:
        print("Error: Failed to run 'flutter pub get'. Please make sure Flutter is installed and in your PATH.")

if __name__ == "__main__":
    install_mixpanel_sdk()
