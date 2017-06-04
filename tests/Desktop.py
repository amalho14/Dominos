def chrome():
    caps = {'browserName': "chrome"}
    caps['platform'] = "Windows 10"
    caps['version'] = "58.0"
    caps['idleTimeout']="10"
    return caps
def safari():
    caps = {'browserName': "safari"}
    caps['platform'] = "macOS 10.12"
    caps['version'] = "10.0"
    return caps