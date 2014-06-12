# originally created by:
# + castles_made_of_sand
# + facelessuser
# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806

import sublime
import sublime_plugin

offset = 0.0

scrolling_mode_center_on_commands = [
    "move"
]

scrolling_mode_center_on_next_selection_modified_commands = [
    "find_next",
    "find_prev"
]

typing_mode_blocked_commands = [
    "drag_select",
    "undo",
    "redo",
    "redo_or_repeat",
    "soft_undo",
    "soft_redo",
    "paste",
    "paste_and_indent",
    "paste_from_history",
    "move",
    "select_lines",
    "move_to",
    # "scroll_lines",
    "select_all",
    "expand_selection",
    "find_under_expand",
    "run_macro_file",  # "Add Line Before.sublime-macro",
    "swap_line_up",
    "swap_line_down",
    # "show_overlay" # "goto",
    "goto_definition",
    "goto_symbol_in_project",
    "jump_back",
    "jump_forward",
    # "show_panel" # "incremental_find",
    # "show_panel" # "find",
    # "show_panel" # "replace",
    "replace_next",
    "find_next",
    "find_prev",
    "find_under",
    "find_under_prev",
    "find_all_under",
    # "show_panel" # "find_in_files",
    "next_result",
    "prev_result",
    "next_misspelling",
    "prev_misspelling",
    "transpose",
    "next_bookmark",
    "prev_bookmark",
    "select_all_bookmarks",
    "select_to_mark",
    "delete_to_mark"
]


def move_cursor_to_eof(view):
    # During Typing Mode cursor is always at EOF
    eof = view.size()
    sel = view.sel()[0]
    if sel.a != eof:
        view.sel().clear()
        view.sel().add(sublime.Region(eof))
        view.show(eof)


class TypewriterMode(sublime_plugin.EventListener):

    def __init__(self):
        self.center_view_on_next_selection_modified = False

    def on_selection_modified(self, view):
        settings = view.settings()
        if settings.get('typewriter_mode_typing') == 1:
            move_cursor_to_eof(view)
        if (settings.get('typewriter_mode_scrolling') and
                self.center_view_on_next_selection_modified):
            self.center_view(view)
            self.center_view_on_next_selection_modified = False

    def on_post_text_command(self, view, command_name, args):
        if not view.settings().get('typewriter_mode_scrolling'):
            return
        if command_name in scrolling_mode_center_on_commands:
            self.center_view(view)

    def on_window_command(self, window, command_name, args):
        # This is to work around a bug in Sublime Text 3 wherein on_post_window_command
        # is not being called. Ideally that is where we should call center_view so that
        # the view is centered on the new location. Instead, we 'remember' here that
        # we need to center the view on the next selection_modified event.
        if not window.active_view().settings().get('typewriter_mode_scrolling'):
            return
        if command_name in scrolling_mode_center_on_next_selection_modified_commands:
            self.center_view_on_next_selection_modified = True

    def on_modified(self, view):
        if not view.settings().get('typewriter_mode_scrolling'):
            return
        self.center_view(view)

    # Center View
    def center_view(self, view):
        sel = view.sel()
        region = sel[0] if len(sel) == 1 else None
        if region is not None:
            global offset
            offset = sublime.load_settings('Typewriter.sublime-settings').get(
                'typewriter_mode_scrolling_offset', 0.0) * view.line_height()
            if offset != 0:
                if offset > (view.viewport_extent()[1] / 2):
                    print(
                        "Typewriter Error: The cursor is outside the viewport! Use a smaller offset value.")
                else:
                    region = sublime.Region(
                        self.offset_point(view, region.a), self.offset_point(view, region.b))
            view.show_at_center(region)

    def offset_point(self, view, point):
        vector = list(view.text_to_layout(point))
        vector[1] = vector[1] + offset
        return view.layout_to_text(tuple(vector))

    # Block Commands
    def on_text_command(self, view, cmd, args):
        blocked = False
        if view.settings().get('typewriter_mode_typing') == 1:
            blocked = self.block_commands(
                view, cmd, args, typing_mode_blocked_commands)
        if blocked:
            return ("do_nothing")

    def block_commands(self, view, cmd, args, blocked_cmds):
        for i in blocked_cmds:
            if cmd == i:
                return (True)


# Typing Mode Command
class TypewriterTypingToggleCommand(sublime_plugin.TextCommand):

    """
    Toggle typewriter_mode_typing, placing the cursor at the end of the file when toggling on.
    """

    def run(self, edit):
        view = self.view
        settings = self.view.settings()
        if settings.get('typewriter_mode_typing') != 1:
            settings.set('typewriter_mode_typing', 1)
            move_cursor_to_eof(view)
            return
        else:
            settings.set('typewriter_mode_typing', 0)
