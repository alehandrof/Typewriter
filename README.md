Typewriter
==========

This plugin provides two typewriter-inspired modes for Sublime Text 2 & 3:

- **Typewriter Scrolling** keeps the view centered on the current line, when there is more than half a screenful of text, à la _iA Writer_, _WriteRoom_ and the like. This mode keeps you from craning your neck to look at the bottom of the screen for hours on end. (If you happen to write for hours on end.)

- **Typewriter Typing** disables your cursor keys and all bindings that move the cursor and/or select text, leaving you only with letters, numbers, symbols, <kbd>Backspace</kbd>, <kbd>Delete</kbd> and <kbd>Enter</kbd>. Stay in the flow of writing and don't let your inner editor stifle your verbiage ever again. (Also: experience the joy of not being able to go back and correct your typos.)


## Installation

This plugin is available through [Package Control](https://sublime.wbond.net/).

Select the `Package Control: Install Package` command via the palette and choose the `Typewriter` package.

### Manual Install

1. Download the latest release from here: <https://github.com/alehandrof/Typewriter/releases/>
2. Extract it in your Packages folder. (You can find out its location by clicking the `Preferences > Browse Packages…` menu inside Sublime Text.)

-- _or_ --

Clone the repository in your Packages folder: `git clone https://github.com/alehandrof/Typewriter.git`


## Usage

The typewriter modes are controlled by the `typewriter_mode_scrolling` and `typewriter_mode_typing` settings. Setting them to `true` enables the modes.

- See the files provided for ideas on how to use these in settings & keymap files.
- You can toggle the modes via the:
	- Command Palette -- search for `typewriter`
	- Main Menu menu -- under `View > Typewriter`.

### Notes

- Using the mouse is very difficult in the Scrolling mode and rather counter-productive in the Typing mode. I would like to disable and/or tweak its behavior, but I haven't figured out how to do so.
- Neither mode is designed to work with multiple cursors.
- The Typing mode does not work in OSX.


## Changelog & History

- 0.2.3 - Added offset option for Scrolling mode (requested by [Luis Martins](https://github.com/lmartins)).
- 0.2.2 - Typing mode now supports OSX as well.
- 0.2.1 - Renamed settings to `typewriter_mode_scrolling` and `typewriter_mode_typing` so they won't conflict with BufferScroll.
- 0.2 - Added Typing mode for Windows & Linux. `typewriter_mode` renamed `typewriter_scrolling`.
- 0.1 - Initial release. Typewriter was created upon [my request](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806) by [castles\_made\_of\_sand](https://github.com/sublimator/) & [facelessuser](https://github.com/facelessuser).


## Issues/Todo

- Typing mode for OSX is currently untested (Current state: waiting for feedback)
- Mousemaps (Current state: researching)
	- Disable mouse during the Typing mode.
	- Disable click & drag for selection during Scrolling mode.
- Typewriter Typing is _kind of_ a hack. A more pythonesque approach would probably be preferable.
- Add Markdown syntax (Current state: rough draft)
- Add color scheme designed for prose/long text (Current state: near complete)


## Alternatives

- [BufferScroll](https://github.com/SublimeText/BufferScroll) also provides a version of "typewriter scrolling" and many other features besides.
