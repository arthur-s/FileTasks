import os
import shlex
import sublime
import sublime_plugin
import subprocess

settings = sublime.load_settings("FileTasks.sublime-settings")



def get_replaced_cmd(cmd_str, file_full_path, custom_replace=None):
    
    filedir, filename = os.path.split(file_full_path)

    if '__file__' in cmd_str:
        cmd_str = cmd_str.replace('__file__', file_full_path)

    if '__filename__' in cmd_str:
        cmd_str = cmd_str.replace('__filename__', filename)

    if '__filedir__' in cmd_str:
        cmd_str = cmd_str.replace('__filedir__', filedir)

    # custom replacements
    if custom_replace is None:
        custom_replace = {}
    for replacement in custom_replace:
        if replacement in cmd_str:
            cmd_str = cmd_str.replace(replacement, custom_replace[replacement])

    # relative paths, if workdir was defined
    if '__workdir__' in custom_replace:
        workdir = custom_replace['__workdir__']
        workdir = os.path.normpath(workdir) + '/'
        splitted = file_full_path.split(workdir)
        if len(splitted) == 2:
            relative_file_path = splitted[1]
            cmd_str = cmd_str.replace('__relative_file_path__', relative_file_path)
        else:
            return False

    return cmd_str



class FileTasksRunTaskCommand(sublime_plugin.WindowCommand):
    def run(self):
        self._tasks = settings.get('tasks')
        if self._tasks is None:
            window.status_message('Couldnt load settings')
        
        self._items = [k for k in self._tasks]

        self.window.show_quick_panel(self._items, self.on_select)

    def on_select(self, index):
        """callback function on option select
        """
        if index != -1:
            key = self._items[index]
            tasks_obj = self._tasks[key]
            command = tasks_obj.get('command')
            # print(command)
            custom_replace = self._tasks[key].get('custom_replace')

            view = self.window.active_view()
            filename = view.file_name()
            cmd = get_replaced_cmd(command, filename, custom_replace)
            # print('Final cmd', cmd)
            if cmd is not False:
                cmd = shlex.split(cmd)
                subprocess.call(cmd, shell=False)
                print('cmd executed', cmd)
