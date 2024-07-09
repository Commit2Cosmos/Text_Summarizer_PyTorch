import json
import subprocess

def get_dependency_graph():
    result = subprocess.run(['pipenv', 'graph', '--json'], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("Failed to generate dependency graph")
    return json.loads(result.stdout)

def find_version_mismatches(dependency_graph):
    mismatches = []
    package_versions = {}

    def traverse_dependencies(dependencies, parent=None):
        for dependency in dependencies:
            package = dependency['package']
            package_name = package['package_name']
            installed_version = package['installed_version']
            
            if package_name in package_versions:
                if package_versions[package_name] != installed_version:
                    mismatches.append({
                        'package': package_name,
                        'installed_version': installed_version,
                        'conflicting_package': parent
                    })
            else:
                package_versions[package_name] = installed_version

            if 'dependencies' in package:
                traverse_dependencies(package['dependencies'], package_name)

    traverse_dependencies(dependency_graph)
    return mismatches

def main():
    dependency_graph = get_dependency_graph()
    mismatches = find_version_mismatches(dependency_graph)
    
    if mismatches:
        print("Version mismatches found:")
        for mismatch in mismatches:
            print(f"Package: {mismatch['package']}")
            print(f"  Installed version: {mismatch['installed_version']}")
            print(f"  Required version: {mismatch['required_version']}")
            print(f"  Conflicting package: {mismatch['conflicting_package']}")
            print()
    else:
        print("No version mismatches found.")

if __name__ == "__main__":
    main()
