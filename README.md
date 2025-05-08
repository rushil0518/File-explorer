# 🔍 CLI-based File Explorer with Process Management  

A powerful **command-line interface (CLI) application** for navigating, managing files and directories, and monitoring system processes seamlessly. This project is designed to enhance user productivity by combining **file management** with **process control** directly from the terminal.

---

## 🚀 **Features**
- **File Management:**  
  - List, create, rename, open, and delete files and directories.  
  - Navigate through directories with simple commands.  

- **Memory Management:**  
  - Display directory sizes (`ls -s` style).  
  - Monitor disk usage (`disk` command) for total, used, and free space.  

- **Process Management:**  
  - List all running processes with PID, Name, CPU, and Memory usage.  
  - Monitor specific process performance in real-time.  
  - Kill processes by PID.  
  - Visualize the parent-child relationship of running processes.  

---

## 🛠️ **Requirements**
- Python 3.10 or later  
- Required libraries:  
    ```sh
    pip install psutil
    ```

---

## 📦 **Installation**
1. **Clone the repository:**  
    ```sh
    git clone https://github.com/your-username/cli-file-explorer.git
    cd cli-file-explorer
    ```

2. **Install dependencies:**  
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**  
    ```sh
    python explorer.py
    ```

---

## 🔗 **Available Commands**
| Command            | Description                                                    |
|---------------------|----------------------------------------------------------------|
| `ls`               | List contents of the current directory                         |
| `ls -s`            | List contents with size information                            |
| `cd <dir>`         | Change the current directory                                   |
| `pwd`              | Print the current directory path                               |
| `mkdir <dir>`      | Create a new directory                                         |
| `rmdir <dir>`      | Remove an empty directory                                      |
| `touch <file>`     | Create a new empty file                                        |
| `open <file>`      | Display contents of a file                                     |
| `rm <file>`        | Delete a specified file                                        |
| `rn <old> <new>`   | Rename a file                                                  |
| `cd ..`            | Navigate to the parent directory                               |
| `disk`             | Display disk usage statistics                                  |
| `ps`               | List all running processes with PID, Name, CPU, and Memory     |
| `kill <pid>`       | Terminate a process by its PID                                 |
| `watch <pid>`      | Monitor CPU and memory usage of a specific process in real-time|
| `pstree`           | Display the parent-child process tree                         |
| `help`             | Show the list of available commands                           |
| `exit` or `quit`   | Exit the application                                           |

---

## 💡 **Usage Examples**
```sh
file-explorer> ls -s
Total Directory Size: 5.2MB
Permissions Size       Modified            Name
------------------------------------------------------------
drwxr-xr-x  4.5KB     2025-05-08 10:23    folder1
-rw-r--r--  1.2MB     2025-05-08 10:23    file1.txt
