# FileTasks
Inspired by VScode's [tasks](https://code.visualstudio.com/docs/editor/tasks) feature.

## Installation
Currently this plugin is not added to Package Control, so you need to install it manually. 
Clone in Sublime's packages directory (Preferences -> Browse Packages) this repo. E.g. for Ubuntu users it may be:
```
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/arthur-s/FileTasks.git
```

## Setup
Real world example - copy files from laptop to remote server:
```json
{
    "tasks": {
        "copy example.com": { // name of task
            "command": "scp __file__ example.com:/home/arthur/project/__relative_file_path__",
            "workdir": "/home/arthur/work" //optionally you may set workdir
        },
    }
}
```

Reserved words are `tasks`, `command` and `workdir`. 
You may use variables in command string. Variables looks like \_\_var\_\_ (with double underscores in both ends). Variables list is (and with what it will be replaced, if your active opened file is `/home/arthur/work/project/app1/models/model.js`):

* \_\_file\_\_ - replaces with file full path (`/home/arthur/work/project/app1/models/model.js`)
* \_\_filename\_\_ - replaces with file name (`model.js`)
* \_\_filedir\_\_ - file's direcrory path (`/home/arthur/work/project/app1/models`)
* \_\_relative_file_path\_\_ - if `workdir` is set, `workdir` will be cutted from fullpath (if workdir is `/home/arthur/work`, then `__relative_file_path__` will be replaced with `project/app1/models/model.js`)

# TODO
* show response message when tasks finishes
* show error when command fails
* add debug mode
* add ability to do tasks for directories in project
