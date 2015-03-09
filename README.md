# pygame_base

This is the initial pygame loop code with everything you need: window, caption, key processing stub, and logic processing separated from drawing processing, so it prevents game from slowing down when drawing does lag.

## Why separate "Game" class?

Because you may probably want to create variable-controlled gamemodes with different init/logic/drawing code (e.g. N players). Maybe you'll even consider to move this class to another file.