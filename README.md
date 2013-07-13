Typewriter
==========

This plugin provides two typewriter-inspired modes for Sublime Text 2 & 3:

- **Typewriter Scrolling** keeps the view centered on the current line, when there is more than half a screenful of text, à la _iA Writer_, _WriteRoom_ and the like. This mode keeps you from craning your neck to look at the bottom of the screen for hours on end. (If you happen to write for hours on end.)

- **Typewriter Typing** disables your cursor keys and all bindings that move the cursor and/or select text, leaving you only with letters, numbers, symbols, <kbd>Backspace</kbd>, <kbd>Delete</kbd> and <kbd>Enter</kbd>. Stay in the flow of writing and don't let your inner editor stifle your verbiage ever again. (Also: experience the joy of not being able to go back and correct your typos.)


## Installation

You can install Typewriter either manually or through _Package Control_. The latter is preferred as it will update automatically.

### Package Control

Typewriter is not available in _Package Control_ by default, you will need to add it first.

1. Select the `Package Control: Add Repository` command via the palette and add this repository: `https://github.com/alehandrof/Typewriter`
2. Select the `Package Control: Install Package` command via the palette and choose the newly-available `Typewriter` package.

### Manually

Clone the repository in your Packages folder: `git clone https://github.com/alehandrof/Typewriter.git`


## Usage

The typewriter modes are controlled by the `typewriter_mode_scrolling` and `typewriter_mode_typing` settings. Setting them to `true` enables the modes.

- See the example files provided for ideas on how to use these in settings & keymap files.
- You can toggle the modes via the Command Palette. (Just search for `typewriter`.)

### Notes

- Using the mouse is very difficult in the Scrolling mode and rather counter-productive in the Typing mode. I would like to disable and/or tweak its behavior, but I haven't figured out how to do so.
- The Typing mode does not work in OSX.

## Changelog & History

- 0.2 - Added Typing mode for Windows & Linux. `typewriter_mode` renamed `typewriter_mode_scrolling`.
- 0.1 - Initial release. Typewriter was created upon [my request](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806) by [castles\_made\_of\_sand](https://github.com/sublimator/) & [facelessuser](https://github.com/facelessuser).


## Issues/Todo

- Support OSX in Typing mode.
- Mousemaps
	- Disable mouse during the Typing mode.
	- Disable click & drag for selection during Scrolling mode.
- Typewriter Typing is _kind of_ a hack. A more pythonesque approach would probably be preferable.


## Alternatives

- [BufferScroll](https://github.com/SublimeText/BufferScroll) also provides "typewriter scrolling" and many other features besides.
