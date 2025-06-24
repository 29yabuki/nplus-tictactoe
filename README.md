# N+ Tic-Tac-Toe

**N+ Tic-Tac-Toe** is a creative fusion of two unique twists on the classic game: **Tic-Tac-Toe+** and **N-Tac-Toe**.

This repository contains a command-line interface (CLI) implementation of the game.

## 🎯 What is Tic-Tac-Toe+?

Tic-Tac-Toe+ is played on a 3x3 grid of mini Tic-Tac-Toe boards. 

Here's how it works:
- The first player can place their ‘X’ anywhere on any of the nine boards.
- The position of that move determines _which board_ the next player must play on.
  - For instance: if Player 1 plays in the **top-right square** of their current board, Player 2 must play on the **top-right board**.
- Each mini board is a regular Tic-Tac-Toe game.
- Winning a mini board marks that board with your symbol.
- Win three boards in a row (like regular Tic-Tac-Toe), and you win the whole game.

For a visual explanation, check out this [short video on Tic-Tac-Toe+](https://www.youtube.com/watch?v=_Na3a1ZrX7c).

## 🚫 What is N-Tac-Toe?

N-Tac-Toe has the following mechanics:
- **Both players use the same symbol: ‘X’.**
- The objective is to **avoid completing** a row, column, or diagonal of three X’s.
- If you’re the player who completes the line, **you lose**.

For example, if a player places an ‘X’ that results in three X’s diagonally, they lose the game.
