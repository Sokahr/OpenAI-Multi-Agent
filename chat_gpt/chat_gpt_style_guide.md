Updated Style Guide for CLI Application:

## Font Choices:

- Utilize the default font of the terminal emulator.
    - CLI applications typically inherit the font settings of the terminal emulator being used, and users do not have
      control over changing the font within the CLI application itself.

## Color Palette:

- Primary Color: #ffffff (White)
- Secondary Color: #00ff00 (Green)
- Background Color: #000000 (Black)
- Accent Color: #ffff00 (Yellow)
- Error Color: #ff0000 (Red)

## Typography:

- Use the default font and styling of the terminal emulator.
- Prioritize legibility and clarity over decorative or stylized fonts.

## Buttons and Interactive Elements:

- Instead of graphical buttons, utilize clear and concise command options.
- Use ASCII characters or symbols to visually represent interactive elements or command options.

## Input Fields:

- Represent input fields using prompts followed by the user's input on the same line.
- Use clear prompts to guide users on the expected inputs.
- Ensure the user's input is distinguishable from the prompt or surrounding text through visual cues such as different
  text colors or brackets.

## Terminal Compatibility:

- Design the CLI interface to be compatible with various terminal emulators.
- Avoid relying on advanced styling or rendering features that may not be supported universally across terminal
  emulators.

## Responsive Design:

- CLI applications do not have responsive layouts like GUI applications, but ensure the interface remains usable and
  readable on different terminal window sizes.
- Avoid fixed-width elements or hard-coded dimensions that may cause layout issues or text truncation in smaller
  terminal windows.
- Adjust the output or formatting based on the size of the terminal window to optimize readability.

Please note that in CLI applications, the styling is limited by the capabilities and settings of the terminal emulator
itself. The CLI application should adapt to the default settings and font of the terminal emulator being used by the
user.