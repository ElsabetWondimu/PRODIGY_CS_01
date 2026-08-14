# Caesar Cipher – Task 01 (Prodigy InfoTech Cybersecurity Internship)

For my first task with Prodigy InfoTech I had to build a Caesar Cipher — basically a small tool that scrambles text using a shift number, and can unscramble it again if you know the shift. I did it in Python, then also made a quick browser version because I wanted to see it running somewhere other than a terminal.

## What's a Caesar Cipher anyway?

It's one of the oldest tricks in the book, literally — named after Julius Caesar because he supposedly used it to send military orders that wouldn't make sense if someone intercepted them. All it does is push every letter a certain number of spots down the alphabet. Shift by 3 and A turns into D, B turns into E, and so on until you loop back around at Z.

Not exactly hard to crack by today's standards (you could brute-force all 26 shifts in a second), but it's a good starting point for understanding how encryption works at a basic level.

## What my version does

- Takes any message and shifts it by whatever number you type in
- Can also reverse it back to the original if you give it the same shift
- Doesn't touch spaces, punctuation, or numbers — just the letters
- Works whether you type in caps or lowercase
- I made two versions: one you run from the terminal, one you just open in a browser

## Files here

- `caesar_cipher.py` — run this if you want the terminal version
- `index.html` — open this in a browser, no setup needed

## How to actually run it

If you're using Python:
```bash
python caesar_cipher.py
```
It'll ask if you want to Encrypt, Decrypt, or Quit, then just follow along from there.

Or skip Python entirely and open `index.html`, or use the live link below.

## Live version

https://ElsabetWondimu.github.io/PRODIGY_CS_01/

## Quick example

Type in: `Meet at the old bridge at dawn`
With shift `3` you get: `Phhw dw wkh ROG eulgjh dw gdzq`

## Author

[ElsabetWondimu](https://github.com/ElsabetWondimu) — made this for the Prodigy InfoTech Cybersecurity internship.
