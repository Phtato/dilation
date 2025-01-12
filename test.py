import os

def create_package(path):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write("# 初始化包\n")

create_package("another_project")