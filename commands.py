import os
from utils import format_permissions, format_size
from datetime import datetime
import shutil;
import psutil;

def list_dir():
        try:
            for item in os.listdir():
                stats = os.stat(item)
                perms = format_permissions(stats.st_mode)
                size = format_size(stats.st_size)
                modified = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
                print(f"{perms} {size:>8} {modified} {item}")
        except Exception as e:
            print (f"Error listing directory: {e}")

def change_dir(args):
        if not args:
            print("provide directory name")
            return
        try:
            os.chdir(args[0])
        except Exception as e:
            print(f"Error: {e}")

def make_dir(args):
        if not args:
            print("provide directory name")
            return
        try:
            os.mkdir(args[0])
        except Exception as e:
            print(f"Error: {e}")

def remove_dir(args):
        if not args:
            print("provide directory name")
            return
        try:
            os.rmdir(args[0])
        except Exception as e:
            print(f"Error: {e}")

def open_file(args):
        if not args:
            print("provide file name")
            return
        try:
            with open(args[0],'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Error: {e}")   
        
def create_file(args):
        if not args:
            print("provide file name")
            return
        try:
            open(args[0],'a').close()
        except Exception as e:
            print(f"Error: {e}")

def delete_file(args):
        if not args:
            print("provide file name")
            return
        try:
            os.remove(args[0])
        except Exception as e:
            print(f"Error: {e}")
    
def rename_file(args):
        if len(args) != 2:
            print ("please check the format")
            return
        try:
            os.rename(args[0],args[1])
        except Exception as e:
            print(f"Error: {e}")
def go_up_directory():
        try:
           os.chdir("..")
        except Exception as e:
            print(f"Error: {e}")

def get_directory_size(start_path='.'):
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except FileNotFoundError:
                continue
    return total_size

def list_dir_with_sizes():
    try:
        total_size = get_directory_size()
        print(f"Total Directory Size: {format_size(total_size)}")
        print(f"{'Permissions':<10} {'Size':>10} {'Modified':<20} {'Name'}")
        print("-" * 60)
        for item in os.listdir():
            stats = os.stat(item)
            perms = format_permissions(stats.st_mode)
            size = format_size(stats.st_size) if os.path.isfile(item) else format_size(get_directory_size(item))
            modified = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
            print(f"{perms:<10} {size:>10} {modified:<20} {item}")
    except Exception as e:
        print(f"Error listing directory with sizes: {e}")

def disk_usage():
    try:
        total, used, free = shutil.disk_usage(os.getcwd())
        print(f"{'Disk Usage Information':^50}")
        print("-" * 50)
        print(f"{'Total Space:':<20} {format_size(total):>20}")
        print(f"{'Used Space:':<20} {format_size(used):>20}")
        print(f"{'Free Space:':<20} {format_size(free):>20}")
        print("-" * 50)
    except Exception as e:
        print(f"Error retrieving disk usage: {e}")

def list_processes():
    print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%':<10}")
    print("-" * 60)
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        print(f"{process.info['pid']:<10} {process.info['name']:<25} "
              f"{process.info['cpu_percent']:<10.2f} {process.info['memory_percent']:<10.2f}")
        
def kill_process(args):
    if not args:
        print("Please provide a PID to kill.")
        return
    try:
        pid = int(args[0])
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=5)
        print(f"Process {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid}")
    except Exception as e:
        print(f"Error terminating process: {e}")

def watch_process(args):
    if not args:
        print("Please provide a PID to monitor.")
        return
    try:
        pid = int(args[0])
        process = psutil.Process(pid)
        print(f"Monitoring process {pid} (Press Ctrl+C to stop)...")
        print(f"{'CPU%':<10} {'Memory%':<10}")
        print("-" * 20)
        while True:
            cpu = process.cpu_percent(interval=1)
            mem = process.memory_percent()
            print(f"{cpu:<10.2f} {mem:<10.2f}")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid}")
    except KeyboardInterrupt:
        print("\nStopped monitoring.")
    except Exception as e:
        print(f"Error monitoring process: {e}")

def display_process_tree():
    def print_tree(pid, indent=""):
        try:
            proc = psutil.Process(pid)
            print(f"{indent}-[{pid}] {proc.name()}")
            children = proc.children()
            for child in children:
                print_tree(child.pid, indent + "   ")
        except psutil.NoSuchProcess:
            pass

    print("[ROOT PROCESS TREE]")
    for proc in psutil.process_iter(['pid', 'ppid']):
        if proc.info['ppid'] == 0:  # Root processes
            print_tree(proc.info['pid'])

def print_help():
        print("""Available Commands:
    ls                  - List contents of current directory
    cd <dir>            - Change current directory
    pwd                 - Print current directory
    mkdir <dir>         - Create a directory
    rmdir <dir>         - Remove an empty directory
    touch <file>        - Create a new empty file
    open <file>         - Display contents of a file
    rm <file>           - Delete a file
    rn <old> <new>      - Rename file
    cd ..               - Go to the parent directory
    ls -s               - List directory with size
    disk                - Display the disk usage statistics
    ps                  - List all running processes
    kill <pid>          - Kill a process by its PID
    watch <pid>         - Monitor CPU and memory usage of a process
    pstree              - Display the process tree
    help                - Show this help message
    exit or quit        - Exit the file explorer
    """)
    
def handle_command(command):
    parts = command.split()
    if not parts:
        return
    cmd = parts[0]
    args = parts[1:]

    if (cmd == "ls"):
        list_dir()
    elif cmd == "ls -s":
        list_dir_with_sizes()
    elif (cmd == "cd"):
        change_dir(args)
    elif (cmd == "pwd"):
        print(os.getcwd())
    elif (cmd == "mkdir"):
        make_dir(args)
    elif (cmd == "rmdir"):
        remove_dir(args)
    elif (cmd == "open"):
        open_file(args)
    elif (cmd == "touch"):
        create_file(args)
    elif (cmd == "rm"):
        delete_file(args)
    elif (cmd == "rn"):
        rename_file(args)
    elif (cmd == "cd .."):
         go_up_directory()
    elif cmd == "disk":
         disk_usage()
    elif cmd == "ps":
        list_processes()
    elif cmd == "kill":
        kill_process(args)
    elif cmd == "watch":
        watch_process(args)
    elif cmd == "pstree":
        display_process_tree()
    elif (cmd == "help"):
        print_help()
    else:
        print(f"Unknown command: {cmd}")
    
