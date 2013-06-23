import sublime, sublime_plugin

class ToggleGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        ngroups = self.window.num_groups()
        curgroup = self.window.active_group()
        curgroup += 1
        if curgroup >= ngroups:
            curgroup = 0
        self.window.focus_group(curgroup)
