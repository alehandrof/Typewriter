# originally created by:
# + castles_made_of_sand
# + facelessuser
# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806

import sublime, sublime_plugin

class TypewriterScrolling(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        if view.settings().get('typewriter_mode_scrolling') == 1:
            sel = view.sel()
            region = sel[0] if len(sel) == 1 else None
            if region != None:
                offset = sublime.load_settings('Typewriter.sublime-settings').get('typewriter_mode_scrolling_offset', 0.0)
                if offset != 0:
                    offset = offset * view.line_height()
                    if offset > view.viewport_extent()[1] / 2:
                        print("Typewriter: The cursor is not within the viewport! Use a smaller offset value.")
                    region_a    = list(view.text_to_layout(region.a))
                    region_b    = list(view.text_to_layout(region.b))
                    region_a[1] = region_a[1] + offset
                    region_b[1] = region_b[1] + offset
                    region      = sublime.Region(view.layout_to_text(region_a), view.layout_to_text(region_b))
                view.show_at_center(region)
