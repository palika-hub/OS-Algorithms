from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import os
from DSA import FirstFit,NextFit,BestFit,WorstFit
app = Flask(__name__)
CORS(app) 

class FileSystem:
    def __init__(self):
        self.files = {}
        self.current_directory = "/"

    def cd(self, path):
        if path == "..":
            # Move up one level in the directory structure
            path_parts = self.current_directory.split("/")
            if len(path_parts) > 1:
                self.current_directory = "/".join(path_parts[:-1])
                return "Directory changed to " + self.current_directory
            else:
                return "Already at the root directory."
        elif path in self.files and self.files[path]["is_folder"]:
            self.current_directory = path
            return "Directory changed to " + self.current_directory
        else:
            return "Directory not found"

    def ls(self):
        if self.current_directory in self.files and self.files[self.current_directory]["is_folder"]:
            return [item for item, data in self.files.items() if data["parent"] == self.current_directory]
        else:
            return "Invalid directory."

    def touch(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        if file_path not in self.files:
            self.files[file_path] = {"is_folder": False, "parent": self.current_directory, "data": ""}
            return "File created: " + file_path
        else:
            return "File already exists."

    def mkdir(self, dirname):
        dir_path = os.path.join(self.current_directory, dirname)
        if dir_path not in self.files:
            self.files[dir_path] = {"is_folder": True, "parent": self.current_directory}
            return "Directory created: " + dir_path
        else:
            return "Directory already exists."

    def write_file(self, filename, data):
        file_path = os.path.join(self.current_directory, filename)
        if file_path in self.files and not self.files[file_path]["is_folder"]:
            self.files[file_path]["data"] = data
            return "Data written to " + file_path
        else:
            return "File not found."

    def read_file(self, filename):
        file_path = os.path.join(self.current_directory, filename)
        if file_path in self.files and not self.files[file_path]["is_folder"]:
            return self.files[file_path]["data"]
        else:
            return "File not found."

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.current_process = None
        self.pid_counter = 1  # PID generator

    def create_process(self, process_name):
        if process_name not in self.processes:
            pid = self.pid_counter  # Get a unique PID
            self.pid_counter += 1
            self.processes[pid] = {"name": process_name, "threads": [], "parent": self.current_process}
            return "Process created: " + process_name + " (PID: " + str(pid) + ")"
        else:
            return "Process already exists."

    def create_thread(self, process_name, thread_name):
        if process_name in self.processes:
            threads = self.processes[process_name]["threads"]
            threads.append(thread_name)
            return "Thread created: " + thread_name
        else:
            return "Process not found."

    def set_current_process(self, process_name):
        for pid, process in self.processes.items():
            if process["name"] == process_name:
                self.current_process = pid
                return "Current process set to: " + process_name + " (PID: " + str(pid) + ")"
        return "Process not found."

    def fork(self, thread_name):
        if self.current_process:
            new_pid = self.pid_counter
            self.pid_counter += 1

            new_process = {
                "name": self.processes[self.current_process]["name"],
                "threads": [thread_name],
                "parent": self.current_process
            }

            self.processes[new_pid] = new_process

            return "Forked a new process: " + thread_name + " (PID: " + str(new_pid) + ")"
        else:
            return "No current process selected."

    def list_processes(self):
        table = f"{'PID':<5}{'Process Name':<15}{'Parent':<15}Threads\n"
        for pid, process in self.processes.items():
            process_name = process["name"]
            parent = process["parent"]
            parent_name = self.processes[parent]["name"] if parent else ""
            threads = ", ".join(process["threads"]) if process["threads"] else ""
            table += f"{pid:<5}{process_name:<15}{parent_name:<15}{threads}\n"
        return table



@app.route('/execute', methods=['GET'])
def get_data():
    # You can replace this data with the data you want to send as JSON.
    query_parameter = request.args.get('param')
    if (query_parameter=="help"):
        return jsonify(["This is the Help section of the OS. The following commands are available:","cd <directory> - Change directory","ls - List files and folders in the current directory","touch <filename> - Create a file","mkdir <dirname> - Create a directory","write <filename> <data> - Write data to a file","read <filename> - Read data from a file","ps - List all processes","fork <threadname> - Fork a new thread","set <processname> - Set the current process","kill <processname> - Kill a process","exit - Exit the OS"])
    elif (query_parameter=="start"):
        return jsonify("""
         _________ _______ _________          _______  _______ 
|\     /|\__   __/(  ____ )\__   __/|\     /|(  ___  )(  ____ |
| )   ( |   ) (   | (    )|   ) (   | )   ( || (   ) || (    \/
| |   | |   | |   | (____)|   | |   | |   | || |   | || (_____ 
( (   ) )   | |   |     __)   | |   | |   | || |   | |(_____  )
 \ \_/ /    | |   | (\ (      | |   | |   | || |   | |      ) |
  \   /  ___) (___| ) \ \__   | |   | (___) || (___) |/\____) |
   \_/   \_______/|/   \__/   )_(   (_______)(_______)\_______)
                       

                                                                                                                        
        """)
    elif (query_parameter=="hl"):
        return jsonify("""
  _______ _     _       _       _   _            _    _      _                       _   _                      __   _   _             ____   _____    _______ _             __      _ _               _                                                             _                                         _ _       _     _        
 |__   __| |   (_)     (_)     | | | |          | |  | |    | |                     | | (_)                    / _| | | | |           / __ \ / ____|  |__   __| |           / _|    | | |             (_)                                                           | |                                       (_| |     | |   | |     _ 
    | |  | |__  _ ___   _ ___  | |_| |__   ___  | |__| | ___| |_ __    ___  ___  ___| |_ _  ___  _ __     ___ | |_  | |_| |__   ___  | |  | | (___       | |  | |__   ___  | |_ ___ | | | _____      ___ _ __   __ _    ___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |___    __ _ _ __ ___    __ ___   ____ _ _| | __ _| |__ | | ___(_)
    | |  | '_ \| / __| | / __| | __| '_ \ / _ \ |  __  |/ _ | | '_ \  / __|/ _ \/ __| __| |/ _ \| '_ \   / _ \|  _| | __| '_ \ / _ \ | |  | |\___ \      | |  | '_ \ / _ \ |  _/ _ \| | |/ _ \ \ /\ / | | '_ \ / _` |  / __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|  / _` | '__/ _ \  / _` \ \ / / _` | | |/ _` | '_ \| |/ _ \  
    | |  | | | | \__ \ | \__ \ | |_| | | |  __/ | |  | |  __| | |_) | \__ |  __| (__| |_| | (_) | | | | | (_) | |   | |_| | | |  __/ | |__| |____) _     | |  | | | |  __/ | || (_) | | | (_) \ V  V /| | | | | (_| | | (_| (_) | | | | | | | | | | | (_| | | | | (_| \__ \ | (_| | | |  __/ | (_| |\ V | (_| | | | (_| | |_) | |  __/_ 
    |_|  |_| |_|______ __|___/  \__|_| __|\___| |_|  |_|\___|_| .__/  |___/_____\___|\__|_|\___/|_| |_|  \___/|_|   _\__|_| |_|\___|  _____/|_____(_)    |_|  |_| |_|\___| |_| \___/|_|_|\___/ \_/\_/ |_|_| |_|\__, |  \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/  \__,_|_|  \___|  \__,_| \_/ \__,_|_|_|\__,_|_.__/|_|\___(_)
         | |   / /  | (_)             | |                 \ \ | |         / ____| |                                | (_)             | |                                                                        __/ |                                                                                                                   
   ___ __| |  / / __| |_ _ __ ___  ___| |_ ___  _ __ _   _ \ \|_|______  | |    | |__   __ _ _ __   __ _  ___    __| |_ _ __ ___  ___| |_ ___  _ __ _   _                                                      |___/                                                                                                                    
  / __/ _` | < < / _` | | '__/ _ \/ __| __/ _ \| '__| | | | > > |______| | |    | '_ \ / _` | '_ \ / _` |/ _ \  / _` | | '__/ _ \/ __| __/ _ \| '__| | | |                                                                                                                                                                              
 | (_| (_| |  \ | (_| | | | |  __| (__| || (_) | |  | |_| |/ /           | |____| | | | (_| | | | | (_| |  __/ | (_| | | | |  __| (__| || (_) | |  | |_| |                                                                                                                                                                              
  ____\__,_|   \_\__,_|_|__  \___|\___|_______/|_|   \__, /_/            _\_____|_| |__\__,___| |_|\__, |\___|_ \__,_|_|_|  ____|\___|\__\___/|_|   \__, |              _         _ _               _                                                                                                                                   
 | |              | |    (_)   | |    / _(_| |        __/ |             | |  / _|    | |   | |      __/ |    (_)       | | | |                       __/ |             | |       | (_)             | |                                                                                                                                  
 | |___   ______  | |     _ ___| |_  | |_ _| | ___ ______/__ _ _ __   __| | | |_ ___ | | __| | ___ ____/___   _ _ __   | |_| |__   ___    ___ _   _ ____/_ __ ___ _ __ | |_    __| |_ _ __ ___  ___| |_ ___  _ __ _   _                                                                                                                 
 | / __| |______| | |    | / __| __| |  _| | |/ _ / __|  / _` | '_ \ / _` | |  _/ _ \| |/ _` |/ _ | '__/ __| | | '_ \  | __| '_ \ / _ \  / __| | | | '__| '__/ _ | '_ \| __|  / _` | | '__/ _ \/ __| __/ _ \| '__| | | |                                                                                                                
 | \__ \          | |____| \__ | |_  | | | | |  __\__ \ | (_| | | | | (_| | | || (_) | | (_| |  __| |  \__ \ | | | | | | |_| | | |  __/ | (__| |_| | |  | | |  __| | | | |_  | (_| | | | |  __| (__| || (_) | |  | |_| |                                                                                                                
 |_|___/          |______|_|___/_____|_|_|_|_|\___|___/  \__,_|_| |_|\__,__ |_| \___/|_|\_________|_|  |___/ |___| |_|  \__|_| |_|____|_ \___|\__,_|_|  |_|  \___|_| |_|\__|  \__,_|_|_|  \___|\___|\__\___/|_|   \__, |                                                                                                                
 | |                 | |       / // _(_| |                               \ \             / ____|              | |                / _(_| |                                                                          __/ |                                                                                                                
 | |_ ___  _   _  ___| |__    / /| |_ _| | ___ _ __   __ _ _ __ ___   ___ \ \   ______  | |     _ __ ___  __ _| |_ ___    __ _  | |_ _| | ___                                                                     |___/                                                                                                                 
 | __/ _ \| | | |/ __| '_ \  < < |  _| | |/ _ | '_ \ / _` | '_ ` _ \ / _ \ > > |______| | |    | '__/ _ \/ _` | __/ _ \  / _` | |  _| | |/ _ \                                                                                                                                                                                          
 | || (_) | |_| | (__| | | |  \ \| | | | |  __| | | | (_| | | | | | |  __// /           | |____| | |  __| (_| | ||  __/ | (_| | | | | | |  __/                                                                                                                                                                                          
  \__\___/ \__,_|\___|_| |_|   \___| |_|_|\___|_| |_|\__,_|_| |_| |_|\_____/             \_____|_|  \___|\__,_|___\___|  \__,_| |_| |_|_|\___|         _                                                                                                                                                                                
           | |     | (_)        / /  | (_)                               \ \             / ____|              | |                   | (_)             | |                                                                                                                                                                               
  _ __ ___ | | ____| |_ _ __   / / __| |_ _ __ _ __   __ _ _ __ ___   ___ \ \   ______  | |     _ __ ___  __ _| |_ ___    __ _    __| |_ _ __ ___  ___| |_ ___  _ __ _   _                                                                                                                                                              
 | '_ ` _ \| |/ / _` | | '__| < < / _` | | '__| '_ \ / _` | '_ ` _ \ / _ \ > > |______| | |    | '__/ _ \/ _` | __/ _ \  / _` |  / _` | | '__/ _ \/ __| __/ _ \| '__| | | |                                                                                                                                                             
 | | | | | |   | (_| | | |     \ | (_| | | |  | | | | (_| | | | | | |  __// /           | |____| | |  __| (_| | ||  __/ | (_| | | (_| | | | |  __| (__| || (_) | |  | |_| |                                                                                                                                                             
 |_| |_| |_|_|\_\__,_|_|_|      \_\__,_|_|_|  |_| |_|\__,_|_| |_| |_|\___/_/             \_____|_|  \___|\__,_|\__\___|  \__,_|  \__,_|_|_|  \___|\___|\__\___/|_|   \__, |                                                                                                                                                             
                                                                                                                                                                      __/ |                                                                                                                                                             
                _ _           __ __ _ _                                __       __   _       _       __             __          __   _ _             _       _       |___/                  __ _ _                                                                                                                                      
               (_| |         / // _(_| |                               \ \     / /  | |     | |      \ \            \ \        / /  (_| |           | |     | |        | |                 / _(_| |                                                                                                                                     
 __      ___ __ _| |_ ___   / /| |_ _| | ___ _ __   __ _ _ __ ___   ___ \ \   / / __| | __ _| |_ __ _ \ \   ______   \ \  /\  / _ __ _| |_ ___    __| | __ _| |_ __ _  | |_ ___     __ _  | |_ _| | ___                                                                                                                                 
 \ \ /\ / | '__| | __/ _ \ < < |  _| | |/ _ | '_ \ / _` | '_ ` _ \ / _ \ > > < < / _` |/ _` | __/ _` | > > |______|   \ \/  \/ | '__| | __/ _ \  / _` |/ _` | __/ _` | | __/ _ \   / _` | |  _| | |/ _ \                                                                                                                                
  \ V  V /| |  | | ||  __/  \ \| | | | |  __| | | | (_| | | | | | |  __// /   \ | (_| | (_| | || (_| |/ /              \  /\  /| |  | | ||  __/ | (_| | (_| | || (_| | | || (_) | | (_| | | | | | |  __/                                                                                                                                
   \_/\_/ |_|  |_|\______| __\____ __|_|\___|_| |_|\__,_|_| |_| |_|\___/_/     \_\________,_|\__\__,_/_/ _       _      \_  \/ |_|  |__\__\___|  \__,_|\__,_|\__\__,_| ____\___/   \__,_| |_| |_|_|\___|                                                                                                                                
                    | |   / // _(_| |                               \ \            |  __ \              | |     | |     | |         / _|                              / _(_| |                                                                                                                                                          
  _ __ ___  __ _  __| |  / /| |_ _| | ___ _ __   __ _ _ __ ___   ___ \ \   ______  | |__) |___  __ _  __| |   __| | __ _| |_ __ _  | |_ _ __ ___  _ __ ___     __ _  | |_ _| | ___                                                                                                                                                      
 | '__/ _ \/ _` |/ _` | < < |  _| | |/ _ | '_ \ / _` | '_ ` _ \ / _ \ > > |______| |  _  // _ \/ _` |/ _` |  / _` |/ _` | __/ _` | |  _| '__/ _ \| '_ ` _ \   / _` | |  _| | |/ _ \                                                                                                                                                     
 | | |  __| (_| | (_| |  \ \| | | | |  __| | | | (_| | | | | | |  __// /           | | \ |  __| (_| | (_| | | (_| | (_| | || (_| | | | | | | (_) | | | | | | | (_| | | | | | |  __/                                                                                                                                                     
 |_|  \___|\__,_|\__,_|_  \_|__ |_|__\___|_| |_|___,_|_| |_| |_|\___/_/            |_|  \_\___|\__,_|\__,_|  \__,_|\__,_|\__\__,_| |_| |_|  \___/|_| |_| |_|  \__,_| |_| |_|_|\___|                                                                                                                                                     
                      | |    (_)   | |         | | |                                                                                                                                                                                                                                                                                    
  _ __  ___   ______  | |     _ ___| |_    __ _| | |  _ __  _ __ ___   ___ ___ ___ ___  ___ ___                                                                                                                                                                                                                                         
 | '_ \/ __| |______| | |    | / __| __|  / _` | | | | '_ \| '__/ _ \ / __/ _ / __/ __|/ _ / __|                                                                                                                                                                                                                                        
 | |_) \__ \          | |____| \__ | |_  | (_| | | | | |_) | | | (_) | (_|  __\__ \__ |  __\__ \                                                                                                                                                                                                                                        
 | .__/|___/          |______|_|___/\__|  \__,_|_|_| | .__/|_|  \___/ \___\___|___|___/\___|___/                                                                                                                                                                                                                                        
 | |                                                 | |                                                                                                                                                                                                                                                                                
 |___           _        ___   _                     |_|_                           __              ______         _                                    _   _                        _                                                                                                                                                  
  / _|         | |      / | | | |                      | |                          \ \            |  ____|       | |                                  | | | |                      | |                                                                                                                                                 
 | |_ ___  _ __| | __  / /| |_| |__  _ __ ___  __ _  __| |_ __   __ _ _ __ ___   ___ \ \   ______  | |__ ___  _ __| | __   __ _   _ __   _____      __ | |_| |__  _ __ ___  __ _  __| |                                                                                                                                                 
 |  _/ _ \| '__| |/ / < < | __| '_ \| '__/ _ \/ _` |/ _` | '_ \ / _` | '_ ` _ \ / _ \ > > |______| |  __/ _ \| '__| |/ /  / _` | | '_ \ / _ \ \ /\ / / | __| '_ \| '__/ _ \/ _` |/ _` |                                                                                                                                                 
 | || (_) | |  |   <   \ \| |_| | | | | |  __| (_| | (_| | | | | (_| | | | | | |  __// /           | | | (_) | |  |   <  | (_| | | | | |  __/\ V  V /  | |_| | | | | |  __| (_| | (_| |                                                                                                                                                 
 |_| \___/|_|  |_|\__   \_\\__|_| |_|_|  \___|\__,_|\__,_|_| |_|\__,_|_| |_| |_|____/_/          _____  \____|_|  __|\_\  \__,_| |_| |_|\___| \_/\_/    \__|_| |_|_|  \___|\__,_|\__,_|                                                                                                                                                 
          | |     / /                                                           \ \             / ____|    | |   | | | |                                         | |                                                                                                                                                                    
  ___  ___| |_   / / _ __  _ __ ___   ___ ___ ___ ___ _ __   __ _ _ __ ___   ___ \ \   ______  | (___   ___| |_  | |_| |__   ___    ___ _   _ _ __ _ __ ___ _ __ | |_   _ __  _ __ ___   ___ ___ ___ ___                                                                                                                                
 / __|/ _ | __| < < | '_ \| '__/ _ \ / __/ _ / __/ __| '_ \ / _` | '_ ` _ \ / _ \ > > |______|  \___ \ / _ | __| | __| '_ \ / _ \  / __| | | | '__| '__/ _ | '_ \| __| | '_ \| '__/ _ \ / __/ _ / __/ __|                                                                                                                               
 \__ |  __| |_   \ \| |_) | | | (_) | (_|  __\__ \__ | | | | (_| | | | | | |  __// /            ____) |  __| |_  | |_| | | |  __/ | (__| |_| | |  | | |  __| | | | |_  | |_) | | | (_) | (_|  __\__ \__ \                                                                                                                               
 |___/\___|___|  ___| .__/|_|  \___/ \___\___|___|___|_| |_|\__,_|_| |_| |_|\___/_/           _|______ ____|\__|  \__|_| |_|\___|  \___|\__,_|_|  |_|  \___|_| |_|\__| | .__/|_|  \___/ \___\___|___|___/                                                                                                                               
 | |  (_| | |   / / | |                                                       \ \            | |/ (_| | |                                                              | |                                                                                                                                                              
 | | ___| | |  / / _|__  _ __ ___   ___ ___ ___ ___ _ __   __ _ _ __ ___   ___ \ \   ______  | ' / _| | |   __ _   _ __  _ __ ___   ___ ___ ___ ___                    |_|                                                                                                                                                              
 | |/ | | | | < < | '_ \| '__/ _ \ / __/ _ / __/ __| '_ \ / _` | '_ ` _ \ / _ \ > > |______| |  < | | | |  / _` | | '_ \| '__/ _ \ / __/ _ / __/ __|                                                                                                                                                                                    
 |   <| | | |  \ \| |_) | | | (_) | (_|  __\__ \__ | | | | (_| | | | | | |  __// /           | . \| | | | | (_| | | |_) | | | (_) | (_|  __\__ \__ \                                                                                                                                                                                    
 |_|\_|_|_|__ _ \_| .__/|_|  ______\___\_______|___|__ |_|\__,_|_| ____|_|______/            |_|\_|_|_|_|  \__,_| | .__/|_|  \___/ \___\___|___|___/                                                                                                                                                                                    
           (_| |  | |       |  ____|    (_| |   | | | |           / __ \ / ____|                                  | |                                                                                                                                                                                                                   
   _____  ___| |_ |_______  | |__  __  ___| |_  | |_| |__   ___  | |  | | (___                                    |_|                                                                                                                                                                                                                   
  / _ \ \/ | | __| |______| |  __| \ \/ | | __| | __| '_ \ / _ \ | |  | |\___ \                                                                                                                                                                                                                                                         
 |  __/>  <| | |_           | |____ >  <| | |_  | |_| | | |  __/ | |__| |____) |                                                                                                                                                                                                                                                        
  \___/_/\_|_|\__|          |______/_/\_|_|\__|  \__|_| |_|\___|  \____/|_____/   

""")
        return jsonify(query_parameter)
    elif query_parameter.startswith("cd "):
        # Parse and execute the "cd" command
        directory = query_parameter[3:]  # Extract the directory from the command
        response = file_system.cd(directory)
        return jsonify(response)

    elif query_parameter == "ls":
        # Execute the "ls" command
        response = file_system.ls()
        return jsonify(response)

    elif query_parameter.startswith("touch "):
        # Parse and execute the "touch" command
        filename = query_parameter[6:]  # Extract the filename from the command
        response = file_system.touch(filename)
        return jsonify(response)

    elif query_parameter.startswith("mkdir "):
        # Parse and execute the "mkdir" command
        dirname = query_parameter[6:]  # Extract the directory name from the command
        response = file_system.mkdir(dirname)
        return jsonify(response)

    elif query_parameter.startswith("write "):
        # Parse and execute the "write" command
        parts = query_parameter[6:].split(' ', 1)
        if len(parts) == 2:
            filename, data = parts
            response = file_system.write_file(filename, data)
            return jsonify(response)
        else:
            return jsonify("Invalid write command. Usage: write <filename> <data>")

    elif query_parameter.startswith("read "):
        # Parse and execute the "read" command
        filename = query_parameter[5:]  # Extract the filename from the command
        response = file_system.read_file(filename)
        return jsonify(response)

    elif query_parameter == "ps":
        # Execute the "ps" command
        response = process_manager.list_processes()
        return jsonify(response)

    elif query_parameter.startswith("fork "):
        # Parse and execute the "fork" command
        thread_name = query_parameter[5:]  # Extract the thread name from the command
        response = process_manager.fork(thread_name)
        return jsonify(response)

    elif query_parameter.startswith("set "):
        # Parse and execute the "set" command
        process_name = query_parameter[4:]  # Extract the process name from the command
        response = process_manager.set_current_process(process_name)
        return jsonify(response)

    elif query_parameter.startswith("kill "):
        # Parse and execute the "kill" command
        process_name = query_parameter[5:]  # Extract the process name from the command
        # Implement the logic to kill the process (not provided in the original code)
        response = "Killed process: " + process_name  # Replace this with the actual logic
        return jsonify(response)

    elif query_parameter == "exit":
        # Implement the exit command (you can add custom logic to terminate the application)
        return jsonify("Exiting the OS...")
    
visclass = FirstFit()
visclass1 = BestFit()
visclass2 = WorstFit()
visclass3 = NextFit()
m = 10
arr = [100,50,70,90,200,110,150,80,100,50]

@app.route('/Firstfit', methods=['GET'])
def FF():
    global visclass
    global m
    global arr
    query_parameter = request.args.get('param')
    if query_parameter == "start":
        visclass.reset()
        return jsonify("FirstFit started")
    elif query_parameter == "end":
        visclass.reset()
        return jsonify("FirstFit ended")

@app.route('/Firstfitadd', methods=['GET'])
def FFadd():
    global visclass
    global m
    global arr
    query_parameter = request.args.get('param')
    query_parameter = int(query_parameter)
    if visclass is None:
        return jsonify(["FirstFit not started"])
    else:
        progress = visclass.__addnew__(query_parameter)
        return jsonify([progress, visclass.m, visclass.blockSize])
@app.route('/Bestfit', methods=['GET'])
def FF1():
    global visclass1
    global m
    global arr
    query_parameter = request.args.get('param')
    if query_parameter == "start":
        visclass1.reset()
        return jsonify("FirstFit started")
    elif query_parameter == "end":
        visclass1.reset()
        return jsonify("FirstFit ended")

@app.route('/Bestfitadd', methods=['GET'])
def FFadd1():
    global visclass1
    global m
    global arr
    query_parameter = request.args.get('param')
    query_parameter = int(query_parameter)
    if visclass1 is None:
        return jsonify(["FirstFit not started"])
    else:
        progress = visclass1.__addnew__(query_parameter)
        return jsonify([progress, visclass1.m, visclass1.blockSize])
@app.route('/Worstfit', methods=['GET'])
def FF2():
    global visclass2
    global m
    global arr
    query_parameter = request.args.get('param')
    if query_parameter == "start":
        visclass2.reset()
        return jsonify("FirstFit started")
    elif query_parameter == "end":
        visclass2.reset()
        return jsonify("FirstFit ended")

@app.route('/Worstfitadd', methods=['GET'])
def FFadd2():
    global visclass2
    global m
    global arr
    query_parameter = request.args.get('param')
    query_parameter = int(query_parameter)
    if visclass2 is None:
        return jsonify(["FirstFit not started"])
    else:
        progress = visclass2.__addnew__(query_parameter)
        return jsonify([progress, visclass2.m, visclass2.blockSize])
@app.route('/Nextfit', methods=['GET'])
def FF3():
    global visclass3
    global m
    global arr
    query_parameter = request.args.get('param')
    if query_parameter == "start":
        visclass3.reset()
        return jsonify("FirstFit started")
    elif query_parameter == "end":
        visclass3.reset()
        return jsonify("FirstFit ended")

@app.route('/Nextfitadd', methods=['GET'])
def FFadd3():
    global visclass3
    global m
    global arr
    query_parameter = request.args.get('param')
    query_parameter = int(query_parameter)
    if visclass3 is None:
        return jsonify(["FirstFit not started"])
    else:
        progress = visclass3.__addnew__(query_parameter)
        return jsonify([progress, visclass3.m, visclass3.blockSize])


if __name__ == '__main__':
    file_system = FileSystem()
    process_manager = ProcessManager()
    app.run(debug=True)
